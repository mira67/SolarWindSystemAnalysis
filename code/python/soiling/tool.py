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
def bearing_plot(df, dirn='wind_dir', dir_info='Wind from the North', 
                 ax=None, N=16, bottom=0, loc_0='N', loc_90 ='E', zero_is_nan=True):
    # zero means that no wind is blowing so we will remove those values.
    if zero_is_nan:
        df = df[df[dirn]>0]
    if ax is None:
        ax = plt.subplot(111, polar=True)
    theta = np.linspace(0.0, 2 *np.pi, N+1)
    radii, _ = np.histogram(df[dirn].values, bins=(theta/np.pi*180))
    width = (2*np.pi) / N

    bars = ax.bar(theta[:-1], radii, width=width, bottom=bottom)
    
    ax.set_theta_zero_location(loc_0)
    clockwise = ['N', 'E', 'S','W', 'N']
    if clockwise[clockwise.index(loc_0)+1] == loc_90:
        ax.set_theta_direction(-1)

    # Use custom colors and opacity
    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.jet(r/float(np.max(radii))))
        bar.set_alpha(0.8)
    ax.text(0.5,1.1,dir_info, horizontalalignment='center', transform=ax.transAxes, fontsize=14)
    return(ax)

def windrose(df, dirn='wind_dir', speed='wind_speed', dir_info='Wind from the North', 
             ax=None, N=16, bottom=0, loc_0='N', loc_90 ='E', zero_is_nan=True):
    if zero_is_nan:
        df = df[df[dirn]>0]
    if ax is None:
        ax = plt.subplot(111, polar=True)
    theta = np.linspace(0.0, 2 *np.pi, N+1)
    width = (2*np.pi) / N
    
    ax.set_theta_zero_location(loc_0)
    clockwise = ['N', 'E', 'S','W', 'N']
    if clockwise[clockwise.index(loc_0)+1] == loc_90:
        ax.set_theta_direction(-1)
    
    srange = zip([0,5,10,20,50], [5,10,20,50,100], ['#0000dd','green','#dddd00','#FF7800','#dd0000']) 
    ntot = df[dirn].count()
    
    radii0 = [bottom]*N
    for smin, smax, c in srange:
        cond = ((df[speed]>=smin) & (df[speed]<smax))
        radii, _ = np.histogram(df[dirn][cond].values, bins=(theta/np.pi*180))
        radii = radii/float(ntot)*100
        bars = ax.bar(theta[:-1], radii, width=width, bottom=radii0, facecolor=c, alpha=0.8)
        #print smin, smax, c, radii
        radii0+= radii
    ax.text(0.5,1.1,dir_info, horizontalalignment='center', transform=ax.transAxes, fontsize=14)
    plt.savefig(figPath  + 'windrose.png', dpi=300)
    return(ax)
        
def windrose_cbar(fig=None):
    '''
    If you have a figsize in mind, then pass a figure object to this function
    and the colorbar will be drawn to suit
    '''
    import matplotlib.patches as mpatch
    
    if fig is None:
        fig = plt.figure(figsize=(5,.7))
    y = fig.get_figwidth()
    
    srange = zip([0,10,20,30,40], [10,20,30,40,50], ['#0000dd','green','#dddd00','#FF7800','#dd0000']) 
    n=1
    for smin, smax, c in srange:
        ax = plt.subplot(1,5,n)
        patch = mpatch.FancyBboxPatch([0,0], 1, 1, boxstyle='square', facecolor=c)
        ax.add_patch(patch)
        plt.axis('off')
        if y>=12:
            ax.text(.1, .4, '{smin} - {smax} m/s'.format(smin=smin, smax=smax),
                    fontsize=min(18, y+2), fontdict = {'color': 'white'})
        else:
            ax.text(.1, .4, '{smin} - {smax}\nm/s'.format(smin=smin, smax=smax),
                    fontsize=min(14, y+5), fontdict = {'color': 'white'})
        n+=1
    plt.savefig(figPath  + 'windrosebar.png', dpi=300)