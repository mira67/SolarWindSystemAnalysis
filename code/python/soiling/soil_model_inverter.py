# -*- coding: utf-8 -*-
# Soiling Rate Dev, at inverter level
# Author: Qi Liu
# Email: qi.liu@colorado.edu

#modified by Yingying Zhao on Feb 6, 2018

import pymysql.cursors
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
import glob
import os
import tool

# Parameters configuration
startDTModel = '2016-01-01'
endDTModel = '2017-03-26'
invertnum = 74

# date list
start = datetime.datetime.strptime(startDTModel, "%Y-%m-%d").date()
end = datetime.datetime.strptime(endDTModel, "%Y-%m-%d").date()
dateList = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

dayList = []
for day in dateList:
    dayList.append(str(day))

# date list
start = datetime.datetime.strptime(startDTModel, "%Y-%m-%d").date()
end = datetime.datetime.strptime(endDTModel, "%Y-%m-%d").date()
dateList = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

dayList = []
for day in dateList:
    dayList.append(str(day))

timeRg = ['05:30', '19:30'];  # use pandas to get data within this range
tempRg = [-10,50]
Fs2mRg = [50,1000]
WdRg = [0,365]
WvRg = [0,50]
SdRg = [0,100]
resPath = '/Users/zhaoyingying/surfacesoiling/data/inverter/processed/'
singleslopePath = '/Users/zhaoyingying/surfacesoiling/data/inverter/slope/singleransac/'
MultiSlopePath = '/Users/zhaoyingying/surfacesoiling/data/inverter/slope/multiransac/'
figPath = '/Users/zhaoyingying/surfacesoiling/data/fig/'
qxjl = '/Users/zhaoyingying/surfacesoiling/data/qxjl.csv'
powerPath = '/Users/zhaoyingying/surfacesoiling/data/results/'


"""
Data Query Module: Extract data from database, table-nbq
Input: nbq Info: nbqID, Datetime: startDT,endDT
Output: nbq parameters
"""

def queryNbqData(nbqID, startDT, endDT, timeRg):

    sql1 = """SELECT data_date, I,V FROM pingyuan.nbq WHERE nbqno = '{}'
            AND data_date BETWEEN '{}' AND '{}'
            AND TIME(data_date) BETWEEN '{}'AND '{}'"""
    sqlSts1 = sql1.format(nbqID, startDT, endDT, timeRg[0], timeRg[1])

    sql2 = """SELECT data_date,Fs1m, Fs2m, Wv, Wd, Sd, T0,I1m, I2m, V1m, Fs1Day,Fs2Day FROM pingyuan.qxz
            WHERE data_date BETWEEN '{}' AND '{}'
            AND TIME(data_date) BETWEEN '{}'AND '{}';"""
    sqlSts2 = sql2.format(startDT, endDT, timeRg[0], timeRg[1])

    # Make database connetion
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='123456',
                         db='pingyuan',
                         port=3306,
                         charset='utf8mb4',
                         cursorclass=pymysql.cursors.DictCursor, local_infile=True)
    cbData = pd.DataFrame()
    try:
        '''training data'''
        cursor = db.cursor()
        
        cursor.execute(sqlSts1)
        
        db.commit()

        # collect query data
        strCurrent = pd.DataFrame(cursor.fetchall())
      

        cursor.execute(sqlSts2)
        db.commit()

        # collect query data
        features = pd.DataFrame(cursor.fetchall())

        # join table to avoid missing dates problem
        cbData = strCurrent.join(features.set_index('data_date'), on='data_date')

    except Exception as e:
        # Rollback in case there is any error
        db.rollback()
        print('Not able to query hlx %s' % (nbqID))

    # close connection
    db.close()
    return cbData

# Main

