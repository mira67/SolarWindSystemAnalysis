#PV Classification - A full pipeline, data query to preprocessing, modeling 
# A multi-functional code: extract linear slope for strings by windows
# Record to file
# Query data to file
# Code is modular and can be extended
#Author: Qi Liu
#Email: qi.liu@colorado.edu

import pymysql.cursors
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import time
import math
import multiprocessing as mp
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import statsmodels.api as sm

#Parameters configuration
startDT = '2016-04-15'
endDT = '2016-08-15'

timeRg = ['06:00','18:00'];#use pandas to get data within this range

gtFile = 'E:/myprojects/pv_detection/data/classification_0929/labeldata/groundTruthPV.csv'
cbPath = 'E:/myprojects/pv_detection/data/classification_0929/cb_raw_data_with_env/'
strPath = 'E:/myprojects/pv_detection/data/classification_0929/pre_processed_with_label/'
feaPath = 'E:/myprojects/pv_detection/data/classification_0929/classification_features/'

"""
Step 1: Extract data from database, table-hlx
Input: String Info: hlxID, strID, Datetime: startDT,endDT
Output: String current
"""
def queryCBData(hlxID, startDT,endDT):
    # AND TIME(data_date) BETWEEN '08:00'AND '17:00'
    # AND TIME(data_date) BETWEEN '08:00'AND '17:00'
    sql1 = """SELECT * FROM pingyuan2.hlx WHERE combinerbox = '{}' 
            AND data_date BETWEEN '{}' AND '{}';"""
    sqlSts1 = sql1.format(hlxID, startDT,endDT)
    
    sql2 = """SELECT data_date,FS1,Fs2,Fs1m,Fs2m,Sd,T0 FROM pingyuan2.qxz WHERE data_date BETWEEN '{}' AND '{}';"""
    sqlSts2 = sql2.format(startDT,endDT)
    
    #Make database connetion
    db = pymysql.connect(host='localhost',
                                user='liuqi',
                                password='1234',
                                db='pingyuan2',
                                port=3306,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor,local_infile=True)

    try:
        '''grab current data'''
        cursor = db.cursor()
        cursor.execute(sqlSts1)
        db.commit()
        #collect query data
        strCurrent = pd.DataFrame(cursor.fetchall())
        
        '''grab environmental data'''
        cursor.execute(sqlSts2)
        db.commit()
        #collect query data
        features = pd.DataFrame(cursor.fetchall())
        
        #join table to avoid missing data problem
        cbData = strCurrent.join(features.set_index('data_date'),on='data_date')
        
    except:
        # Rollback in case there is any error
        db.rollback()
        print('Not able to query combinerbox %s' % (hlxID))
        
    #close connection
    #cursor.close()
    db.close()
    return cbData

"""Query Weather Data"""
def queryWTData(startDT,endDT):
    sql = """SELECT data_date,FS1,Fs2,Fs1m,Fs2m,Sd,T0 FROM pingyuan2.qxz WHERE data_date BETWEEN '{}' AND '{}';"""
    sqlSts = sql.format(startDT,endDT)
    
    #Make database connetion
    db = pymysql.connect(host='localhost',
                                user='liuqi',
                                password='1234',
                                db='pingyuan2',
                                port=3306,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor,local_infile=True)

    try:
        cursor = db.cursor()
        '''grab environmental data'''
        cursor.execute(sqlSts)
        db.commit()
        #collect query data
        features = pd.DataFrame(cursor.fetchall())
    except:
        # Rollback in case there is any error
        db.rollback()
        print('Not able to query weather data')
        
    #close connection
    #cursor.close()
    db.close()
    return features

