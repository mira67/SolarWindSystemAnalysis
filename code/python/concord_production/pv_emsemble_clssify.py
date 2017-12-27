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
from matplotlib import pyplot
from xgboost.sklearn import XGBClassifier
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import csv
import time


AnomalyTypeNum = 5
FaultNum = 1034
kfold = 4 # cross validation

#agg+frq
#inPath = '/Users/zhaoyingying/PVData/ADIbyCen/temporal_frq_features/agg_frq_features.csv'
#outPath = '/Users/zhaoyingying/PVData/ADIbyCen/temporal_frq_features/confusionMatrix/report_agg_frq_tsne.csv'
#totalreportPath= '/Users/zhaoyingying/PVData/ADIbyCen/temporal_frq_features/confusionMatrix/total_report_agg_frq_tsne.csv'
#FIPath= '/Users/zhaoyingying/PVData/ADIbyCen/temporal_frq_features/confusionMatrix/FI_agg_frq_tsne.csv'
#conMarPath = '/Users/zhaoyingying/PVData/ADIbyCen/temporal_frq_features/confusionMatrix/conMar.csv'

#agg
#inPath = '/Users/zhaoyingying/PVData/ADIbyCen/temporal_frq_features/agg_features.csv'
#outPath = '/Users/zhaoyingying/PVData/ADIbyCen/temporal_frq_features/confusionMatrix/report_agg_tsne.csv'
#totalreportPath= '/Users/zhaoyingying/PVData/ADIbyCen/temporal_frq_features/confusionMatrix/total_report_agg_tsne.csv'
#FIPath= '/Users/zhaoyingying/PVData/ADIbyCen/temporal_frq_features/confusionMatrix/FI_agg.csv'
#conMarPath = '/Users/zhaoyingying/PVData/ADIbyCen/temporal_frq_features/confusionMatrix/conMar_agg.csv'
    #confusion matrix print
    
inPath = '/Users/zhaoyingying/PVData/ADIbyCen/similarity_features/similarity_features_scale/ADI.csv'
outPath = '/Users/zhaoyingying/PVData/ADIbyCen/similarity_features/similarity_features_scale/report_ADI_tsne.csv'
totalreportPath= '/Users/zhaoyingying/PVData/ADIbyCen/similarity_features/similarity_features_scale/total_report_ADI_tsne.csv'
FIPath= '/Users/zhaoyingying/PVData/ADIbyCen/similarity_features/similarity_features_scale/FI_ADI_tsne.csv'
conMarPath = '/Users/zhaoyingying/PVData/ADIbyCen/similarity_features/similarity_features_scale/conMar.csv'


cnm = open(conMarPath,"a+")

def pvKNN(trainX,testX,trainY,testY,k):
    knn = neighbors.KNeighborsClassifier(n_neighbors=k) 
    knn.fit(trainX, trainY)
    preds = knn.predict(testX)
    conMar = confusion_matrix(testY,preds)
    print(conMar)
    cnm.writelines('\n**knn-confusion martix, and k= '+ str(k)+'\n')
    cnm.write(np.array2string(conMar))
    return classification_report(testY,preds) 

def pvDecisionTree(trainX,testX,trainY,testY):
    tr = tree.DecisionTreeClassifier() 
    tr.fit(trainX, trainY)
    preds = tr.predict(testX)
    conMar = confusion_matrix(testY,preds)
    print(conMar)
    cnm.writelines('\n**DecisionTree-confusion martix\n')
    cnm.write(np.array2string(conMar))
    return classification_report(testY,preds) 

def pvSVM(trainX,testX,trainY,testY):
    svc = svm.SVC() 
    svc.fit(trainX, trainY)
    preds = svc.predict(testX)
    conMar = confusion_matrix(testY,preds)
    print(conMar)
    cnm.writelines('\n**SVM-confusion martix\n')
    print('sucessfully write')
    cnm.write(np.array2string(conMar))
    return classification_report(testY,preds)   

def pvKMEANS(trainX,testX,trainY,testY):
    kmeans = KMeans(n_clusters=AnomalyTypeNum,random_state=0).fit(trainX, trainY)
    preds = kmeans.predict(testX)
    conMar = confusion_matrix(testY,preds)
    print(conMar)
    cnm.writelines('\n**kMEANS-confusion martix\n')
    cnm.write(np.array2string(conMar))
    return classification_report(testY,preds) 
  
