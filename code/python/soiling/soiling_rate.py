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

# Temp Bucket
tempRg = [[30.0, 40], [20.0, 30], [10.0, 20], [0.0, 10.0], [-10.0, 0.0]]

# Data Path
resPath = '/Users/mira67/Documents/concord/concord_work/inverter/'
figPath = '/Users/mira67/Documents/concord/concord_work/'
qxjl = '/Users/mira67/Documents/concord/concord_work/qxjl.csv'


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


def avgSoilingRate(df):
    clean = pd.read_csv(qxjl)
    clean = clean[clean.nbqno == 'S01-NBA']
    cleanDates = clean['qxdate'].tolist()
    df = df.fillna(method='ffill')
    soilingDict = {}
    gpi = []
    # remove extreme outliers
    upper = np.percentile(df.Pr, 75)  # can get based on different temperatures
    slope = df.Pr / upper  # df.InvCPR  #
    df['slope'] = removeOutliers(slope, 1.5)

    for idx, dt in enumerate(cleanDates[:-1]):
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
            if slope < 0:
                gpi.append(slope * 100)
                # plot
                plt.plot(dn, data.slope, '.', label=str(rgDate))
                p_pred = lm.predict(dn.reshape(-1, 1))
                plt.plot(dn, p_pred, linewidth=2, label=str(rgDate) + 'regression')
    # plt.legend()
    plt.xlabel('# of Days after Clean Event')
    plt.ylabel('Normalized G-PI to Median')
    plt.figure(2)
    plt.hist(gpi, label='Distribution of Soiling Rates', bins=20)
    plt.xlabel('Soiling Rate (%)/ Day')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()
    print(median(gpi), gpi)

    return soilingDict


if __name__ == "__main__":
    # lignClean()
    #nbqData = pd.read_csv(resPath + 'S01-NBA.csv')
    df = pd.read_csv(resPath + 'slope_ransac.csv')
    soilingDict = avgSoilingRate(df)
    # print(soilingDict)
    #nbqData['P'] = nbqData['I'] * nbqData['V']
    #optGPI = OptimalGPI(nbqData)
