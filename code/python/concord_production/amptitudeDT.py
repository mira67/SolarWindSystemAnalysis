# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:58:02 2017

@author: xiaomei
"""

import numpy as np
import pandas as pd
from sklearn import svm 
from sklearn.metrics import classification_report,confusion_matrix
from sklearn import preprocessing
from sklearn.model_selection import StratifiedKFold
from sklearn import neighbors 
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
from sklearn import tree
from sklearn.naive_bayes import GaussianNB, MultinomialNB #Bayes
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
import csv



AnomalyTypeNum = 5
FaultNum = 1034
kfold = 4 # cross validation
inPath = '/Users/zhaoyingying/PVData/ADIbyCen/ADIALLTimeSeriesAmptitude.csv'
outPath = '/Users/zhaoyingying/PVData/ADIbyCen/classification_report_4fold_DT.csv'
totalreportPath= '/Users/zhaoyingying/PVData/ADIbyCen/classification_total_report_DT.csv'


def pvDecisionTree(trainX,testX,trainY,testY):
    tr = tree.DecisionTreeClassifier() 
    tr.fit(trainX, trainY)
    preds = tr.predict(testX)
    conMar = confusion_matrix(testY,preds)
    print(conMar)
    return classification_report(testY,preds) 


#dataset partition to train and test
def pvKfoldValidation(data,kfold):
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
    print('starting crossing validation....')
    #cross validation
    for train, test in skf.split(X, Y):
        trainX = X[train,:] 
        testX = X[test,:]
        trainY = Y[train].reshape((len(train),1))
        testY = Y[test].reshape((len(test),1))
        train = np.append(trainX, trainY, axis=1)
        test = np.append(testX, testY, axis=1)
        #choose classifiers

        rpt.writelines('\n*********the DecisionTree report************\n')
        report = pvDecisionTree(trainX,testX,trainY,testY)
        rpt.write(report)
        

    #close report file
    rpt.close()
    return 'ok'    
def total_report():
    precision=[]
    recall=[]
    f1=[]
    method=[]

    #get method and precision ,recall ,f1
    with open(outPath) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            if(len(row)>0):
                if '***' in row[0]:
                    method.append(row[0].split(' ')[1])
                if 'avg' in row[0]:
                    precision.append(float(row[0].split(' ')[9]))
                    recall.append(float(row[0].split(' ')[15]))
                    f1.append(float(row[0].split(' ')[21]))
    #total:
    results = pd.DataFrame()
    results['Method'] = pd.DataFrame(data=method, columns=['Method'])
    results['Precision'] = pd.DataFrame(data=precision, columns=['Precision'])
    results['Recall'] = pd.DataFrame(data=recall, columns=['Recall'])
    results['F1'] = pd.DataFrame(data=f1, columns=['F1'])
    
    #get average
    print(results.groupby('Method').mean())
    
    results.groupby('Method').mean().to_csv(totalreportPath)

                    
if __name__ == '__main__':
        
    data = pd.read_csv(inPath, delimiter=',')
    pvKfoldValidation(data,kfold)
    total_report()

    
    