def main_old():
    # list of combiner boxes
    hlx_info = pd.read_csv('/Users/zhaoyingying/surfacesoiling/data/hlxinfo.csv')
    nbqList = hlx_info['nbqno'].unique().tolist()
    print(nbqList)
    # hlxList = map(str, hlxList)

    start = time.time()

    for idx, nbqID in enumerate(nbqList):
        print(idx, nbqID)
        nbqData = queryNbqData(nbqID, startDTModel, endDTModel, timeRg)
        # fill na with the forward valid data
        nbqData.fillna(method='ffill')
        nbqData.to_csv(resPath + nbqID + '.csv')

        # downsample for quick plot
        nbqSample = nbqData.sample(n=2000, replace='False')
        nbqSample = nbqSample.drop(['data_date'], axis=1)
        nbqSample['P'] = nbqSample['I'] * nbqSample['V']
        nbqSample['Pex'] = nbqSample['I1m'] * nbqSample['V1m']
        # plot
#        nbqSample = nbqSample.astype(np.float32)  # must convert to float32 before scatter
#        nbqPlot(nbqSample, nbqID)

    end = time.time()
    runtime = end - start
    msg = "Single Process Took {time} seconds to complete"
    print(msg.format(time=runtime))

    # profiling
    '''
    start = time.time()

    with mp.Pool(3) as pool:
        results = pool.map(extractSlopeFea, hlxList[121:301])
    end = time.time()
    runtime = end - start

    msg = "Feature Extraction Multi-Processing Took {time} seconds to complete"
    print(msg.format(time=runtime))
    '''
# analyse nbq data


def nbqPlot(df, title):
    # correlation matrix
    scatter_matrix(df, alpha=0.2, figsize=(6, 6), diagonal='kde')
    plt.show()
    # plt.savefig(figPath + title + '.png', dpi=300)





def linearModel(Features, stringCurrent, estimator):
    '''
    multiple regression estimation methods
    simple-simple linear
    theil-theil-sen, median
    '''
    if estimator == 'simple':
        lm = linear_model.LinearRegression()
        lm.fit(Features, stringCurrent)
    elif estimator == 'theil':
        pass
    elif estimator == 'ransac':
        lm = linear_model.RANSACRegressor()
        lm.fit(Features, stringCurrent)
    else:
        print('Invalid Estimator')
    return lm


def extractSlopeFea(df_org,fname):
    '''
    Grab daily slopes and put in dataframe and save to csv files
    '''
    # grab daily slopes -> upgrade code to spark later for multiple columns computing in parallel
    # create an array to store slopes for each strings
    numDays = len(dayList)
    print('there are '+str(numDays)+' days in total.')
    slopeArray = np.zeros((numDays, 1))
    try:
        for idx, day in enumerate(dateList):
            # query data
            print(day)
            df = df_org[(df_org['data_date'] >= str(day) + ' ' + timeRg[0]) &
                        (df_org['data_date'] < str(day) + '' + timeRg[1])]
            # print('remove data date')
            df = df.drop(['data_date'], axis=1)
            # print('add columns')
            df['P'] = df['I'] * df['V']
            # print('remove outliers')
            # df = df[df.apply(lambda x: np.abs(
            #     x - x.mean()) / x.std() < 3).all(axis=1)]
            print('computing...', df.shape)
            if df.shape[0] >= 100:
                # all strings currents
                df_power = df.P
                # feature data
                df_fea = df.Fs2m
                # features, currents
                try:
                    lm = linearModel(df_fea.values.reshape(-1, 1),
                                     df_power.values.reshape(-1, 1), 'ransac')
                    #estimated value
                    slope = lm.estimator_.coef_[0]  # lm.coef_[0]#extract slopes
                    # put in array
                    slopeArray[idx] = slope
                except:
                    # use the prev one, or assign zeros
                    slopeArray[idx] = slopeArray[idx - 1]
                    print('regression fail')

        # obtain dataframe and record to file
        slopeDF = pd.DataFrame(data=slopeArray, columns=['Pr'])
        slopeDF['data_date'] = pd.DataFrame(data=dayList)
        filename = singleslopePath + fname+'slope_ransac' + '.csv'
        slopeDF.to_csv(filename, sep=',', header=True)
        print('Completed computing slopes')

    except Exception as e:
        print('Exception: ', e)
        print('Not able to process')

    return '2018'

