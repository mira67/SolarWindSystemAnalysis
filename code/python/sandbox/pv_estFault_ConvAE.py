# Data Partition with ConvAutoEncoder
# Author: Qi Liu
# Email: qliu.hit@gmail.com
# Date: 2017-09-18


import pymysql.cursors
import numpy as np
import pandas as pd
import time
import math
from sklearn import preprocessing

from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D
from keras.models import Model
from keras import backend as K

#import pydot
import matplotlib.pyplot as plt

from keras.utils import plot_model
from sklearn.preprocessing import MinMaxScaler

# Model Path
modelFile = 'E:/myprojects/pv_detection/data/model_fault_0912/aeModel.h5'
modelArc = 'E:/myprojects/pv_detection/data/model_fault_0912/modelArc.png'

# data window parameters
window_length = 720 # around a day
num_sensors = 2
step_size = 60
test_ratio = 0.2
smLen = 60

EPC = 2000# number of epochs

# Parameters configuration
startDT = '2016-04-15'
endDT = '2016-06-30'

timeRg = ['6:00','18:00'];#use pandas to get data within this range

"""
Step 1: Extract data from database, table-hlx
Input: String Info: hlxID, strID, Datetime: startDT,endDT
Output: String current
"""
def queryStrData(hlxID, strID, startDT,endDT):
    # AND TIME(data_date) BETWEEN '08:00'AND '17:00'
    # AND TIME(data_date) BETWEEN '08:00'AND '17:00'
    sql1 = """SELECT data_date,{} FROM pingyuan.hlx WHERE combinerbox = '{}' 
            AND data_date BETWEEN '{}' AND '{}';"""
    sqlSts1 = sql1.format(strID, hlxID, startDT,endDT)
    
    sql2 = """SELECT data_date,Fs2m FROM pingyuan.qxz WHERE data_date BETWEEN '{}' AND '{}';"""
    sqlSts2 = sql2.format(startDT,endDT)
    
    #Make database connetion
    db = pymysql.connect(host='localhost',
                                user='liuqi',
                                password='1234',
                                db='pingyuan',
                                port=3306,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor,local_infile=True)

    try:
        '''training data'''
        cursor = db.cursor()
        cursor.execute(sqlSts1)
        db.commit()
        
        #collect query data
        strCurrent = pd.DataFrame(cursor.fetchall())
        
        cursor.execute(sqlSts2)
        db.commit()
        
        #collect query data
        features = pd.DataFrame(cursor.fetchall())
        
        #join table to avoid missing data problem
        data = strCurrent.join(features.set_index('data_date'),on='data_date')
        
    except:
        # Rollback in case there is any error
        db.rollback()
        print('Not able to query string %s' % (strID))
        
    #close connection
    #cursor.close()
    db.close()
    return data

# Step 2: prepare training and test data for NN model
def dataPrepare(data):
    windows = []
    n_rows,n_cols = data.shape
    window_num = math.floor((n_rows-window_length)/step_size)
    
    print('window number: ', window_num, 'data length: ', n_rows)
    
    data = data.iloc[smLen:,:].as_matrix().astype(np.float32)
    
    data = preprocessing.scale(data)
    #scaler = MinMaxScaler()
    #scaler.fit(data)
    #data = scaler.transform(data)
    
    window_start = 0 
    for window_id in range(0, window_num):# every minite as a step
        #update window start
        window_start = window_id*step_size
        window_end = window_start + window_length
        window_range = range(window_start, window_end)
        window = list(data[window_range])
        windows.append(window)
        
    all_data = np.expand_dims(np.array(windows), axis=3)
    
    # train and test 
    test_num = math.floor(test_ratio* window_num)
    test_data = all_data[0:test_num,:,:,:]
    train_data = all_data[test_num: window_num,:,:,:]
    print('Test Number: ',test_num,'Train Data Shape: ', train_data.shape, 'Test Data Shape: ', test_data.shape)
    
    return train_data,test_data

# Step 3: Setup models
def trainModel(x_train,x_test):
    input_img = Input(shape=(window_length, num_sensors, 1))  # adapt this if using `channels_first` image data format
    
    x = Conv2D(1, (72, 2), activation='relu', padding='same')(input_img)
    x = MaxPooling2D((2, 1), padding='same')(x)
    x = Conv2D(1, (2, 1), activation='relu', padding='same')(x)
    encoded = MaxPooling2D((2, 1), padding='same')(x)
    
    # at this point the representation is (4, 4, 8) i.e. 128-dimensional
    
    x = Conv2D(1, (2, 1), activation='relu', padding='same')(encoded)
    x = UpSampling2D((2, 1))(x)    
    x = Conv2D(1, (72, 2), activation='relu', padding='same')(x)
    x = UpSampling2D((2, 1))(x)
    decoded = Conv2D(1, (72, 2), activation='sigmoid', padding='same')(x)
    
    autoencoder = Model(input_img, decoded)
    #autoencoder.compile(optimizer='adadelta', loss='binary_crossentropy')
    autoencoder.compile(optimizer='sgd', loss='mean_squared_error')
    
    # visualize model architecture
    #plot_model(autoencoder, to_file=modelArc)
    print('Fitting')
    
    autoencoder.fit(x_train, x_train,
                    epochs=EPC,
                    batch_size=5,
                    shuffle=True,
                    validation_data=(x_test, x_test))
    
    autoencoder.save(modelFile)
    return autoencoder
            
#Main
def main():
    dataPath = 'E:/myprojects/pv_detection/code/code/python/sandbox/testData_full.xlsx'
    strInfo = pd.read_excel(dataPath).values.tolist()
    
    #for quick test
    strInfo = strInfo[0:1]
    
    #profiling
    start = time.time()
    for idx,item in enumerate(strInfo):
        testData = strInfo[idx]
        hlxID = 'S18-NBA-HL02'#testData[0]
        strID = 'I2'#'I'+str(testData[1])
        FeatureList = ['FS1','Fs2','Fs1m','Fs2m','Wv','Wd','Sd','T0']
        
        data = queryStrData(hlxID, strID, startDT,endDT)
        data = data.dropna(axis=0, how='any')
        data = data.drop('data_date',axis=1)
        #data = pd.rolling_mean(data, smLen)
        
        print(data.head())
        
        train_x, test_x = dataPrepare(data)
        aeModel = trainModel(train_x, test_x)
        
        decoded_imgs = aeModel.predict(test_x)
    
        # visualization
        n = 5
        plt.figure(figsize=(20, 4))
        for i in range(n):
            # display original
            plt.figure(1)
            plt.subplot(2, n, i+1)
            test_ts = test_x[i].reshape(720, 2)
            plt.scatter(test_ts[:,1],test_ts[:,0])
        
            # display reconstruction
            plt.subplot(2, n, i + n+1)
            res_ts = decoded_imgs[i].reshape(720, 2)
            plt.scatter(res_ts[:,1],res_ts[:,0])
            
            plt.figure(2)
            plt.subplot(2, n, i+1)
            plt.plot(test_ts[:,0])
        
            # display reconstruction
            plt.subplot(2, n, i + n+1)
            plt.plot(res_ts[:,0])

            plt.show()
    
    end = time.time()
    runtime = end - start
    msg = "AutoEncoder Single-Processing Took {time} seconds to complete"
    print(msg.format(time=runtime))                
                
if __name__ == "__main__":
    main()