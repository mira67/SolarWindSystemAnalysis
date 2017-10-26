# PV Classification - A full pipeline, data query to preprocessing, modeling 
# Record to file
# Query data to file
# Code is modular and can be extended
# Author: Qi Liu
# Date 10/25/2017
# Email: qi.liu@colorado.edu

import pymysql.cursors
import numpy as np
import pandas as pd
import time
import math
import multiprocessing as mp
import matplotlib.pyplot as plt
import plotly.plotly as py
from sklearn.cluster import KMeans
import glob
import os
import gc

# Configurations 
startDT = '2016-06-01'
endDT = '2016-08-31'
timeRg = ['06:00','19:00'];#use pandas to get data within this range

hourAday = 14
minAhour = 60
numDays = 5
feaWindow = hourAday*minAhour*numDays; # number of days

# Paths
feaPath = 'E:/myprojects/pv_detection/data/classification_0929/classification_features/'

# Step 1: query 8199 strings based on cuan_info from pingyuan2 database, combiner box level
def queryStringData(hlxID):
    sql = """SELECT * FROM pingyuan2.hlx WHERE combinerbox = '{}' AND data_date BETWEEN '{}' AND '{}'
    AND TIME(data_date) BETWEEN '{}'AND '{}' """
    sqlSts = sql.format(hlxID, startDT, endDT, timeRg[0], timeRg[1])
    
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
        cursor.execute(sqlSts)
        db.commit()
        #collect query data
        cbData = pd.DataFrame(cursor.fetchall())
        print(cbData.shape)
        
    except:
        # Rollback in case there is any error
        db.rollback()
        print('Not able to query combinerbox %s' % (hlxID))
        
    #close connection
    cursor.close()
    db.close()
    return cbData

# Step 2: Feature extraction for strings inside a combiner box
def strFeaExtract(cbData, hlxID, strList):
    # subtract median from each string
    currents = cbData[strList]
    currents = currents.fillna(0)
    # filter
    smLen = 60
    currents = pd.rolling_mean(currents, smLen)
    currents = currents[smLen:]
    # compute median for non-zero, real strings
    
    current_med = currents.median(axis = 1)
    current_base = currents.subtract(current_med,axis=0)
    
    
    # Store med feature data
    filename = feaPath + 'fft_5days_med_adi/'+ 'FFT_MED_'+hlxID+'.csv'
    cb_med = current_base
    cb_med['data_date'] = cbData['data_date'].iloc[60:]
    cb_med.to_csv(filename, sep=',',header=True)
    
    # For each pre-processed string, compute feature vector
    Fs = 1/60
    
    fft_power = pd.DataFrame()
    for strID in strList:
        fft_power = fftTrans(current_base[strID], Fs, feaWindow)  
        fft_power = fft_power[0:200]      
        # Record feature vector data to file
        filename = feaPath + 'fft_5days_cbs/' + 'FFT_'+hlxID+'_'+strID+'.csv'
        fft_power.to_csv(filename, sep=',',header=True)
        
    del [currents, current_med, current_base, fft_power, cb_med]
    
    return "Done"

# Step 3: Feature Extraction Modules - FFT, Wavelets or others
def fftTrans(current, Fs, window_size):
    Fs = Fs;  # sampling rate
    Ts = 1.0/Fs; # sampling interval
    ws = window_size
    
    y = current
    lenN = len(y) # length of the signal
    
    ws_Y = pd.DataFrame()
    
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
        ws_Y[str(w_num)] = pd.DataFrame(Y,columns=[str(w_num)])              
    
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
    
    # add one column -> convert freq to hours
    frq_hours = np.divide(1.0, frq_rep)
    frq_hours = np.divide(frq_hours, 60*60)
    ws_Y['Freq'] = pd.DataFrame(frq_rep,columns=['Freq'])    
    ws_Y['Period'] = pd.DataFrame(frq_hours,columns=['Period']) 
    
    del [y, frq_rep, Y]
    
    return ws_Y

# feaExtract
def feaExtract(hlxID, cuan_info):
    strList = cuan_info.loc[cuan_info['combinerbox'] == hlxID]
    strList = strList['branch_no']
    strList = 'I' + strList.astype(str)
    # query data
    cbData = queryStringData(hlxID)
    # feature extraction
    strFeaExtract(cbData,hlxID, strList)
    return "DONE"

# for each day, organize all 8199 features into a matrix
# Input: windowNum - data from which windown number to cluster
# Need further work to configure it into date range?
# record organized daily features to a file
def featuresByday(windowNum):
    #grab all combiner boxes
    dPath = "E:/myprojects/pv_detection/data/classification_0929/classification_features/fft_5days_cbs/"#fft_5days_cbs
    strFiles = glob.glob(dPath + '*.csv')
    
    # extract all feature vectors from all strings in the same window
    all_ffts = pd.DataFrame()
    for strf in strFiles:
        #read cb all data
        print(strf)
        df = pd.read_csv(strf)
        strName = os.path.basename(strf)
        #
        all_ffts[strName[:-4]] = pd.DataFrame(data=df[str(windowNum)], columns=[str(windowNum)])
    all_ffts['Period'] = pd.DataFrame(data=df['Period'], columns=['Period'])
    # Store to file for analysis
    filename = feaPath + 'fft_5days_str_windows/' + 'FFT_5days_window'+str(windowNum)+'.csv'
    all_ffts.to_csv(filename, sep=',',header=True)
    #
    gc.collect()
    
    return all_ffts

# use with featureByday function
# clustering method to partition states
def clusterByday(windowNum):
    win_ffts = featuresByday(windowNum)
    random_state = 5
    prior_k = 5 # prior knowledge about 
    X = win_ffts[1:60,1:-1]
    y_pred = KMeans(n_clusters=prior_k, random_state=random_state).fit_predict(X)
    # record y_pred to file, with string ID + state ID (cluster ID)
    return "Unsupervsied"

# Step 4: Main
def main_create_features():
    # use multi-threading
    #profiling
    start = time.time()
    
    #list of hlx
    cuan_info = pd.read_csv('E:/myprojects/pv_detection/data/classification_0929/cuaninfo_pingyuan.csv')
    hlxList = cuan_info['combinerbox']
    hlxUniq = hlxList.unique()
    # half way
    # hlxUniq = hlxUniq[160:]
    print("Number of Combiner Boxes: ", hlxUniq.shape)
    # processing
    
    for index, hlxID in enumerate(hlxUniq):
        print("Number of HLX: ", index)
        strList = cuan_info.loc[cuan_info['combinerbox'] == hlxID]
        strList = strList['branch_no']
        strList = 'I' + strList.astype(str)
        # query data
        cbData = queryStringData(hlxID)
        # feature extraction
        strFeaExtract(cbData,hlxID, strList)
        
        del [cbData, strList] # python for loop will create many variables, del
        gc.collect()
    
    # multi-threading
    #pool = mp.Pool(3)
    #results = pool.map(feaExtract, hlxUniq)
    
    end = time.time()
    runtime = end - start
    msg = "CB Data Writing Process Took {time} seconds to complete"
    print(msg.format(time=runtime))   
    
    return "Done"

# cluster file
def main():
    # use multi-threading
    #profiling
    start = time.time()
    
    windowNum = 0
    clusterByday(windowNum)
    
    end = time.time()
    runtime = end - start
    msg = "CB Data Writing Process Took {time} seconds to complete"
    print(msg.format(time=runtime))  
    
    return "done"

"""Execute Main"""   
if __name__ == "__main__":
    main() 