def extractMultiSlopeFea(df_org,fname):
    '''
    Grab daily multi slopes and put in dataframe and save to csv files
    '''
    # grab daily slopes -> upgrade code to spark later for multiple columns computing in parallel
    # create an array to store slopes for each strings
    numDays = len(dayList)
    print('there are '+str(numDays)+' days in total.')
    slopeArray = np.zeros((numDays, 5))
    try:
        for idx, day in enumerate(dateList):
            # query data
            print(day)
            
            #remove outliers due to sensor
            df = df_org[(df_org['data_date'] >= str(day) + ' ' + timeRg[0]) &
                        (df_org['data_date'] < str(day) + '' + timeRg[1])  ]
            # print('remove data date')
            df = df.drop(['data_date'], axis=1)
            # print('add columns')
            df['P'] = df['I'] * df['V']
            # print('remove outliers')
            # df = df[df.apply(lambda x: np.abs(
            #     x - x.mean()) / x.std() < 3).all(axis=1)]
            print('computing...', df.shape)
            if df.shape[0] >= 100:
                # all strings currents
                df_power = df.P
                # feature data:'Fs2m','Sd','Wd','Wv','T0']
                df_fea = df.loc[:,['Fs2m','Sd','Wd','Wv','T0']].values
                # feature data:'Fs2m','Sd','T0']
                df_fea = df.loc[:,['Fs2m','Sd','T0']].values

                try:
                    lm = linearModel(df_fea,
                                     df_power.values.reshape(-1, 1), 'ransac')
                    #estimated value
                    slope = lm.estimator_.coef_[0]  # lm.coef_[0]#extract slopes
                    # put in array
                    slopeArray[idx] = slope
                except:
                    # use the prev one, or assign zeros
                    slopeArray[idx] = slopeArray[idx - 1]
                    print('regression fail')

        # obtain dataframe and record to file
        slopeDF = pd.DataFrame(data=slopeArray, columns=['Pr','PrSd','PrWd','PrWv','PrT0'])
        slopeDF['data_date'] = pd.DataFrame(data=dayList)
        filename = MultiSlopePath + fname+'slope_ransac' + '.csv'
        slopeDF.to_csv(filename, sep=',', header=True)
        print('Completed computing slopes')

    except Exception as e:
        print('Exception: ', e)
        print('Not able to process')

    return '2018'

def removeOutliers(a, outlierConstant):
    '''
    remove outliers  and fill the missing data with median
    '''
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
    return resultList, upper_quartile


def alignClean(filePath,nbqname):
    nbq_qx = pd.read_csv(qxjl)

    df = pd.read_csv(filePath)
    print(df.head())
    # df = df[df['DeviceCode'] == '350M201M2M1']
    nbq_qx = nbq_qx[nbq_qx['nbqno'] == nbqname]  # reorganize code and make a flow

    nbq_qx['qxdate'] = pd.to_datetime(nbq_qx['qxdate'], format='%Y-%m-%d %H:%M:%S')
    
    nbq_qx.set_index(['qxdate'], inplace=True)


    # plot slope
    # df['data_date'] = pd.to_datetime(df['data_date'],
    #                                  format='%Y-%m-%d %H:%M:%S')
    # df.set_index(['data_date'], inplace=True)
#
    df['data_date'] = pd.to_datetime(df['data_date'],
                                     format='%Y-%m-%d %H:%M:%S')
    df.set_index(['data_date'], inplace=True)

    # reduce the slope number by divided 485
    slope = df.Pr / 485  # df.InvCPR  
    #normalize
    #slope = (df.Pr - df.Pr()) / (df.Pr.std())
    #slope = (df.Pr - df.Pr.min()) / (df.Pr.max() - df.Pr.min())
    med_slope, upper = removeOutliers(slope, 1)
    plt.plot(df.index, med_slope, label='Outliers/Missing Data Fixed')
    # med filtering
    y1 = medfilt(med_slope, 3)
    plt.plot(df.index, y1, label='7-day Med Filtered')

    # add clean record
    n_clean = [1.0] * nbq_qx.index.shape[0]

    plt.plot(nbq_qx.index, n_clean, 'x', label='Clean Event')
    plt.legend()
    plt.show()
    
