#PV Fault Classification using DTW and K-NN
#Author: Qi Liu
#Email: qliu.hit@gmail.com

from ts_classifier import ts_classifier
import numpy as np
import pandas as pd 
from sklearn import preprocessing
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report

import time

#global settings
kfold = 5 # cross validation
inPath = 'E:/myprojects/pv_detection/code/python/data.csv'
outPath = 'E:/myprojects/pv_detection/code/python/report.csv'
w = 4

#KNN class
knn = ts_classifier()

#dataset partition to train and test
def pvKfoldValidation(data,kfold,w):
    skf = StratifiedKFold(n_splits=kfold)
    nCols = data.shape[1]
    #extract attributes and class target
    X = data.iloc[:,1:nCols-1].as_matrix()
    y = data.iloc[:,-1].as_matrix()
    #encode string labels to numeric labels
    le = preprocessing.LabelEncoder()
    le.fit(y)
    Y = le.transform(y)
    #report file
    rpt = open(outPath, "a+")
    #cross validation
    for train, test in skf.split(X, Y):
        trainX = X[train,:] 
        testX = X[test,:]
        trainY = Y[train].reshape((len(train),1))
        testY = Y[test].reshape((len(test),1))
        train = np.append(trainX, trainY, axis=1)
        test = np.append(testX, testY, axis=1)
        report = pvKNN(train,test,w)
        rpt.write(report)
        #classifaction_report_csv(report)
    #close report file
    rpt.close()
    return 'ok'

#classification
def pvKNN(train,test,w):
    preds=[]
    for ind,i in enumerate(test):
        min_dist=float('inf')
        closest_seq=[]
        #print ind
        for j in train:
            if knn.LB_Keogh(i[:-1],j[:-1],5)<min_dist:
                dist=knn.DTWDistance(i[:-1],j[:-1],w)
                if dist<min_dist:
                    min_dist=dist
                    closest_seq=j
        preds.append(closest_seq[-1])
    return classification_report(test[:,-1],preds)

#record results to file    
def classifaction_report_csv(report):
    report_data = []
    lines = report.split('\n')
    for line in lines[2:-3]:
        row = {}
        row_data = line.split('      ')
        row['class'] = row_data[0]
        row['precision'] = float(row_data[1])
        row['recall'] = float(row_data[2])
        row['f1_score'] = float(row_data[3])
        row['support'] = float(row_data[4])
        report_data.append(row)
    dataframe = pd.DataFrame.from_dict(report_data)
    dataframe.to_csv(outPath, index = False)
    
if __name__ == '__main__':
    #profiling
    start = time.time()
    
    data = pd.read_csv(inPath, delimiter=',', header=None)
    pvKfoldValidation(data,kfold,w)
    
    end = time.time()
    runtime = end - start
    msg = "PV Classification Tooks {time} seconds to complete"
    print(msg.format(time=runtime)) 