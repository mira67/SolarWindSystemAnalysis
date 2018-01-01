#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 11:34:28 2017

@author: zhaoyingying
"""

import pandas as pd

#aggreagation feature set
aggFEPath = '/Users/zhaoyingying/PVData/ADIbyCen/temporal_frq_features/FI_Agg.csv'
#spectrum feature set
frqFEPath = '/Users/zhaoyingying/PVData/ADIbyCen/temporal_frq_features/FI_frq.csv'
#all feature set
allFEPath = '/Users/zhaoyingying/PVData/ADIbyCen/temporal_frq_features/FI_agg_frq.csv'

outPath = '/Users/zhaoyingying/PVData/ADIbyCen/temporal_frq_features/FI_total.csv'

def countFI(FS1,FS2,FS3):
    '''
    Count all features importance in each feature set
    '''
    avg_fs = pd.DataFrame(columns=['F1','F2','F3'])
    
    for i in range(FS1.shape[1]-1):
        avg_fs.loc[i,'F1'] = FS1.iloc[:,i].mean()
        print('get the mean')
    for i in range(FS2.shape[1]-1):
        print('start process the second fs')
        print(str(i))
        avg_fs.loc[i,'F2'] = FS2.iloc[:,i].mean()
    for i in range(FS3.shape[1]-1):
        avg_fs.loc[i,'F3'] = FS3.iloc[:,i].mean()
    avg_fs.to_csv(outPath)
        
if __name__ == '__main__':
    fs1 = pd.read_csv(aggFEPath,header=None)
    fs2 = pd.read_csv(frqFEPath,header=None)
    fs3 = pd.read_csv(allFEPath,header=None)
    countFI(fs1,fs2,fs3)