def nbqTemp(df, title):
    tempRg = [[-10.0, 0.0], [0.0, 10.0], [10.0, 20.0], [20.0, 30.0], [30.0, 40.0]]
    #tempRg = [[0.0, 20.0], [20.0, 40.0], [40.0, 60.0], [60.0, 100.0]]
    # tempRg.reverse()
    
    df = df[df.P > 500]
    for rg in tempRg:
        data = df[df.T0 >= rg[0]]
        data = data[data.T0 < rg[1]]
        print(data.shape)
        plt.plot(data.Fs2m, data.P, '.', label=rg)
        lm = linearModel(data.Fs2m.values.reshape(-1, 1), data.P.values.reshape(-1, 1), 'ransac')
        print(rg, lm.estimator_.coef_[0])  #
        p_pred = lm.predict(data.Fs2m.values.reshape(-1, 1))
        plt.plot(data.Fs2m, p_pred, linewidth=2, label=str(rg) + 'regression')
    plt.ylabel('Power (W)')
    plt.xlabel('Solar Irradiance (W/m^2)')
    plt.legend()
    plt.show()

def main():
    # list of combiner boxes
    nbqData = pd.read_csv(resPath + 'S01-NBA.csv')
    # fill na with the forward valid data
    # fill in
    nbqData = nbqData.fillna(method='ffill')
    # print('start computing slopes')
    # extractSlopeFea(nbqData)

    # downsample for quick plot
    nbqSample = nbqData.sample(n=50000, replace='False')
    nbqSample = nbqSample.drop(['data_date'], axis=1)

    # data cleaning
    nbqSample = nbqSample[nbqSample.apply(lambda x: np.abs(x - x.mean()) / x.std() < 3).all(axis=1)]

    nbqSample['P'] = nbqSample['I'] * nbqSample['V']

# Optimal Slope
#     df = nbqSample
#     df_power = df.P
#     # feature data
#     df_fea = df.Fs2m
#     # fft feature holder for each CB
#     all_slopes = pd.DataFrame()
# # features, currents
#     lm = linearModel(df_fea.values.reshape(-1, 1),
#                      df_power.values.reshape(-1, 1), 'ransac')
#     slope = lm.estimator_.coef_[0]  # lm.coef_[0]#extract slopes
#     # put in array
#     print('slope', slope)

    # nbqSample['Pex'] = nbqSample['I1m'] * nbqSample['V1m']

    # plot
    nbqSample = nbqSample.astype(np.float32)  # must convert to float32 before scatter

    nbqTemp(nbqSample, 'Temp, P, Solar')
    # plt.plot(nbqSample['r'], '.')
    # plt.show()
    # nbqSample['T0'].hist()
    # plt.plot(nbqSample['R'])
    # plt.show()
    # nbqPlot(nbqSample, 'inverter')
def getnbqList():
    hlx_info = pd.read_csv('/Users/zhaoyingying/surfacesoiling/data/hlxinfo.csv')
    nbqList = hlx_info['nbqno'].unique().tolist()
    return nbqList


