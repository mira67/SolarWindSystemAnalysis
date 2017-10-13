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
import plotly.plotly as py
from sklearn.cluster import KMeans
import statsmodels.api as sm
import glob
import os

#Parameters configuration
startDT = '2016-01-01'
endDT = '2016-12-31'

timeRg = ['06:00','18:00'];#use pandas to get data within this range

gtFile = 'E:/myprojects/pv_detection/data/classification_0929/labeldata/groundTruthPV.csv'
cbPath = 'E:/myprojects/pv_detection/data/classification_0929/cb_raw_data_with_env/'
strPath = 'E:/myprojects/pv_detection/data/classification_0929/pre_processed_with_label/'
feaPath = 'E:/myprojects/pv_detection/data/classification_0929/classification_features/'
otherPath = 'E:/myprojects/pv_detection/data/classification_0929/otherTest/'

def queryAnyData(hlxID, startDT,endDT):
    # AND TIME(data_date) BETWEEN '08:00'AND '17:00'
    # AND TIME(data_date) BETWEEN '08:00'AND '17:00'
    sql1 = """SELECT * FROM pingyuan2.hlx WHERE combinerbox = '{}' 
            AND data_date BETWEEN '{}' AND '{}';"""
    sqlSts1 = sql1.format(hlxID, startDT,endDT)
    
    sql2 = """SELECT data_date,Fs2m FROM pingyuan2.qxz WHERE data_date BETWEEN '{}' AND '{}';"""
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
        
        cbData = strCurrent.join(features.set_index('data_date'),on='data_date')
        
    except:
        # Rollback in case there is any error
        db.rollback()
        print('Not able to query combinerbox %s' % (hlxID))
        
    #close connection
    #cursor.close()
    db.close()
    return cbData

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
    bucketLen = 720 #how to determine the optimal bucketlength
    data_len = currents.size
    bucket_num = math.floor(data_len/bucketLen)
    
    print('BucketNumber: ', bucket_num, data_len)
    
    #Pre-linear regression for computing slopes, rough model with single feature
    slopes = np.zeros((bucket_num,1))
    
    for i in range(0,bucket_num):
        x = features[i*bucketLen:(i+1)*bucketLen]#Fs2m,[,3]
        y = currents[i*bucketLen:(i+1)*bucketLen]
        x = sm.add_constant(x)
        
        lm = strPowerModel(x,y)
        
        if len(lm.coef_) > 1:
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
    
"""Main slopes Function""" 
def main_grabslopes():
    #profiling
    start = time.time()
    
    #strFile = strPath + 'labeledStrData_with_env.csv'
    strFile = strPath + 'S35-NBA-HL08_for_slope.csv'
    #
    df = pd.read_csv(strFile)
    df = df.dropna(axis=0, how='any')
    smLen = 60
    df = pd.rolling_mean(df, smLen)
    df_dup = df.iloc[smLen:,:]
    colName = df.columns.values
    strName = colName[1:17]
    
    all_slopes = pd.DataFrame()
    
    for idx, strName in enumerate(strName):
        current = df[strName].as_matrix()
        current = current[smLen:]
        features = df.iloc[smLen:,17:23].as_matrix()#all features
        
        slopes = grabSlopeData(current,features)
        all_slopes[strName] = pd.DataFrame(data=slopes, columns=[strName])
        print(strName)
    #obtain estimated data and record to file
    filename = feaPath + 'slope_features_1010_S35NBAHL08.csv'
    all_slopes.to_csv(filename, sep=',',header=True)
    
    end = time.time()
    runtime = end - start
    msg = "Str Data Writing Process Took {time} seconds to complete"
    print(msg.format(time=runtime))
    
    return "Wao!"   

