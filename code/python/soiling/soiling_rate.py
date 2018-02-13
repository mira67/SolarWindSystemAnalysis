'''
Model: Extracting Soiling Rate from Each Interval
Author: Qi Liu
Email: qi.liu@colorado.edu
'''
import numpy as np
import pandas as pd
import time
import math
import datetime
import multiprocessing as mp
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn import linear_model
from scipy.signal import medfilt
from statistics import median
import tool
import glob
import os

# Temp Bucket
tempRg = [[30.0, 40], [20.0, 30], [10.0, 20], [0.0, 10.0], [-10.0, 0.0]]
tempRg = [-10,50]
Fs2mRg = [50,1000]
WdRg = [0,365]
WvRg = [0,50]
SdRg = [0,100]
soilRate = -0.0113749348364

# Data Path
resPath = '/Users/zhaoyingying/surfacesoiling/data/inverter/slope/ransac/'
MultiSlopePath = '/Users/zhaoyingying/surfacesoiling/data/inverter/slope/multiransac/'
nbqPath = '/Users/zhaoyingying/surfacesoiling/data/inverter/'
figPath = '/Users/zhaoyingying/surfacesoiling/data/fig/'
qxjl = '/Users/zhaoyingying/surfacesoiling/data/qxjl.csv'
dustRatePath = '/Users/zhaoyingying/surfacesoiling/data/'
singleslopePath = '/Users/zhaoyingying/surfacesoiling/data/inverter/slope/singleransac/'


def DataClean(df):
    '''
    make sure the input as continuous date
    '''
    # fill in NA
    df = df.fillna(method='ffill')
    # remove extreme outliers
    df = df[df.P > 500]  # empirical numbers
    return df


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
    else:
        print('Invalid Estimator')
    return lm, slope


def removeOutliers(a, outlierConstant):
    upper_quartile = np.percentile(a, 75)
    lower_quartile = np.percentile(a, 25)
    IQR = (upper_quartile - lower_quartile) * outlierConstant
    quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
    resultList = []
    for y in a.tolist():
        if y >= quartileSet[0] and y <= quartileSet[1]:
            resultList.append(y)
        else:
            resultList.append(np.median(a))
    return resultList


def OptimalGPI(df):
    '''
    only considering temperature
    # Need to grab topper performed values as optimal GPI, current one is average
    # Using Average as Normalization Base Is also OK
    '''
    df = DataClean(df)
    # compute optimal for each bucket
    gpiDictionary = {}
    for rg in tempRg:
        data = df[df.T0 >= rg[0]]
        data = data[data.T0 < rg[1]]
        data = data[data.Sd < 100]
        # need regress with topper data FIX
        lm, slope = linearModel(data.Fs2m.values.reshape(-1, 1),
                                data.P.values.reshape(-1, 1), 'ransac')
        gpiDictionary[str(rg)] = slope
        # plot
        p_pred = lm.predict(data.Fs2m.values.reshape(-1, 1))
        plt.plot(data.Fs2m, data.P, '.', label=rg)
        plt.plot(data.Fs2m, p_pred, linewidth=2, label=str(rg) + 'regression')
    plt.ylabel('Power (W)')
    plt.xlabel('Solar Irradiance (W/m^2)')
    plt.legend()
    plt.show()
    # results
    print(gpiDictionary)
    return gpiDictionary  # gpi for each temp bucket

def NewOptimalGPI(df):
    '''
    considering multi factors: solar radiation, humidity, wind direction, wind speed.
    # Need to grab topper performed values as optimal GPI, current one is average
    # Using Average as Normalization Base Is also OK
    '''
    df = DataClean(df)
    df = df.fillna(method='ffill')
    df = df.fillna(method='backfill')
    
    #experience value
    df = df[df.Fs2m > 50]
    df = df[(df['Fs2m'] < Fs2mRg[1]) & (df['Fs2m'] > Fs2mRg[0]) &
                        (df['T0'] < tempRg[1]) & (df['T0'] > tempRg[0]) &
                        (df['Sd'] < SdRg[1]) & (df['Sd'] > SdRg[0]) &
                        (df['Wv'] < WvRg[1]) & (df['Wv'] > WvRg[0]) &
                        (df['Wd'] < WdRg[1]) & (df['Wd'] > WdRg[0]) ]

    data = df
    features = data.loc[:,['Fs2m','Sd','Wd','Wv','T0']].values
    
        # need regress with topper data FIX
    lm, slope = tool.linearModel(features,
                                data.P.values.reshape(-1, 1), 'ransac')
    #print(slope)
 
        # plot
    p_pred = lm.predict(features)
 
    plt.plot(data.Fs2m, data.P, '.', label='scatters')
    plt.plot(data.Fs2m, p_pred, linewidth=1, label='regression')
    plt.ylabel('Power (W)')
    plt.xlabel('Solar Irradiance (W/m^2)')
    
    plt.legend()
    plt.show()
    # results

    return slope  # gpi for each temp bucket

def avgSoilingRate(df,nbqName):
    '''
    Avg soiling rate for Gpi
    '''
    clean = pd.read_csv(qxjl)
    clean = clean[clean.nbqno == nbqName]
    cleanDates = clean['qxdate'].tolist()
    df = df.fillna(method='ffill')
    soilingDict = {}
    gpi = []
    # remove extreme outliers
    upper = np.percentile(df.Pr, 75)  # can get based on different temperatures
    slope = df.Pr / upper  # df.InvCPR  #

    
    
    df['slope'] = removeOutliers(slope, 1.5)

    for idx, dt in enumerate(cleanDates[:-1]):
        #obtain a cleaning interval
        data = df[df.data_date > dt]
        data = data[data.data_date < cleanDates[idx + 1]]
        rgDate = [dt, cleanDates[idx + 1]]
        
        soilingDict[str(rgDate)] = data.slope.tolist()
        ndays = len(data.slope.tolist())
        dn = np.arange(ndays)
        plt.figure(1)
        if ndays > 1:
            # regression
            lm, slope = linearModel(dn.reshape(-1, 1),
                                    data.slope.values.reshape(-1, 1), 'theil')
            if slope < 0: # for dust accumulation case
                gpi.append(slope)
                #gpi.append(slope * 100)
                # plot