def cmpCleanBeforeAndAfter(slopePath):
    '''
    compare the slopes before cleaning and after cleaning for each inverter

    '''
    #get nbq list
    nbqList = getnbqList()
    for idx,item in enumerate(nbqList):
        #creating slopes after each cleaning
        pr = {}
        prsd ={}
        prwv ={}
        prwd ={}
        prt0={}
        
        #get slopes list for the inverter
        filename = ''
        flist = glob.glob(slopePath+'*.csv')        
        for f in flist:
            filename = os.path.basename(f)[0:7]
            if filename == item:
                break 
        slope_df = pd.read_csv(f)
        
        #normalized slopes and remove outliers
        slope_pr = slope_df.Pr
        slope_prsd = slope_df.PrSd
        slope_prwv = slope_df.PrWv
        slope_prwd = slope_df.PrWd
        slope_prt0 = slope_df.PrT0
    
        
    
        med_slope_pr, upper = tool.removeOutliers(slope_pr, 1)
        med_slope_prsd, upper = tool.removeOutliers(slope_prsd, 1)
        med_slope_prwv, upper = tool.removeOutliers(slope_prwv, 1)
        med_slope_prwd, upper = tool.removeOutliers(slope_prwd, 1)
        med_slope_prt0, upper = tool.removeOutliers(slope_prt0, 1)
    
        
        #medfile using 7 days 
        filterday = 7
        med_slope_pr = medfilt(med_slope_pr, filterday)
        med_slope_prsd = medfilt(med_slope_prsd, filterday)
        med_slope_prwv = medfilt(med_slope_prwv, filterday)
        med_slope_prwd = medfilt(med_slope_prwd, filterday)
        med_slope_prt0 = medfilt(med_slope_prt0, filterday)
        
        slope_df['smoothedSlopePr'] = med_slope_pr
        slope_df['smoothedSlopePrsd'] = med_slope_prsd
        slope_df['smoothedSlopePrwv'] = med_slope_prwv
        slope_df['smoothedSlopePrwd'] = med_slope_prwd
        slope_df['smoothedSlopePrt0'] = med_slope_prt0


        #get cleaning list for the inverter
        nbq_qx = pd.read_csv(qxjl)
        nbq_qx = nbq_qx[nbq_qx['nbqno'] == item]  
        nbq_qx['qxdate'] = pd.to_datetime(nbq_qx['qxdate'], format='%Y-%m-%d') 

        #qxList = time.strftime('%Y-%m-%d',nbq_qx['qxdate']).tolist() 
        qxList = nbq_qx['qxdate'].tolist()     
        qxList = [ riqi.strftime("%Y-%m-%d") for riqi in qxList ]
        

        
        #Creating slopes dictionay
        startDate = slope_df.at[0,'data_date']
        startIDX = 0
        
        for riqi in qxList:
            endIDX = slope_df[slope_df.data_date == riqi].index.tolist()[0]
            #original slopes
            #cmpdict[startDate] = slope_df.loc[startIDX:endIDX,'Pr']
            
            #slopes with no noise
            pr[startDate] = slope_df.loc[startIDX:endIDX,'smoothedSlopePr']
            prsd[startDate] = slope_df.loc[startIDX:endIDX,'smoothedSlopePrsd']
            prwv[startDate] = slope_df.loc[startIDX:endIDX,'smoothedSlopePrwv']
            prwd[startDate] = slope_df.loc[startIDX:endIDX,'smoothedSlopePrwd']
            prt0[startDate] = slope_df.loc[startIDX:endIDX,'smoothedSlopePrt0']
            
            #plot
            plt.figure(1)
            plt.plot(pr[startDate],label='Slopes at a cleaning interval')
            plt.figure(2)
            
            plt.plot(prsd[startDate],label='Slopes at a cleaning interval')
            plt.figure(3)
            plt.plot(prwv[startDate],label='Slopes at a cleaning interval')
            plt.figure(4)
            
            plt.plot(prwd[startDate],label='Slopes at a cleaning interval')
            plt.figure(5)
            
            plt.plot(prt0[startDate],label='Slopes at a cleaning interval')
            


    
            #next cleaning event
            startIDX = endIDX
            startDate = riqi
            
        #adding the last cleaning event
        pr[startDate] = slope_df.loc[startIDX:endIDX,'smoothedSlopePr']
        prsd[startDate] = slope_df.loc[startIDX:endIDX,'smoothedSlopePrsd']
        prwv[startDate] = slope_df.loc[startIDX:endIDX,'smoothedSlopePrwv']
        prwd[startDate] = slope_df.loc[startIDX:endIDX,'smoothedSlopePrwd']
        prwd[startDate] = slope_df.loc[startIDX:endIDX,'smoothedSlopePrt0']
        
            #plot
  
        #plt.ylabel('Slope of solar radiation')
        plt.xlabel('TimeStamp (Day)')


        
        plt.savefig(figPath + filename + '_multislopesVar.png', dpi=300)
        plt.show()         
        plt.close()
       
        break
    
