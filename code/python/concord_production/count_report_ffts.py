#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 09:30:50 2017

@author: zhaoyingying
"""
import glob
import numpy as np
import time
import pandas as pd
import os

inPath = '/Users/zhaoyingying/PVData/ADIbyCen/n_interval_fft_scale/fft_results/total_report/'
outPath = '/Users/zhaoyingying/PVData/ADIbyCen/n_interval_fft_scale/fft_results/total_report/total/'
totalPath='/Users/zhaoyingying/PVData/ADIbyCen/n_interval_fft_scale/fft_results/total_report/total/total.csv'
#define the number of the methods
methods_num = 10

if __name__ == '__main__':
    '''
    count the ffts classificatio report for everytime interval according to different methods
    '''
    
    starttime = time.time()
#    #output each file corresepoding to each method
#    for i in range(methods_num):
#        flist = glob.glob(inPath+'*.csv')
#        method_df = pd.DataFrame()
#        #for each method, traves all files
#        fname =''
#        for idx,item in enumerate(flist):
#            fname = os.path.basename(item)
#            df = pd.read_csv(item)
#            method_name= df.loc[i,'Method'] 
#            method_df.loc[idx,'#Time_interval'] =int(fname[26:-12])
#            method_df.loc[idx,method_name+'Precision'] = df.loc[i,'Precision']
#            method_df.loc[idx,method_name+'Recal'] = df.loc[i,'Recall']
#            method_df.loc[idx,method_name+'F1'] = df.loc[i,'F1']   
#            
#        results = method_df.sort_values(by=['#Time_interval'])
#        results.to_csv(outPath+method_name+'.csv',index=False)
    
        
    #get total performance 
    flist = glob.glob(outPath+'*.csv')
    frame = pd.DataFrame()
    list_ = []
    for f in flist:
        df = pd.read_csv(f,index_col=None, header=0) 
        list_.append(df)

    frame = pd.concat(list_)

    newframe = frame.groupby(['#Time_interval']).mean()

    newframe.to_csv(totalPath)
    
        
    endtime = time.time()
    print ('Processing Data use :%s sencods'%(endtime-starttime))