#Identify Normal Data Clusters
def dataPartition(currents,features):
    bucketLen = 850 #how to determine the optimal bucketlength
    data_len = currents.size
    bucket_num = math.floor(data_len/bucketLen)
    
    print('BucketNumber: ', bucket_num, data_len)
    
    #Pre-linear regression for computing slopes, rough model with single feature
    slopes = np.zeros((bucket_num,1))
    
    for i in range(0,bucket_num):
        x = features[i*bucketLen:(i+1)*bucketLen,3]#Fs2m
        y = currents[i*bucketLen:(i+1)*bucketLen]
        x = sm.add_constant(x)
        
        lm = strPowerModel(x,y)
        
        slopes[i] = lm.coef_[1]#extract slopes
    
    #remove outliers and make slopes into clusters
    N = 2 #either normal or not 
    
    km = KMeans(n_clusters=N, random_state=0).fit(slopes)
    
    clusters,centroids = km.labels_, km.cluster_centers_
    
    #print('Clusters: ',clusters, centroids)
    
    #pick higher mean clusters and obtain bucket IDX
    maxId = np.argmax(centroids)    
    norm_idx = np.where(clusters==maxId)
    norm_idx = norm_idx[0]#get out of tuple
    norm_bucketLen = norm_idx.size
    #print('norm_idx: ',norm_idx,norm_bucketLen)
    
    #construc normal data for modeling
    ndata_idx = []
    for i in range(0,norm_bucketLen):
        k = norm_idx[i]
        rng = np.linspace(k*bucketLen,(k+1)*bucketLen,bucketLen, endpoint=False, dtype=np.int16)
        ndata_idx.extend(rng.tolist())
        
    #partitioned normal data 
    #print('features: ', features.shape)
    x = features[ndata_idx,:]
    y = currents[ndata_idx]
    
    print('Data Partition - DONE')
    return x, y, centroids[maxId], centroids 


#Build model for individual string
def strPowerModel(Features,stringCurrent):
    #Build libear model
    lm = LinearRegression()
    lm.fit(Features,stringCurrent)    
    return lm

"""Grab Slope Data"""
def grabSlopeData(currents,features):
    bucketLen = 800 #how to determine the optimal bucketlength
    data_len = currents.size
    bucket_num = math.floor(data_len/bucketLen)
    
    print('BucketNumber: ', bucket_num, data_len)
    
    #Pre-linear regression for computing slopes, rough model with single feature
    slopes = np.zeros((bucket_num,1))
    
    for i in range(0,bucket_num):
        x = features[i*bucketLen:(i+1)*bucketLen,3]#Fs2m
        y = currents[i*bucketLen:(i+1)*bucketLen]
        x = sm.add_constant(x)
        
        lm = strPowerModel(x,y)
        
        slopes[i] = lm.coef_[1]#extract slopes
    return slopes


"""Normal Data Modeling"""
def modelStrData(strFile):
    df = pd.read_csv(strFile)
    df = df.dropna(axis=0, how='any')
    smLen = 60
    df = pd.rolling_mean(df, smLen)
    df_dup = df.iloc[smLen:,:]
    colName = df.columns.values
    strName = colName[1:57]
    
    for idx, strName in enumerate(strName):
        current = df[strName].as_matrix()
        current = current[smLen:]
        features = df.iloc[smLen:,57:63].as_matrix()#all features
        
        nfea, ncurrent, slope, centroids = dataPartition(current,features)
        lm = strPowerModel(nfea,ncurrent)
        print('Normal Model Variance score: %.4f' % lm.score(nfea, ncurrent))
        #estimated current
        predCurrent = lm.predict(features)
        print('All Data Model Variance score: %.4f' % lm.score(features, current))
        
        strName = strName + '_model'
        #predCurrent = pd.DataFrame(predCurrent.reshape(-1),columns=strName)
        df_dup[strName] = predCurrent.tolist()
    
    #obtain estimated data and record to file
    filename = strPath + 'labeledStrData_with_env_model.csv'
    df_dup.to_csv(filename, sep=',',header=True)
    
    return "Hello"

"""Group all labelled data in one file"""
def grabStrData(hlxID, strID, cbFile):
    cbData = pd.read_csv(cbFile)
    strData = pd.DataFrame()
    strData['data_date'] = cbData['data_date']
    strID = 'I'+str(strID)
    strName = hlxID+'_'+strID
    strData[strName] = cbData[strID]
    return strData