#                plt.plot(dn, data.slope, '.', label=str(rgDate))
                p_pred = lm.predict(dn.reshape(-1, 1))
#                plt.plot(dn, p_pred, linewidth=2, label=str(rgDate) + 'regression')
#   
#    
#    plt.xlabel('# of Days after Clean Event')
#    plt.ylabel('Normalized G-PI to Median')
#    plt.savefig(figPath + 'GPITrendaftercleaning.png', dpi=300)
#    plt.figure(2)
#    plt.hist(gpi, label='Distribution of Soiling Rates', bins=20)
#    plt.xlabel('Soiling Rate (%)/ Day')
#    plt.ylabel('Frequency')
#    plt.legend()
#    plt.savefig(figPath + 'DistributionSoilingrate.png', dpi=300)
#    plt.show()
#    print(median(gpi), np.mean(gpi),np.std(gpi),gpi)

 
    #return soilingDict
    return median(gpi), np.mean(gpi),np.var(gpi)

def avgSoilingRateSd(df):
    '''
    Avg soiling rate for Sd: humidity
    '''
    clean = pd.read_csv(qxjl)
    clean = clean[clean.nbqno == 'S01-NBA']
    cleanDates = clean['qxdate'].tolist()
    df = df.fillna(method='ffill')
    soilingDict = {}
    gpi = []
    # remove extreme outliers
    #upper = np.percentile(df.Pr, 75)  # can get based on different temperatures
    #slope = df.Pr / upper  # df.InvCPR  #
    slope = df.PrT0
    
    
    df['slope'] = removeOutliers(slope, 1.5)

    for idx, dt in enumerate(cleanDates[:-1]):
        #obtain a cleaning interval
        data = df[df.data_date > dt]
        data = data[data.data_date < cleanDates[idx + 1]]
        rgDate = [dt, cleanDates[idx + 1]]
        
        soilingDict[str(rgDate)] = data.slope.tolist()
        ndays = len(data.slope.tolist())
        dn = np.arange(ndays)
        plt.figure(1)
        if ndays > 1:
            # regression
            lm, slope = linearModel(dn.reshape(-1, 1),
                                    data.slope.values.reshape(-1, 1), 'theil')
            if slope <  0: # for dust accumulation case
                gpi.append(slope * 100)
                # plot
                plt.plot(dn, data.slope, '.', label=str(rgDate))
                p_pred = lm.predict(dn.reshape(-1, 1))
                plt.plot(dn, p_pred, linewidth=2, label=str(rgDate) + 'regression')
    # plt.legend()
    plt.xlabel('# of Days after Clean Event')
   # plt.ylabel('Normalized G-PI to Median')
    plt.ylabel('G-PI')
    plt.savefig(figPath + 'GPITrendaftercleaning.png', dpi=300)
    plt.figure(2)
    plt.hist(gpi, label='Distribution of Soiling Rates', bins=20)
    plt.xlabel('Soiling Rate (%)/ Day')
    plt.ylabel('Frequency')
    plt.legend()
    plt.savefig(figPath + 'DistributionSoilingrate.png', dpi=300)
    plt.show()
    #print(median(gpi), gpi)
   # print(soilingDict)
 
    return soilingDict

def countdust(inPath,method):
    '''
    count the median, mean, std of dust accumulation for each inverter
    '''
    
    flist = glob.glob(inPath+'*.csv')
    nbqList = []
    mdList = []
    mnList = []
    stdLsit = []
    
    
    for idx, f in enumerate(flist):
        nbqname = os.path.basename(f)[0:7]
        print(nbqname)
        nbq_df = pd.read_csv(f)
        md,mn,std = avgSoilingRate(nbq_df,nbqname)
        nbqList.append(  nbqname)
        mdList.append(md)
        mnList.append( mn)
        stdLsit.append( std)
    soiling_df = pd.DataFrame(columns=['nbqName', 'dustMedian', 'dustMean', 'dustStd'])
    soiling_df['nbqName'] = nbqList
    soiling_df['dustMedian'] = mdList
    soiling_df['dustMean'] = mnList
    soiling_df['dustStd'] = stdLsit
    soiling_df.to_csv(dustRatePath+method+'dustRate.csv')
    
    #plot
    plt.plot(soiling_df.dustMedian, label='Median of Dust Accumulation Rate')
    plt.plot(soiling_df.dustMean, label='Mean of Dust Accumulation Rate')
    plt.plot(soiling_df.dustStd, label='Var of Dust Accumulation Rate')
    plt.xlabel('No. of Inverters')
    plt.ylabel('Value')
    plt.legend()
    plt.savefig(figPath + method+'spatialVarDust.png', dpi=300)
    plt.show()
    plt.close()
    
    
    
if __name__ == "__main__":
    # lignClean()
    #get optimal GPI
#    nbqData = pd.read_csv(nbqPath + 'S01-NBA.csv')
#    nbqData['P'] = nbqData['I'] * nbqData['V']
#    optGPI = NewOptimalGPI(nbqData)
    
    method= 'single'  
    countdust(singleslopePath,method)
