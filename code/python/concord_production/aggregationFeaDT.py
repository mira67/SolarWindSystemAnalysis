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
from xgboost.sklearn import XGBClassifier
from matplotlib import pyplot
import time
#import pv_ensemble_classify 



AnomalyTypeNum = 5
FaultNum = 1034
kfold = 4 # cross validation
#inPath = '/Users/zhaoyingying/PVData/ADIbyCen/ADIALLTimeSeriesAmptitude.csv'
inPath = '/Users/zhaoyingying/PVData/ADIbyCen/ADIALLTimeSeriesrenameType_rawsignal.csv'
aggFeaPath='/Users/zhaoyingying/PVData/ADIbyCen/agg_features.csv'
outPath = '/Users/zhaoyingying/PVData/ADIbyCen/classification_report_agg.csv'
totalreportPath= '/Users/zhaoyingying/PVData/ADIbyCen/classification_total_agg.csv'
FIPath= '/Users/zhaoyingying/PVData/ADIbyCen/Agg_Fea_importance.csv'
def AggregationFeatures():
    newColumns = ['mean','median','std','amp','Type']
    df = pd.read_csv(inPath, header = None)
    agg_df = pd.DataFrame(columns = newColumns)
    agg_df.loc[:, 'mean'] = df.iloc[:, 1:-1].mean(axis=1)
    agg_df.loc[:, 'median'] = df.iloc[:, 1:-1].median(axis=1)
    agg_df.loc[:, 'std'] = df.iloc[:, 1:-1].std(axis=1)
    agg_df.loc[:, 'amp'] = df.iloc[:, 1:-1].max(axis=1)
    agg_df.loc[:, 'Type'] = df.iloc[:, -1]
    agg_df.to_csv(aggFeaPath)

        
    

def pvKNN(trainX,testX,trainY,testY,k):
    knn = neighbors.KNeighborsClassifier(n_neighbors=k) 
    knn.fit(trainX, trainY)
    preds = knn.predict(testX)
    conMar = confusion_matrix(testY,preds)
   # print(conMar)
    return classification_report(testY,preds) 

def pvDecisionTree(trainX,testX,trainY,testY):
    tr = tree.DecisionTreeClassifier() 
    tr.fit(trainX, trainY)
    preds = tr.predict(testX)
    conMar = confusion_matrix(testY,preds)
    #print(conMar)
    return classification_report(testY,preds) 

def pvSVM(trainX,testX,trainY,testY):
    svc = svm.SVC() 
    svc.fit(trainX, trainY)
    preds = svc.predict(testX)
    conMar = confusion_matrix(testY,preds)
    #print(conMar)
    return classification_report(testY,preds)   

def pvKMEANS(trainX,testX,trainY,testY):
    kmeans = KMeans(n_clusters=AnomalyTypeNum,random_state=0).fit(trainX, trainY)
    preds = kmeans.predict(testX)
    conMar = confusion_matrix(testY,preds)
   # print(conMar)
    return classification_report(testY,preds)  
#Bayes
def pvBayes(trainX,testX,trainY,testY):
    pass
    train = np.append(trainX, trainY, axis=1)
    test = np.append(testX, testY, axis=1)
    clf = GaussianNB()
    clf = MultinomialNB(alpha=1.5, fit_prior=False)
    # fitting data
    X = train[:, 0:-1]
    Y = train[:, -1]
    clf.fit(X, Y)
    preds = []
    for ind, i in enumerate(test):
        pred = clf.predict([i[0:-1]])
        preds.append(pred[0])
    #print 'preds: ' + str(preds)

    conMar = confusion_matrix(test[:, -1], preds)
   # print(conMar)

    target_names = ['class 0', 'class 1', 'class 2', 'class 3', 'class 4']
    return classification_report(test[:, -1], preds, target_names=target_names)