#Bayes
def pvBayes(trainX,testX,trainY,testY):
    print('starting bayes')
    pass
    train = np.append(trainX, trainY, axis=1)
    test = np.append(testX, testY, axis=1)
    clf = GaussianNB()
    clf = MultinomialNB(alpha=1.5, fit_prior=False)
    # fitting data
    X = train[:, 0:-1]
    print(X)
    Y = train[:, -1]
    clf.fit(X, Y)
    preds = []
    for ind, i in enumerate(test):
        pred = clf.predict([i[0:-1]])
        preds.append(pred[0])
    #print 'preds: ' + str(preds)

    conMar = confusion_matrix(test[:, -1], preds)
    print(conMar)
    cnm.writelines('\n**Bayes-confusion martix\n')
    cnm.write(np.array2string(conMar))

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
    print(conMar)
    cnm.writelines('\n**pvGMM-confusion martix\n')
    cnm.write(np.array2string(conMar))
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
    print(conMar)
    cnm.writelines('\n**RF-confusion martix\n')
    cnm.write(np.array2string(conMar))
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
    print(conMar)
    cnm.writelines('\n**ET-confusion martix\n')
    cnm.write(np.array2string(conMar))
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
    print(conMar)
    cnm.writelines('\n**AdaBoosting-confusion martix\n')
    cnm.write(np.array2string(conMar))
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
    print(conMar)
    cnm.writelines('\n**pvGBDT-confusion martix\n')
    cnm.write(np.array2string(conMar))
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
    cnm.writelines('\n**XGBoosting-confusion martix\n')
    cnm.write(np.array2string(conMar))
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
    print(conMar)
    cnm.writelines('\n**Bagging-confusion martix\n')
    cnm.write(np.array2string(conMar))
    return classification_report(testY,preds)

def pca(X):
    pass
    #pca = PCA(n_components='mle',svd_solver='full') # MLE算法自己选择降维维度
    
    pca = PCA(n_components=3)
    
    pca.fit(X)
    print('starting pca...')
    print (pca.explained_variance_)
    print(pca.explained_variance_ratio_)
    return pca.transform(X)

def tsne(X):
    pass
    t_sne = TSNE(n_components=3).fit_transform(X)
#    df_tsne = pd.DataFrame()
#        #get type col
#    TypePath= '/Users/zhaoyingying/PVData/ADIbyCen/agg_features.csv'
#    type_df = pd.read_csv(TypePath).loc[:,'Type']
#    #adding type colum
#    df_tsne['Type']=type_df.as_matrix()
#    
#
#    df_tsne['x-tsne'] = t_sne[:,0]
#    df_tsne['y-tsne'] = t_sne[:,1]
#    df_tsne.to_csv(tsnePath)
#    
#    df_tsne_t1 =df_tsne.iloc[0:475,1:3].copy()
#    df_tsne_t2 =df_tsne.iloc[475:704,1:3].copy()
#    
#    df_tsne_t2.index = range(len(df_tsne_t2))
#    
#    df_tsne_t3 =df_tsne.iloc[704:900,1:3].copy()
#    df_tsne_t3.index = range(len(df_tsne_t3))
#    df_tsne_t4 =df_tsne.iloc[904:,1:3].copy()
#    df_tsne_t4.index = range(len(df_tsne_t4))
#    df_tsne_t5 =df_tsne.iloc[900:904,1:3].copy()
#    df_tsne_t5.index = range(len(df_tsne_t5))
#    res = pd.concat([df_tsne_t1, df_tsne_t2, df_tsne_t3,df_tsne_t4,df_tsne_t5],axis=1)
#    res.to_csv(tsnePlotPath)
    return t_sne
 
#dataset partition to train and test
def pvKfoldValidation(data,kfold):
    skf = StratifiedKFold(n_splits=kfold,random_state=None, shuffle=False)
    nCols = data.shape[1]
    #extract attributes and class target
    X = data.iloc[:,1:nCols-1].as_matrix()
        # tsne
    #X_tsne = tsne(X)
    #pca
    #pca = PCA(X)

   
    
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
#        rpt.writelines('\n*********the KMeans report************\n')
#        start = time.time()
#        report = pvKMEANS(trainX,testX,trainY,testY)
#        end = time.time()
#        runtime = end - start
#        msg = "PV KMeans Classification Tooks {time} seconds to complete"
#        print(msg.format(time=runtime)) 
#        rpt.write(report)
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
#        rpt.writelines('\n*********the GMM report************\n')
#        start = time.time()
#        report = pvGMM(trainX,testX,trainY,testY)
#        end = time.time()
#        runtime = end - start
#        msg = "PV GMM Classification Tooks {time} seconds to complete"
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
        
    data = pd.read_csv(inPath, delimiter=',')
    pvKfoldValidation(data,kfold)
    total_report()

    
    