def fftTrans(current,Fs, window_size):
    Fs = Fs;  # sampling rate
    Ts = 1.0/Fs; # sampling interval
    ws = window_size
    
    y = current
    lenN = len(y) # length of the signal
    
    ws_Y = np.empty(shape=None)
    
    for w_num in range(0, round(lenN/ws) - 1):
        y_w = y[w_num*ws:(w_num+1)*ws]
        n = len(y_w) # length of the signal
        k = np.arange(n)
        T = n/Fs
        frq = k/T # two sides frequency range
        frq = frq[range(round(n/2))] # one side frequency range
        
        #Y = np.fft.fft(y)/n # fft computing and normalization?
        Y = np.fft.fft(y_w) # fft computing and no normalization
        Y = Y[range(round(n/2))]
        Y = abs(Y)
        #expand numpy array
        if w_num == 0:
            ws_Y = Y
        else:
            ws_Y = np.append(ws_Y,Y)               
    
    '''
    fig, ax = plt.subplots(2, 1)
    ax[0].plot(y)
    ax[0].set_xlabel('Time')
    ax[0].set_ylabel('Amplitude')
    ax[1].plot(ws_Y,'r') # plotting the spectrum
    ax[1].set_xlabel('Freq (Hz)')
    ax[1].set_ylabel('|Y(freq)|')
    
    plt.show()
    '''
    
    #make the length of frq same as fft
    frq_rep = np.matlib.repmat(frq, 1,w_num+1).reshape(-1)

    return ws_Y, frq_rep

"""Main Function, FFT feature extraction for all strings in Conbiner boxes""" 
def main_generate_FFT():
    #profiling
    start = time.time()
    
    #grab all combiner boxes
    strFiles = glob.glob(cbPath + '*.csv')
    #Sampling rate
    Fs = 1/60
    window_size = 12*60*8
    
    #iterate each CB to compute features
    for cb in strFiles:
        #read cb all data and smooth
        print(cb)
        cbFile = cb
        df = pd.read_csv(cbFile)
        df_strings = df.iloc[:,1:17]
        df_strings = df_strings.dropna(axis=0, how='any')
        smLen = 60
        df_strings = pd.rolling_mean(df_strings, smLen)
        colName = df_strings.columns.values
        strName = colName[0:16]
        
        #fft feature holder for each CB
        all_ffts = pd.DataFrame()
    
        for idx, strName in enumerate(strName):
            current = df_strings[strName].as_matrix()
            current = current[smLen:]
            
            fft_fea, frq_rep = fftTrans(current,Fs, window_size)
            all_ffts[strName] = pd.DataFrame(data=fft_fea, columns=[strName])

        #Append frequencies column
        all_ffts['Freq'] = pd.DataFrame(data=frq_rep, columns=['Freq'])
        #obtain estimated data and record to file
        filename = feaPath + 'FFT_'+os.path.basename(cb)
        all_ffts.to_csv(filename, sep=',',header=True)
    
    end = time.time()
    runtime = end - start
    msg = "Str Data Writing Process Took {time} seconds to complete"
    print(msg.format(time=runtime))
    
    return "Wao!"      

#region level slope, data extraction
def main():
    #profiling
    start = time.time()
    
    hlxIDs = ['S35-NBA-HL04','S35-NBA-HL05']#,'S35-NBA-HL06','S35-NBA-HL07','S35-NBA-HL08','S35-NBA-HL36-1','S35-NBA-HL36-2','S35-NBA-HL36-3']
    
    colTot = np.zeros(264082)#264082
    print(colTot.shape)
    df = pd.DataFrame()
    
    for hlxID in hlxIDs: 
        cbData = queryAnyData(hlxID, startDT,endDT)
        print(cbData.head())
        strCurrents = cbData.iloc[:,1:16]
        colSum = strCurrents.sum(axis = 1)
        colTot = np.add(colSum.as_matrix(),colTot)
        print(colTot.shape)
    #create dataframe contain  data_date,Fs2m, colTot
    df['data_date'] = cbData['data_date']
    df['Fs2m'] = cbData['Fs2m']
    df['strSum'] = pd.DataFrame(data=colTot, columns=['strSum'])
    
    #grab slopes
    df = df.dropna(axis=0, how='any')
    
    filename = feaPath + 'raw_data_1012_S35NBA.csv'
    df.to_csv(filename, sep=',',header=True)
    
    smLen = 60
    
    all_slopes = pd.DataFrame()
    
    current = pd.rolling_mean(df['strSum'], smLen).as_matrix()
    current = current[smLen:]
    features = pd.rolling_mean(df['Fs2m'], smLen).as_matrix()#all features
    features = features[smLen:]
        
    slopes = grabSlopeData(current,features)
    all_slopes['Slopes'] = pd.DataFrame(data=slopes, columns=['Slopes'])
    
    #obtain estimated data and record to file
    filename = feaPath + 'slope_features_1012_S35NBA.csv'
    all_slopes.to_csv(filename, sep=',',header=True)
    
    end = time.time()
    runtime = end - start
    msg = "Str Data Writing Process Took {time} seconds to complete"
    print(msg.format(time=runtime))   
    
    return "a great day"        
                                    
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
    