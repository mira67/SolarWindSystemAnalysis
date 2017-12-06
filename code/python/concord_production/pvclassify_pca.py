# -*- coding: utf-8 -*-

# PV Fault Classification using DTW and K-NN
# Author: Qi Liu
# Email: qliu.hit@gmail.com

"""
adding confusion matrix 
@author Yingying Zhao
@date: 5/4/2017
"""

from ts_classifier import ts_classifier
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from sklearn.naive_bayes import GaussianNB, MultinomialNB #Bayes
from sklearn.mixture import GMM #GMM

#pca
from sklearn.decomposition import PCA
from sklearn import neighbors
import time
from sklearn import svm

# global settings
kfold = 2  # cross validation
inPath = 'sortedADIbyType.csv'
outPath = 'allADIReport_SVM_pca.csv'
w = 4

# KNN class
knn = ts_classifier()

# pca
def pca(X):
    pass
    #pca = PCA(n_components=36) # n_components为要降维到的维度，
    # pca = PCA(n_components='mle') # MLE算法自己选择降维维度
    pca = PCA(n_components=520) #根据mle自动先择的520维
    pca.fit(X)
    #print pca.explained_variance_ratio_
    #print pca.explained_variance_
    return pca.transform(X)

# dataset partition to train and test
def pvKfoldValidation(data, kfold, w):
    skf = StratifiedKFold(n_splits=kfold, shuffle=True, random_state=1)
    nCols = data.shape[1]
    # extract attributes and class target
    X = data.iloc[:, 1:nCols - 1].as_matrix()

    # pca
    X_pca = pca(X)

    print 'X len: ' + str(len(X[0]))
    print 'X len pca: ' + str(len(X_pca[0]))
    print X
    print X_pca

    y = data.iloc[:, -1].as_matrix()
    # encode string labels to numeric labels
    le = preprocessing.LabelEncoder()
    le.fit(y)
    Y = le.transform(y)
    # report file
    rpt = open(outPath, "a+")
    # cross validation
    for train, test in skf.split(X_pca, Y):
        trainX = X[train, :]
        testX = X[test, :]
        trainY = Y[train].reshape((len(train), 1))
        testY = Y[test].reshape((len(test), 1))
        train = np.append(trainX, trainY, axis=1)
        test = np.append(testX, testY, axis=1)  ########################


        # select different classifier
        # report = pvKNN(train,test,w) #select KNN
        report = pvBayes(train, test)  # select Bayes
        # report = pvGMM(train, test) #select GMM
        # report = pvHMM(train, test) #select HMM

        rpt.write(report)
        # classifaction_report_csv(report)
    # close report file
    rpt.close()
    return 'ok'


def pvKfoldValidation1(data,kfold,w):
    skf = StratifiedKFold(n_splits=kfold)
    nCols = data.shape[1]
    #extract attributes and class target
    X = data.iloc[:,1:nCols-1].as_matrix()

    # pca
    X_pca = pca(X)

    y = data.iloc[:,-1].as_matrix()
    #encode string labels to numeric labels
    le = preprocessing.LabelEncoder()
    le.fit(y)
    Y = le.transform(y)
    #report file
    rpt = open(outPath, "a+")
    #cross validation
    for train_index, test_index in skf.split(X_pca,Y):
        trainX = X[train_index,:]
        testX = X[test_index,:]
        trainY = Y[train_index].reshape((len(train_index),1))
        testY = Y[test_index].reshape((len(test_index),1))
#        train = np.append(trainX, trainY, axis=1)
#        test = np.append(testX, testY, axis=1)
        report = SVM(trainX,testX,trainY,testY)
        rpt.write(report)
#        report = pvKNN(train,test,w)
#        rpt.write(report)
        #classifaction_report_csv(report)
    #close report file
    rpt.close()
    return 'ok'


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

# classification
def pvKNN(train, test, w):
    preds = []
    for ind, i in enumerate(test):
        min_dist = float('inf')
        closest_seq = []
        # print ind
        for j in train:
            if knn.LB_Keogh(i[:-1], j[:-1], 5) < min_dist:
                dist = knn.DTWDistance(i[:-1], j[:-1], w)
                if dist < min_dist:
                    min_dist = dist
                    closest_seq = j
        preds.append(closest_seq[-1])
    conMar = confusion_matrix(test[:, -1], preds)
    print(conMar)
    return classification_report(test[:, -1], preds)

#Bayes
def pvBayes(train, test):
    pass
    # print('train: ', train)
    # print('test: ', test)
    clf = GaussianNB()
    clf = MultinomialNB(alpha=1.5, fit_prior=False)
    # fitting data
    X = train[:, 0:-1]
    Y = train[:, -1]
    # print 'X: ' + str(X)
    # print 'Y: ' + str(Y)
    clf.fit(X, Y)
    preds = []
    for ind, i in enumerate(test):
        pred = clf.predict([i[0:-1]])
        preds.append(pred[0])
    #print 'preds: ' + str(preds)

    conMar = confusion_matrix(test[:, -1], preds)
    print(conMar)

    target_names = ['class 0', 'class 1', 'class 2', 'class 3', 'class 4']
    return classification_report(test[:, -1], preds, target_names=target_names)

#GMM
def pvGMM(train, test):
    pass

    X = train[:, 0:-1]
    Y = train[:, -1]
    # print 'X: ' + str(X)
    # print 'Y: ' + str(Y)
    clf = GMM(n_components=5).fit(X)
    clf.fit(X, Y)
    preds = []
    for ind, i in enumerate(test):
        pred = clf.predict([i[0:-1]])
        preds.append(pred[0])
    #print 'preds: ' + str(preds)
    conMar = confusion_matrix(test[:, -1], preds)
    print(conMar)
    target_names = ['class 0', 'class 1', 'class 2', 'class 3', 'class 4']
    return classification_report(test[:, -1], preds, target_names=target_names)

# record results to file
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
    dataframe.to_csv(outPath, index=False)


if __name__ == '__main__':
    # profiling
    start = time.time()

    data = pd.read_csv(inPath, delimiter=',', header=None)
    pvKfoldValidation1(data, kfold, w)

    end = time.time()
    runtime = end - start
    msg = "PV Classification Tooks {time} seconds to complete"
    print(msg.format(time=runtime))