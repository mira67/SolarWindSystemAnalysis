"""PV String Level Fault Detection
   Author: Qi Liu
   Email: qliu.hit@gmail.com
"""
import pandas as pd
import numpy as np
from pvalgs import fdGMM
from sklearn.mixture import GMM
from matplotlib import pyplot as plt
import datetime
import multiprocessing as mp
import glob
import os
import time
import filecmp
from sklearn.cluster import KMeans
from scipy import signal

#running stages
localStage = 0
globalStage = 1

#data paths
#input hlx data
inPath = 'E:/myprojects/pv_detection/data/smoothedData_xinjiang/'
#output local stage path, change stage1 to dir like /local_03_23_5min_08_17
outPath = 'E:/myprojects/pv_detection/data/experiment_results/xinjiang_local_05_12_10min_02_17/'
#report path, global path  /global_03_23_5min_08_17
reportPath = 'E:/myprojects/pv_detection/data/experiment_results/xinjiang_global_05_12_10min_02_17/'

#column names
colNames = ['I1','I10','I11','I12','I13','I14','I15','I16','I2','I3','I4','I5','I6','I7','I8','I9'];

# generate date list, process by day
start = datetime.datetime.strptime("2017-02-01", "%Y-%m-%d").date()
end = datetime.datetime.strptime("2017-02-28", "%Y-%m-%d").date()
dateList = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

dayList = []
for day in dateList:
    dayList.append(str(day))
print dayList

# this is just for one day testing
dateName = '#data_date'
timeRg = ['00:00','12:00'];#maybe calculate based on the sunshine value, contextual information
interval = 10;#every n min sampling
stringNum = 16
#total number of strings
totalVString = 294*16
    
#daily clustering results
numDays = len(dateList)

#list of local results for global stage use
localList = glob.glob(outPath+'*.csv') 

def faultDetection(fullname):
    # read module    
    print fullname
    
    df = pd.read_csv(fullname)
    
    #day result array
    faultArr = np.zeros((numDays,stringNum),dtype=np.float)
    dayCount = 0
    #downsample data at regular interval
    df = df.iloc[::interval,:]
    for dt in dateList:
        dfday = df[(df[dateName] > str(dt)+' '+timeRg[0]) & (df[dateName] < str(dt)+' '+timeRg[1])]  

        dayT = dfday.count(axis=1)
        lenT = len(dayT)
        
        # intialize disctionary data structure for fault count of each string
        dayFaultCount = np.zeros((1,stringNum),dtype=np.float);
        
        try:#excetpion catch is necessary for robust code
            for t in range(lenT):
                
                # grab strings I from each timestamp
                x=dfday.iloc[t,1:stringNum+1].as_matrix().reshape(stringNum,1)

                #dealing with missing data
                zeroId = np.where(x == 0)[0]
                nonZeroId = np.nonzero(x)[0]
                kLen = len(nonZeroId)/2#reduce cluster numbers
                
                #need test this part
                if kLen > 0:#if all strings are zero
                    #stringNum shall equal non-zeros members
                    clusters,centroids,ck = fdGMM(x[nonZeroId],kLen)                         
                    #set cluster with largest mean to 0, set others to 1
                    maxId = np.argmax(centroids)
                    clusters[clusters==maxId] = -1
                    clusters[clusters!=-1] = 1
                    clusters[clusters==-1] = 0
                else:
                    clusters = np.zeros((1,stringNum),dtype=np.float)    
                
                if (len(zeroId) > 0 and len(zeroId) < stringNum):
                    #insert missing values position back
                    offset = np.arange(len(zeroId))
                    pos = zeroId - offset
                    clusters = np.insert(clusters, pos, 0)                       
                                                    
                #accumulate for fault string 
                dayFaultCount = dayFaultCount + clusters
        except:
            print 'error on %s, but pass' % (dt)
            
        dayFaultCount = dayFaultCount/lenT    
        faultArr[dayCount,:] = dayFaultCount
        dayCount = dayCount + 1
    
    # record to file: date + strings fault alarms
    datesArr = np.asarray(dateList)
    dayResults = pd.DataFrame(faultArr, columns=colNames)
    dayResults['date'] = datesArr
    
    #record local context detection results
    hlx = os.path.basename(fullname)
    dayResults.to_csv(outPath+hlx)

    return 'Success!'
    

def falseAlarmRemoval(dayId):
    #maximal number of clusters assumed
    K = 20
    
    #initialize empty table for daily report 
    dayStrings = pd.DataFrame(index=range(totalVString), columns=['stringName','dt','cluster','fault']) 
    stringName = ['' for s in range(totalVString)] 
    dutyCycle = np.zeros((totalVString,1))
    strCount = 0
    
    print 'Construct Report on day %s' % (dayId)

    for rf in localList:
        # read module    
        df = pd.read_csv(rf)
        df = df[df['date'] == dayId]
        # construct string name and duration table
        hlx = os.path.basename(rf)
        for cuan in colNames:
            stringName[strCount] = hlx+'_'+cuan
            dutyCycle[strCount] = df[cuan]
            strCount = strCount + 1
    
    #
    try:
        #clustering, test with kmeans first, then GMM
        clusters = KMeans(n_clusters=K, random_state=0).fit(dutyCycle)
        centroids = clusters.cluster_centers_
        #fault identification - sort centroids                     
        sortedIdx = np.argsort(centroids,axis=0,kind='mergesort')
        sortedCentroids = centroids[sortedIdx]
        #fault identification - find gap
        diff2 = np.diff(sortedCentroids, n=2, axis=0)
        diff2 = diff2.reshape((1,K-2))
        peakind = signal.find_peaks_cwt(diff2[0],np.arange(1,totalVString))
        #if works, why this parameter
        gap = sortedCentroids[peakind[0]+2]#offset by 1
        #for all dutyCycle greater than gap, reported as fault
        fault = np.greater(dutyCycle,gap)
        #construct table and report day by day
        dayStrings['stringName'] = stringName
        dayStrings['dt'] = dutyCycle
        dayStrings['cluster'] = clusters.labels_
        dayStrings['fault'] = fault 
        #write to file report
        dayStrings.to_csv(reportPath+dayId+'.csv') 
    #
    except:
        print 'error on %s, but pass' % (dayId)
                                                                                                             
    return 'ok'

# summarize reulsts, print daily fault strings to file

if __name__ == '__main__':
    
    if localStage == 1:
        print 'Running Local Stage...'
        
        flist = glob.glob(inPath+'*.csv')
            
        #profiling 1
        start = time.time()
        pool = mp.Pool(3)
        results = pool.map(faultDetection, flist)
        
        end = time.time()
        runtime = end - start
        msg = "Local Multi-Processing Took {time} seconds to complete"
        print(msg.format(time=runtime))
   
   
    if globalStage == 1:
        #global timing 
        start = time.time()
        
        print 'Running Global Stage...'
        #date = '2016-06-06'#dateList
        pool = mp.Pool(3)
        results = pool.map(falseAlarmRemoval, dayList)
        
        end = time.time()
        runtime = end - start
        msg = "Global Stage Multi-Processing Took {time} seconds to complete"
        print(msg.format(time=runtime))
        
        print 'TEST DONE'