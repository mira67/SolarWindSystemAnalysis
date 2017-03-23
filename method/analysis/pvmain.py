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
outPath = 'E:/myprojects/pv_detection/data/stage1_2/'
reportPath = 'E:/myprojects/pv_detection/data/experiment_results/'
#column names
colNames = ['I1','I10','I11','I12','I13','I14','I15','I16','I2','I3','I4','I5','I6','I7','I8','I9'];
# generate date list, process by day
start = datetime.datetime.strptime("2016-06-01", "%Y-%m-%d").date()
end = datetime.datetime.strptime("2016-07-02", "%Y-%m-%d").date()
dateList = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

# this is just for one day testing
dateName = '#data_date'
timeRg = ['08:00','17:00'];#maybe calculate based on the sunshine value, contextual information
interval = 10;#every n min sampling
stringNum = 16
#total number of strings
totalVString = 553*16
    
#daily clustering results
numDays = len(dateList)

def faultDetection(fullname):
    # read module    
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
                
                # test
                #kLen = 5
                #x = np.array([[0],[0.988518519],[0.15259259],[0.314814815],[0.314814815],[0.314814815],[0.092592593],[0.296296296],[0.314814815],[0.111111111],[0],[0],[0.018518519],[0],[0],[0.01851851]])
                
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
    

def falseAlarmRemoval(dayId, method, K):
    rlist = glob.glob(outPath+'*.csv') 
    
    #initialize empty table for daily report 
    dayStrings = pd.DataFrame(index=range(totalVString), columns=['stringName','dt','cluster','fault']) 
    stringName = ['' for s in range(totalVString)] 
    dutyCycle = np.zeros((totalVString,1))
    cluster = np.zeros((totalVString,1))
    strCount = 0
    if method == 'cluster':
        for rf in rlist:
            # read module    
            df = pd.read_csv(rf)
            df = df[df['date'] == dayId]
            # construct string name and duration table
            hlx = os.path.basename(rf)
            for cuan in colNames:
                stringName[strCount] = hlx+'_'+cuan
                dutyCycle[strCount] = df[cuan]
                strCount = strCount + 1
    #clustering, test with kmeans first, then GMM
    clusters = KMeans(n_clusters=K, random_state=0).fit(dutyCycle)
    centroids = clusters.cluster_centers_
    #fault identification - sort centroids                     
    sortedIdx = np.argsort(centroids,axis=1,kind='mergesort')
    sortedCentroids = centroids[sortedIdx]
    #fault identification - find gap
    diff2 = np.diff(sortedCentroids, n=2)
    peakind = signal.find_peaks_cwt(diff2)
    gap = sortedCentroids(peakind)
    #for all dutyCycle greater than gap, reported as fault
    fault = np.less(dutyCycle,gap)                                                                                                          
    return 'ok'

# summarize reulsts, print daily fault strings to file

if __name__ == '__main__':
    
    if localStage == 1:
        print 'Running Global Stage...'
        
        inPath = 'E:/myprojects/pv_detection/data/test/'
        flist = glob.glob(inPath+'*.csv')
        #profiling 2
        start = time.time()    
        for f in flist:
            print f
            faultDetection(f)
        
        end = time.time()
        runtime = end - start
        msg = "Single Thread Took {time} seconds to complete"
        print(msg.format(time=runtime))
    
        
    '''
        #profiling 1
        start = time.time()
        pool = mp.Pool(4)
        results = pool.map(faultDetection, newList)
        
        end = time.time()
        runtime = end - start
        msg = "Multi-Processing Took {time} seconds to complete"
        print(msg.format(time=runtime))
    '''
        
    '''
        #dir1 = 'E:/myprojects/pv_detection/data/filtered/'
        #dir2 = 'E:/myprojects/pv_detection/data/stage1/'
        
        #results = filecmp.dircmp(dir1, dir2)
        
        #flist = results.left_only
        #newList = []
        #for f in flist:
        #    f = dir1+f
        #    newList.append(f)
    '''
    if globalStage == 1:
        start = time.time()  
        
        print 'Running Global Stage...'
        date = '2016-06-06'
        method = 'cluster'
        falseAlarmRemoval(date, method, 20)
        
        end = time.time()
        runtime = end - start
        msg = "Single Day False Alarm Removal Took {time} seconds to complete"
        print(msg.format(time=runtime))
        print 'TEST DONE'