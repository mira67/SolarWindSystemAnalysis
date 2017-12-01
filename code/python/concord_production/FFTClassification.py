# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:58:02 2017

@author: xiaomei
"""

import numpy as np
import pandas as pd
import time
from sklearn import svm 
from sklearn.metrics import classification_report,confusion_matrix
from sklearn import preprocessing
from sklearn.model_selection import StratifiedKFold

AnomalyTypeNum = 5
FaultNum = 1034
kfold = 2 # cross validation
inPath = '/Users/zhaoyingying/PVData/ADIbyCen/ADIALLTimeSeriesrenameId_rawsignal.csv'
fftPath = '/Users/zhaoyingying/PVData/ADIbyCen/FFTADIALLTimeSeries_rawsignal.csv'
formatfftPath = '/Users/zhaoyingying/PVData/ADIbyCen/FFTADIALLTimeSeries_rawsignal_fmt.csv'
outPath = '/Users/zhaoyingying/PVData/ADIbyCen/frq_report.csv'
#inPath = 'D:/Xiaomei/SolarEnergy/SolarEnergy/python/classificationADI/ADItimeseries/0600_1800/ADIbyCen/ADIALLTimeSeriesrenameId.csv'
#outPath = 'D:/Xiaomei/SolarEnergy/SolarEnergy/python/classificationADI/ADItimeseries/0600_1800/ADIbyCen/FFTADIALLTimeSeries1min_722ws.csv'
def fftTrans(current,Fs, window_size):
    Fs = Fs;  # sampling rate
    #Ts = 1.0/Fs; # sampling interval
    ws = window_size
    
    y = current
    lenN = len(y) # length of the signal
    
    ws_Y = np.empty(shape=None)
    #init frq
    frq = 0.0
    w_num = 0
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

    
    #make the length of frq same as fft
    frq_rep = np.matlib.repmat(frq, 1,w_num+1).reshape(-1)

    return ws_Y, frq_rep

def generate_FFT():
    '''
    extracting the ADI time series features:
        
    '''
    #profiling
    start = time.time()
    
    #read ADI time series
    df = pd.read_csv(inPath,header = None)
    AllADI = df.iloc[:,1:-1].as_matrix()
    ALLADI=np.transpose(AllADI)
    ADIID = df.iloc[:,0].as_matrix()

    
    #Sampling rate
    Fs = 1/1
    window_size = 30
    all_ffts = pd.DataFrame()
        
    print(len(ADIID))
    for idx, ADIName in enumerate(ADIID):
        fft_fea, frq_rep = fftTrans(ALLADI[:,idx],Fs, window_size)    
        all_ffts[ADIName] = pd.DataFrame(data=fft_fea, columns=[ADIName])
    all_ffts.to_csv(fftPath, sep=',',header=True)
    
    end = time.time()
    runtime = end - start
    msg = "Str Data Writing Process Took {time} seconds to complete"
    print(msg.format(time=runtime))
    return "Wao!" 
   
def formafFFT():
    fftmatrix = pd.read_csv(fftPath).iloc[:,1:].as_matrix()
    newfftmatrix = np.transpose(fftmatrix)
    
#    newfftmatrix = np.around(newfftmatrix, decimals=2)

    
    df = pd.read_csv(inPath,header = None)
    IDname = df.iloc[:,0].as_matrix()
    faultType = df.iloc[:,-1].as_matrix()
    fft = open(formatfftPath, "w")
    tmp=[]
    for i in range(newfftmatrix.shape[0]):
        line=''
        for j in range(newfftmatrix.shape[1]):
            line = line+str(newfftmatrix[i,j])+','  
        tmp.append(line)
    for i in range(FaultNum):
        fft.write(str(IDname[i])+','+tmp[i]+str(faultType[i])+'\n')
    fft.close()

def pvSVM(trainX,testX,trainY,testY):
    svc = svm.SVC() 
    svc.fit(trainX, trainY)
    preds = svc.predict(testX)
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
        report = pvSVM(trainX,testX,trainY,testY)
        rpt.write(report)

    #close report file
    rpt.close()
    return 'ok'    
    
if __name__ == '__main__':
    #generate_FFT()
    #formafFFT()
        
    data = pd.read_csv(formatfftPath, delimiter=',', header=None)
    pvKfoldValidation(data,kfold)
    
    