#GMM
def pvGMM(trainX,testX,trainY,testY):
    train = np.append(trainX, trainY, axis=1)
    test = np.append(testX, testY, axis=1)
    X = train[:, 0:-1]
    Y = train[:, -1]
    clf = GaussianMixture(n_components=5,covariance_type='full')
    clf.fit(X, Y)
    preds = []
    for ind, i in enumerate(test):
        pred = clf.predict([i[0:-1]])
        preds.append(pred[0])
    conMar = confusion_matrix(test[:, -1], preds)
   # print(conMar)
    target_names = ['class 0', 'class 1', 'class 2', 'class 3', 'class 4']
    return classification_report(test[:, -1], preds, target_names=target_names)

def pvRandomForest(trainX,testX,trainY,testY):
    train = np.append(trainX, trainY, axis=1)
    #test = np.append(testX, testY, axis=1)
    X = train[:, 0:-1]
    Y = train[:, -1]
    clf = RandomForestClassifier(n_estimators=100)
    clf = clf.fit(X, Y)
    preds = clf.predict(testX)
    conMar = confusion_matrix(testY,preds)
   # print(conMar)
    return classification_report(testY,preds)  
 
def pvExtraTreesClassifier(trainX,testX,trainY,testY):
    train = np.append(trainX, trainY, axis=1)
    #test = np.append(testX, testY, axis=1)
    X = train[:, 0:-1]
    Y = train[:, -1]
    clf = ExtraTreesClassifier(n_estimators=100)
    clf = clf.fit(X, Y)
    preds = clf.predict(testX)
    conMar = confusion_matrix(testY,preds)
    #print(conMar)
    return classification_report(testY,preds)  

def pvAdaBoosting(trainX,testX,trainY,testY):
    train = np.append(trainX, trainY, axis=1)
    #test = np.append(testX, testY, axis=1)
    X = train[:, 0:-1]
    Y = train[:, -1]
    clf = AdaBoostClassifier(n_estimators=100)
    clf = clf.fit(X, Y)
    preds = clf.predict(testX)
    conMar = confusion_matrix(testY,preds)
   # print(conMar)
    return classification_report(testY,preds)

def pvGBDT(trainX,testX,trainY,testY):
    train = np.append(trainX, trainY, axis=1)
    #test = np.append(testX, testY, axis=1)
    X = train[:, 0:-1]
    Y = train[:, -1]
    clf = GradientBoostingClassifier(n_estimators=100,max_depth=5)
    clf = clf.fit(X, Y)
    preds = clf.predict(testX)
    conMar = confusion_matrix(testY,preds)
    #print(conMar)
    return classification_report(testY,preds)

def pvXBOOST(trainX,testX,trainY,testY):
    train = np.append(trainX, trainY, axis=1)
    # test = np.append(testX, testY, axis=1)
    X = train[:, 0:-1]
    Y = train[:, -1]

    # sklearn接口
    clf = XGBClassifier(
        n_estimators=100,  # trees number
        learning_rate=0.2,
        max_depth=3,
        min_child_weight=1,
        gamma=0.3,
        subsample=0.8,
        colsample_bytree=0.8,
        objective='binary:logistic',
        nthread=12,
        scale_pos_weight=1,
        reg_lambda=1,
        seed=27)

    model_sklearn = clf.fit(X, Y)
    preds = clf.predict(testX)
    conMar = confusion_matrix(testY, preds)
     # feature importance
    print(clf.feature_importances_)
    # plot
    pyplot.bar(range(len(clf.feature_importances_)), clf.feature_importances_)
    pyplot.show()
    FeatureImportance(clf.feature_importances_)
    print(conMar)
    return classification_report(testY, preds)
def FeatureImportance(FI):
    fi = open(FIPath, "a+") 
    line = ''
    for idx, item in enumerate(FI):
        line = line+str(item)+','
    fi.write(line+'\n')
    print('sucessfully write feature importance index')
    
    