"""Record raw 1min cb data with environmental features in a file by CB"""
def writeCBDataToFile():
    gtData = pd.read_csv(gtFile)
    cbList = gtData['CombinerBoxID'].unique()
    print(cbList.shape[0])
    cbNum = cbList.shape[0]
    
    #profiling
    start = time.time()
    for idx, cb in enumerate(cbList):
    #cb = 'S35-NBA-HL08'
        hlxID = cb
        data = queryCBData(hlxID,startDT,endDT)
        filename = cbPath + cb + '.csv'
        writeCBDataToFile(data, filename)
    
    end = time.time()
    runtime = end - start
    msg = "CB Data Writing Process Took {time} seconds to complete"
    print(msg.format(time=runtime))
    
    data.to_csv(filename, sep=',',header=True)
    return 'Great!'

"""Record labled string data in a single file with enviromental data"""
def writeStrDataToFile():
    
    gtData = pd.read_csv(gtFile)
    strList = pd.DataFrame()
    strList['hlxID'] = gtData['CombinerBoxID']
    strList['strID'] = gtData['StringID']
    strList = strList.drop_duplicates()
    print(strList.head())
    
    allStrData = pd.DataFrame()
    
    for idx, rows in strList.iterrows():
    #cb = 'S35-NBA-HL08'
        hlxID = rows['hlxID']
        strID = rows['strID']
        cbFile = cbPath + hlxID + '.csv'
        print(cbFile)
        strData = grabStrData(hlxID, strID, cbFile)    
        
        if idx == 0:
            allStrData['data_date'] = strData['data_date']
            strName = hlxID+'_I'+str(strID)
            allStrData[strName] = strData[strName]
            
        else:
            #join table to avoid missing data problem
            allStrData = allStrData.join(strData.set_index('data_date'),on='data_date')
    
    #grab env data as the last column
    #features = queryWTData(startDT,endDT)
    
    #allStrData = allStrData.join(features.set_index('data_date'),on='data_date')
    
    #record data to file
    filename = strPath + 'labeledStrData.csv'
    allStrData.to_csv(filename, sep=',',header=True)
    
    return "Saturday"
    
"""Main Function""" 
def main():
    #profiling
    start = time.time()
    
    strFile = strPath + 'labeledStrData_with_env.csv'
    
    #
    df = pd.read_csv(strFile)
    df = df.dropna(axis=0, how='any')
    smLen = 60
    df = pd.rolling_mean(df, smLen)
    df_dup = df.iloc[smLen:,:]
    colName = df.columns.values
    strName = colName[1:57]
    
    all_slopes = pd.DataFrame()
    
    for idx, strName in enumerate(strName):
        current = df[strName].as_matrix()
        current = current[smLen:]
        features = df.iloc[smLen:,57:63].as_matrix()#all features
        
        slopes = grabSlopeData(current,features)
        all_slopes[strName] = pd.DataFrame(data=slopes, columns=[strName])
        print(strName)
    #obtain estimated data and record to file
    filename = feaPath + 'slope_features_1003.csv'
    all_slopes.to_csv(filename, sep=',',header=True)
    
    end = time.time()
    runtime = end - start
    msg = "Str Data Writing Process Took {time} seconds to complete"
    print(msg.format(time=runtime))
    
    return "Wao!"   
    
"""Execute Main"""   
if __name__ == "__main__":
    main()   
    
    
"""
ds = pd.read_csv('E:/myprojects/pv_detection/data/classification_0929/pre_processed_with_label/labeledStrData_no_env.csv')
df = pd.read_csv('E:/myprojects/pv_detection/data/classification_0929/pre_processed_with_label/env_data.csv')
allStrData = ds.join(df.set_index('data_date'),on='data_date') 
filename = strPath + 'labeledStrData_with_env.csv'
allStrData.to_csv(filename, sep=',',header=True) 
"""
    