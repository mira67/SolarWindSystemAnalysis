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
from sklearn.naive_bayes import GaussianNB, MultinomialNB #Bayes
import time

#global settings
kfold = 2 # cross validation
#inPath = 'E:/myprojects/pv_detection/code/python/smoothedTimeSeriesADI.csv'
#inPath = 'D:/Xiaomei/SolarEnergy/SolarEnergy/python/classificationADI/ADItimeseries/0600_1800/ADIbyCen/newstates10.csv'
#outPath = 'D:/Xiaomei/SolarEnergy/SolarEnergy/python/classificationADI/ADItimeseries/0600_1800/ADIbyCen/DTW_report_newstates10.csv'
inPath = '/Users/zhaoyingying/PVData/ADIbyCen/processedtimeSeriesADIType.csv'
outPath = '/Users/zhaoyingying/PVData/ADIbyCen//shape_report.csv'
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

#select different interval:1min, 5min, 10min...
def pvKfoldValidation_select(data,kfold,w,steplen):
    skf = StratifiedKFold(n_splits=kfold)
    nCols = data.shape[1]
    #extract attributes and class target
    X = data.iloc[:,1:nCols-1:steplen].as_matrix()
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
        #swap train and test
        trainX,testX = testX, trainX
        
        trainY = Y[train].reshape((len(train),1))
        testY = Y[test].reshape((len(test),1))
        #swap train and test
        trainY, testY = testY, trainY
        train = np.append(trainX, trainY, axis=1)
        test = np.append(testX, testY, axis=1)
        report = pvKNN(train,test,w)
        rpt.write(report)
        #classifaction_report_csv(report)
    #close report file
    rpt.close()
    return 'ok'
    
def pvKfoldValidation1(data,kfold,w):
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
    for train_index, test_index in skf.split(X,Y):
        trainX = X[train_index,:] 
        testX = X[test_index,:]
        trainY = Y[train_index].reshape((len(train_index),1))
        testY = Y[test_index].reshape((len(test_index),1))
#        train = np.append(trainX, trainY, axis=1)
#        test = np.append(testX, testY, axis=1)
        report = GMM(trainX,testX,trainY,testY)
        rpt.write(report)
#        report = pvKNN(train,test,w)
#        rpt.write(report)
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

def KNN(trainX,testX,trainY,testY):
    knn = neighbors.KNeighborsClassifier(n_neighbors=1) 
    knn.fit(trainX, trainY)
    preds = knn.predict(testX)
    conMar = confusion_matrix(testY,preds)
    print(conMar)
    return classification_report(testY,preds)

def SVM(trainX,testX,trainY,testY):
    svc = svm.SVC() 
    svc.fit(trainX, trainY)
    preds = svc.predict(testX)
    conMar = confusion_matrix(testY,preds)
    print(conMar)
    return classification_report(testY,preds)

def GMM(trainX,testX,trainY,testY):
    gmm = GaussianMixture()
    gmm.fit(trainX, trainY)
    preds = gmm.predict(testX)
    conMar = confusion_matrix(testY,preds)
    print(conMar)
    return classification_report(testY,preds)
#record results to file    
def classifaction_report_csv(report):
    report_data = []
    lines = report.split('\n')
    for line in lines[2:-3]:
        row = {}
        print(line)
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
    steplen = 10
    #result_matrix = readFile(inPath_2, steplen)
    
    start = time.time()
    
    data = pd.read_csv(inPath, delimiter=',', header=None)
    #pvKfoldValidation(data,kfold,w)
    pvKfoldValidation_select(data,kfold,w,steplen)
    
    end = time.time()
    runtime = end - start
    msg = "PV Classification Tooks {time} seconds to complete"
    print(msg.format(time=runtime)) 
    