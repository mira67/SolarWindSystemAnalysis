#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:23:54 2018

@author: zhaoyingying
"""
import pandas as pd
import glob
import os
import numpy as np
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import linear_model

figPath = '/Users/zhaoyingying/surfacesoiling/data/fig/'
dustRatePath = '/Users/zhaoyingying/surfacesoiling/data/dustRate.csv'

def getnbqList():
    '''
    get invert list for the PV site
    '''
    hlx_info = pd.read_csv('/Users/zhaoyingying/surfacesoiling/data/hlxinfo.csv')
    nbqList = hlx_info['nbqno'].unique().tolist()
    return nbqList

def getnbqFile(filePath, nbqName):
    '''
    get a specifice invert file.
    
    '''

    flist = glob.glob(filePath+'*.csv')        
    for f in flist:
        filename = os.path.basename(f)[0:7]
        if filename == nbqName:
            break 
    print('find the file sucessfully:')
    print(filename)
    return f
def removeOutliers(a, outlierConstant):
    
    
    upper_quartile = np.nanpercentile(a, 75)
    lower_quartile = np.nanpercentile(a, 25)
    
    IQR = (upper_quartile - lower_quartile) * outlierConstant
    quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
    resultList = []
    
    
    for y in a.tolist():
        if y >= quartileSet[0] and y <= quartileSet[1]:
            resultList.append(y)
        else:
            resultList.append(np.nanmedian(a))
    print('has removed outliers')
    return resultList, upper_quartile

def nbqPlot(df, title):
    # correlation matrix
    scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
    plt.savefig(figPath + title + 'correlation.png', dpi=300)
    plt.show()

def linearModel(Features, stringCurrent, estimator):
    '''
    multiple regression estimation methods
    simple-simple linear
    theil-theil-sen, median
    '''
    slope = 0
    if estimator == 'simple':
        lm = linear_model.LinearRegression()
        lm.fit(Features, stringCurrent)
        slope = lm.coef_[0]
    elif estimator == 'theil':
        lm = linear_model.TheilSenRegressor(random_state=42)
        lm.fit(Features, stringCurrent)
        slope = lm.coef_[0]
    elif estimator == 'ransac':
        lm = linear_model.RANSACRegressor(random_state=42)
        lm.fit(Features, stringCurrent)
        slope = lm.estimator_.coef_[0]
        print(lm.estimator_)
    
    else:
        print('Invalid Estimator')
    return lm, slope    
def soilingrate(invertname,method):
    '''
    get dust accumulation rate by method (median, mean)
    '''
    
    sr = pd.read_csv(dustRatePath)
    sr = sr[sr.nbqName == invertname]    
    sr.set_index(['nbqName'], inplace=True)
    dustRate = sr.at[invertname, method]
    return dustRate