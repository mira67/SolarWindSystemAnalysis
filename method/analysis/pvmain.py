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

#global variables
outPath = 'E:/myprojects/pv_detection/data/stage1_2/'
reportPath = 'E:/myprojects/pv_detection/data/experiment_results/'
#column names
colNames = ['I1','I10','I11','I12','I13','I14','I15','I16','I2','I3','I4','I5','I6','I7','I8','I9'];
# generate date list, process by day
start = datetime.datetime.strptime("2016-06-01", "%Y-%m-%d").date()
end = datetime.datetime.strptime("2016-06-03", "%Y-%m-%d").date()
dateList = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

# this is just for one day testing
dateName = '#data_date'
timeRg = ['08:00','17:00'];#maybe calculate based on the sunshine value, contextual information
interval = 10;#every n min sampling
stringNum = 16;
    
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
                    clusters = np.insert(clusters, pos, -1)                       
                                                    
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
    

def falseAlarmRemoval(method):
        if method == 'threshold':
            
            return 'ok'
            
        if method == 'cluster':
            return 'ok'

# summarize reulsts, print daily fault strings to file

if __name__ == '__main__':
    inPath = 'E:/myprojects/pv_detection/data/test/'
    flist = glob.glob(inPath+'*.csv');
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