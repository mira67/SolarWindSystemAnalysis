#PV Fault Classification using DTW and K-NN
#Author: Qi Liu
#Email: qliu.hit@gmail.com

from ts_classifier import ts_classifier
import numpy as np
import pandas as pd 
from sklearn import preprocessing
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report,confusion_matrix
from sklearn import neighbors 
from sklearn import svm 
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans

import time

#global settings
kfold = 2 # cross validation
#inPath = 'E:/myprojects/pv_detection/code/python/smoothedTimeSeriesADI.csv'
inPath = '/Users/zhaoyingying/PVData/ADIbyCen/ADIALLTimeSeriesAmptitude.csv'
#predsPath = '/Users/zhaoyingying/PVData/ADIbyCen/preds_AMT_report.csv'
outPath = '/Users/zhaoyingying/PVData/ADIbyCen/AMT_report.csv'

w = 4
AnomalyTypeNum = 5
#FaultNum = 1044
#removing some soiling labeling on rainny day
FaultNum = 1034
#KNN class
knn = ts_classifier()

def getTrueLable():
    truelabel = []
    tmp = pd.read_csv(inPath).loc[:,'AnomalyType']
    for i in range(FaultNum):
        truelabel.append(tmp.iloc[i])
#    for i in range(FaultNum):
#        if tmp.iloc[i] == 'type1':
#            print(tmp.iloc[i])
#            truelabel.append(2)
#        if tmp.iloc[i] == 'type2':
#            truelabel.append(0)
#        if tmp.iloc[i] == 'type3':
#            truelabel.append(4)           
#        if tmp.iloc[i] == 'type4':
#            truelabel.append(3)
#        if tmp.iloc[i] == 'type5':
#            truelabel.append(1)
    return truelabel
    

def Kmeans():
    preds = []
    Amptitude = np.zeros((FaultNum,1))
    tmp = pd.read_csv(inPath).loc[:,'Amp']
    for i in range(FaultNum): 
        Amptitude[i] = tmp.iloc[i]
    kmeans = KMeans(n_clusters=AnomalyTypeNum,random_state=0).fit(Amptitude)
    preds = kmeans.labels_
    preds.astype(int)
    newpreds = []
    for i in range(FaultNum):
        if preds[i] == 2:
            newpreds.append('type1')
        if preds[i] == 0:
            newpreds.append('type2')
        if preds[i] == 1:
            newpreds.append('type3')
        if preds[i] == 4:
            newpreds.append('type4')
        if preds[i] == 3:
            newpreds.append('type5')
    print(newpreds)
    
   # np.savetxt(predsPath, preds,fmt='%.0f')
    truelabel = getTrueLable()
    
    rpt = open(outPath, "a+")
    report = classification_report(truelabel,newpreds)
    print(report)
    rpt.write(report)
    rpt.close()

    return 'OK'

    
if __name__ == '__main__':
    #profiling
    steplen = 10
    #result_matrix = readFile(inPath_2, steplen)
    
    start = time.time()
    Kmeans()
    
    end = time.time()
    runtime = end - start
    msg = "PV Classification Tooks {time} seconds to complete"
    print(msg.format(time=runtime)) 
    