def pvBagging(trainX,testX,trainY,testY):
    train = np.append(trainX, trainY, axis=1)
    #test = np.append(testX, testY, axis=1)
    X = train[:, 0:-1]
    Y = train[:, -1]
    clf = BaggingClassifier(n_estimators=100)
    clf = clf.fit(X, Y)
    preds = clf.predict(testX)
    conMar = confusion_matrix(testY,preds)
    #print(conMar)
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
        rpt.writelines('\n*********the SVM report************\n')
        start = time.time()
        report = pvSVM(trainX,testX,trainY,testY)
        end = time.time()
        runtime = end - start
        msg = "PV SVM Classification Tooks {time} seconds to complete"
        print(msg.format(time=runtime)) 
        rpt.write(report)
        rpt.writelines('\n*********the KMeans report************\n')
        start = time.time()
        report = pvKMEANS(trainX,testX,trainY,testY)
        end = time.time()
        runtime = end - start
        msg = "PV KMeans Classification Tooks {time} seconds to complete"
        print(msg.format(time=runtime)) 
        rpt.write(report)
        rpt.writelines('\n*********the DecisionTree report************\n')
        start = time.time()
        report = pvDecisionTree(trainX,testX,trainY,testY)
        end = time.time()
        runtime = end - start
        msg = "PV DecisionTree Classification Tooks {time} seconds to complete"
        print(msg.format(time=runtime)) 
        rpt.write(report)
        rpt.writelines('\n*********the KNN(K=1) report************\n')
        start = time.time()
        report = pvKNN(trainX,testX,trainY,testY, 1)
        end = time.time()
        runtime = end - start
        msg = "PV KNN(K=1) Classification Tooks {time} seconds to complete"
        print(msg.format(time=runtime)) 
        rpt.write(report)
        rpt.writelines('\n*********the KNN(K=3) report************\n')
        start = time.time()
        report = pvKNN(trainX,testX,trainY,testY,3)
        end = time.time()
        runtime = end - start
        msg = "PV KNN(K=3) Classification Tooks {time} seconds to complete"
        print(msg.format(time=runtime)) 
        rpt.write(report)
        rpt.writelines('\n*********the KNN(K=5) report************\n')
        start = time.time()
        report = pvKNN(trainX,testX,trainY,testY,5) 
        end = time.time()
        runtime = end - start
        msg = "PV KNN(K=5) Classification Tooks {time} seconds to complete"
        print(msg.format(time=runtime)) 
        rpt.write(report)
#        rpt.writelines('\n*********the Bayes report************\n')
#        start = time.time()
#        report = pvBayes(trainX,testX,trainY,testY)
#        end = time.time()
#        runtime = end - start
#        msg = "PV Bayes Classification Tooks {time} seconds to complete"
#        print(msg.format(time=runtime)) 
#        rpt.write(report)
        rpt.writelines('\n*********the RandomForest report************\n') 
        start = time.time()
        report = pvRandomForest(trainX,testX,trainY,testY)
        end = time.time()
        runtime = end - start
        msg = "PV RandomForest Classification Tooks {time} seconds to complete"
        print(msg.format(time=runtime)) 
        rpt.write(report)
        rpt.writelines('\n*********the ExtraTrees report************\n')
        start = time.time()
        report = pvExtraTreesClassifier(trainX,testX,trainY,testY)
        end = time.time()
        runtime = end - start
        msg = "PV ExtraTrees Classification Tooks {time} seconds to complete"
        print(msg.format(time=runtime)) 
        rpt.write(report)                
        rpt.writelines('\n*********the GradientBoosting report************\n')
        start = time.time()
        report = pvGBDT(trainX,testX,trainY,testY)
        end = time.time()
        runtime = end - start
        msg = "PV GradientBoosting Classification Tooks {time} seconds to complete"
        print(msg.format(time=runtime))         
        rpt.write(report)
        rpt.writelines('\n*********the XGBoosting report************\n')
        start = time.time()
        report = pvXBOOST(trainX, testX, trainY, testY)
        end = time.time()
        runtime = end - start
        msg = "PV XGBoosting Classification Tooks {time} seconds to complete"
        print(msg.format(time=runtime)) 
        rpt.write(report)
        rpt.writelines('\n*********the Bagging report************\n')
        start = time.time()
        report = pvBagging(trainX, testX, trainY, testY)
        end = time.time()
        runtime = end - start
        msg = "PV Bagging Classification Tooks {time} seconds to complete"
        print(msg.format(time=runtime)) 
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
    #AggregationFeatures()  
    data = pd.read_csv(aggFeaPath, delimiter=',')
    pvKfoldValidation(data,kfold)
    total_report()

    
    