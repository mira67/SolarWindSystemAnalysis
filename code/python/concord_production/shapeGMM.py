#PV Fault Classification using GMM 
#Author: Yingying Zhao
#Email: qliu.hit@gmail.com


import numpy as np
import pandas as pd 
from sklearn import preprocessing
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.mixture import GaussianMixture
from pvalgs import fdGMM
import time
from pvKmeans import getTrueLable

#global settings
kfold = 2 # cross validation

inPath = '/Users/zhaoyingying/PVData/ADIbyCen/DisWithStd.csv'
groundTruthPath = '/Users/zhaoyingying/PVData/ADIbyCen/ADIALLTimeSeriesAmptitude.csv'
outPath = '/Users/zhaoyingying/PVData/ADIbyCen/shapeDistGMM_report.csv'

w = 4
AnomalyTypeNum = 5
#FaultNum = 1044
#removing some soiling labeling on rainny day
FaultNum = 1034
#KNN class


def pvGMM(train,test):
    X = train[:,:-1]
    print(X)
    Y = train[:, -1]
    clf = GaussianMixture(n_components=5,covariance_type='full').fit(X)
    clf.fit(X, Y)
    print('start to predict...')
    preds = []
    for ind, i in enumerate(test):
        pred = clf.predict([i[0:-1]])
        print(pred)
        preds.append(pred[0])
    print ('preds: ' + str(preds))
    conMar = confusion_matrix(test[:, -1], preds)
    print(conMar)
    target_names = ['class 0', 'class 1', 'class 2', 'class 3', 'class 4']
    return classification_report(test[:, -1], preds, target_names=target_names)


def pvKfoldValidation(data, kfold):
    skf = StratifiedKFold(n_splits=kfold, shuffle=True, random_state=1)
    #nCols = data.shape[1]
    # extract attributes and class target
    X = data.iloc[:, 3:].as_matrix()
    
    y = data.iloc[:, -2].as_matrix()
    # encode string labels to numeric labels
    le = preprocessing.LabelEncoder()
    le.fit(y)
    Y = le.transform(y)
    # report file
    rpt = open(outPath, "a+")
    # cross validation
    for train, test in skf.split(X, Y):
        trainX = X[train, :]
        testX = X[test, :]
        trainY = Y[train].reshape((len(train), 1))
        testY = Y[test].reshape((len(test), 1))
        train = np.append(trainX, trainY, axis=1)
        test = np.append(testX, testY, axis=1)
        report = pvGMM(train, test) #select GMM
        rpt.write(report)

    rpt.close()
    return 'ok' 

def adaptiveGMM():
    preds=[]
    shape = np.zeros((FaultNum,1))
    tmp = pd.read_csv(inPath).loc[:,'dist']
    for i in range(FaultNum): 
        shape[i] = tmp.iloc[i]  
    #the max gmm cluster
    kLen = 5
    preds,centroids,ck = fdGMM(shape,kLen)
    
    preds.astype(int)
    np.savetxt('/Users/zhaoyingying/PVData/ADIbyCen/tmp.csv',preds)
    print(preds)
    newpreds = []
    for i in range(FaultNum):
        if preds[i] == 0:
            newpreds.append('type1')
        if preds[i] == 2:
            newpreds.append('type2')
        if preds[i] == 1:
            newpreds.append('type3')
        if preds[i] == 3:
            newpreds.append('type4')
        if preds[i] == 4:
            newpreds.append('type5')
    print(newpreds)

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
        
    data = pd.read_csv(inPath, delimiter=',')
    #pvKfoldValidation(data,kfold)
    adaptiveGMM()
    end = time.time()
    runtime = end - start
    msg = "PV Classification Tooks {time} seconds to complete"
    print(msg.format(time=runtime)) 
    