def cmpPowerLoss():
    '''
    compare the power loss  before cleaning and after cleaning for each inverter

    '''
    #get nbq list
    nbqList = getnbqList()
    mean_list = np.zeros((invertnum, 1))
    var_list = np.zeros((invertnum, 1))
    for idx,item in enumerate(nbqList):
        #creating slopes after each cleaning

        filename = ''
        flist = glob.glob(powerPath+'*.csv')        
        for f in flist:
            filename = os.path.basename(f)[0:7]
            if filename == item:
                break 
        nbq_df = pd.read_csv(f).loc[:,['Date','P_true','Pe_slope']]
        
        
        
        #get cleaning list for the inverter
        nbq_qx = pd.read_csv(qxjl)
        nbq_qx = nbq_qx[nbq_qx['nbqno'] == item]  
        nbq_qx['qxdate'] = pd.to_datetime(nbq_qx['qxdate'], format='%Y-%m-%d') 

        nbq_qx = nbq_qx[(nbq_qx['qxdate'] >= '2016-01-01') & (nbq_qx['qxdate'] < '2017-01-01')]
        qxList = nbq_qx['qxdate'].tolist()     
        qxList = [ riqi.strftime("%Y-%m-%d") for riqi in qxList ]
             
        #Creating cleaning list  dictionay
        #startDate = nbq_df.at[0,'Date']
        startIDX = 0

        for riqi in qxList:
            
            endIDX = nbq_df[nbq_df.Date == riqi].index.tolist()[0]
            
            #relative power loss
            standard = nbq_df.at[startIDX,'Pe_slope']
            
            nbq_df.loc[startIDX:endIDX,'powerloss'] = ( nbq_df.loc[startIDX:endIDX,'Pe_slope'] - nbq_df.loc[startIDX:endIDX,'P_true'])/standard
                #/standard   
            #next cleaning event
            startIDX = endIDX
            #startDate = riqi
        
        nbq_df['powerloss'],upper_quartile = tool.removeOutliers(nbq_df.powerloss, 1.5)
        nbq_df['avg_powerloss'] = nbq_df['powerloss'].mean()
        mean_list[idx] = nbq_df['powerloss'].mean()
        var_list[idx ] =  nbq_df['powerloss'].var()
        
        
        #nbq_df['powerloss'] = nbq_df['powerloss'].rolling(window=5,center=True).median()
        n_clean = [0.0] * nbq_qx.qxdate.shape[0]
        
  

        nbq_df['Date'] = pd.to_datetime(nbq_df['Date'], format='%Y-%m-%d')
        nbq_df.set_index(['Date'], inplace=True)
        nbq_qx.set_index(['qxdate'], inplace=True)
      

    
        #plot for each inverter
#        plt.plot(nbq_qx.index, n_clean, 'x', label='Clean Event')
#        plt.plot(nbq_df.index, nbq_df.powerloss,label='Power loss at a cleaning interval')
#        plt.plot(nbq_df.index, nbq_df.avg_powerloss, label='Mean Relative Power Loss = 5.7%')
#        plt.ylabel('Relative Power Loss')
#        plt.xlabel('Date')
#        plt.legend()       
#        plt.savefig(figPath + filename + '_powerloss.png', dpi=300)
#        plt.show() 
#        plt.close()
        
        #plot for all inverters
    print(mean_list)
    plt.plot(mean_list, label='Mean Relative Power Loss')
    plt.plot(var_list, label='Variance of Relative Power Loss')
    plt.ylabel('Values')
    plt.xlabel('No. of Inverters')
    plt.legend() 
    plt.savefig(figPath + 'powerloss_allinverters.png', dpi=300)
    plt.show()
    plt.close()
     

                
        
    
#if __name__ == "__main__":
#    #get all nbq files
#    #main_old()
#    
#    #grad daily features 
#    flist = glob.glob(resPath+'*.csv')        
#    for f in flist:
#        nbqname = os.path.basename(f)
#        nbqData = pd.read_csv(f, delimiter=',')
#        nbqData = nbqData.fillna(method='ffill')
#        extractSlopeFea(nbqData,nbqname)
#        extractMultiSlopeFea(nbqData,nbqname)
#    
    #align each nbq with cleaning event.
#    flist = glob.glob(resPath+'slope/ransac/'+'*.csv')        
#    for f in flist:
#        # get nbqname, such as s01-nba
#        nbqname = os.path.basename(f)[0:7]
#        print(nbqname)
#        nbqData = pd.read_csv(f, delimiter=',')
#        alignClean(f,nbqname)
    #main()
    
    #analyzing slopes' variation
   # cmpCleanBeforeAndAfter(slopePath=MultiSlopePath)
    
    #cmpPowerLoss()
