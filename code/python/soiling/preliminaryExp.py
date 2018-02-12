#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 16:16:37 2018

@author: zhaoyingying
"""
import pandas as pd
import soiling_rate
import datetime
import numpy as np
import tool
from scipy.signal import medfilt
from pandas import rolling_median



qxjl = '/Users/zhaoyingying/surfacesoiling/data/qxjl.csv'
allnbqData = '/Users/zhaoyingying/surfacesoiling/data/Inv_GPI_pingyuan.csv'
qxz = '/Users/zhaoyingying/surfacesoiling/data/pingyuan_weather_station2016.csv'
qxz_nqb = '/Users/zhaoyingying/surfacesoiling/data/qxz_nqb.csv'

startDTModel = '2016-01-01'
endDTModel = '2017-01-01'
timeRg = ['05:30', '19:30']  # use pandas to get data within this range
    
# date list
start = datetime.datetime.strptime(startDTModel, "%Y-%m-%d").date()
end = datetime.datetime.strptime(endDTModel, "%Y-%m-%d").date()
dateList = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

dayList = []
for day in dateList:
    dayList.append(str(day))  

def alignNBQandQXZ():
    '''
    alighn the nbq data to qxz 
    '''
    #qxz data
    nbq_qx = pd.read_csv(qxz)
    nbq_qx['Date'] = pd.to_datetime(nbq_qx['Date'], format='%Y-%m-%d')

  
    #nbq data
    all_nbq = pd.read_csv(allnbqData)
    all_nbq['Date'] = pd.to_datetime(all_nbq['Date'],format='%Y-%m-%d') 

    
    merged = pd.merge(all_nbq, nbq_qx, on=['Date'])
    print(merged)
    merged.to_csv(qxz_nqb,index =False)
    
    

def getGPI(file):
    '''
    get optimal GPI for each inveter  
    '''
    df = pd.read_csv(file)
    print(df)
    
    #get all nbq
    allnbq = df['DeviceName'].values.tolist()
    allnbq = list(set(allnbq))
    allnbq.sort()
    print(allnbq)
    
    #get optiaml GPI for each nbq
    for idx,item in enumerate(allnbq):
        if idx == 0:
            print(item)
            df = df[df.DeviceName == item]
            soiling_rate.OptimalGPI(df)

def getDailySolarRad():
    '''
    get daily solar radiation from tile fuzhaoyi
    '''
    #from any inverter
    filePath = '/Users/zhaoyingying/surfacesoiling/data/inverter/processed/S01-NBA.csv'
    df = pd.read_csv(filePath)
    
    #convert datetime to date
    dateList = [item[0:10] for item in df['data_date'].values]
    df['Date'] = dateList
    df['Pe_WeaStation'] = df['I1m'] * df['V1m']
    df = df.groupby(['Date']).sum()
    df =df.loc[:,['Fs2m','Pe_WeaStation']]
    print(df)
    df.to_csv('/Users/zhaoyingying/surfacesoiling/data/daily_Weather_Station.csv')

def avgTcell():
    '''
    caculated the average Temperature of cell in weather station in 2016: 30.160829562814
    
    '''
    filePath = '/Users/zhaoyingying/surfacesoiling/data/inverter/processed/S01-NBA.csv'

    
    numDays = len(dayList)
    print('there are '+str(numDays)+' days in total.')
    df_org = pd.read_csv(filePath)
    df = df_org[(df_org['data_date'] >= str(dateList[0]) + ' ' + timeRg[0]) &
                        (df_org['data_date'] < str(dateList[-1]) + '' + timeRg[1])]
    df = df.loc[:,['Wv','T0','Fs2m']]

    df['fv'] = 17.1+ 5.7 * df['Wv']
    alphatau = 0.9
    ita = 0.1545
    beta = 0.0043
    Tr= 25
    
    df['Tcell'] = (df['fv'] * df['T0'] + df['Fs2m']*(alphatau - ita -beta*ita*Tr))  / (df['fv']-beta*ita*df['Fs2m'])
    avg_cell =  df['Tcell'].mean()
    print(avg_cell)
    return avg_cell
    
    
def dailyCPR():
    '''
    get daily CPR
    '''
    #get the average cell temperature
    Avg_Tcell = avgTcell()
    
    filePath = '/Users/zhaoyingying/surfacesoiling/data/inverter/processed/S01-NBA.csv'
    df_org = pd.read_csv(filePath)
    
    startDTModel = '2016-01-01'
    endDTModel = '2017-03-26'
    timeRg = ['05:30', '19:30']  # use pandas to get data within this range
    
    # date list
    start = datetime.datetime.strptime(startDTModel, "%Y-%m-%d").date()
    end = datetime.datetime.strptime(endDTModel, "%Y-%m-%d").date()
    dateList = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

    dayList = []
    for day in dateList:
        dayList.append(str(day)) 
    
    numDays = len(dayList)
    print(dayList)
    CPRArray = np.zeros((numDays, 1))
    dailyinput = np.zeros((numDays, 1))

    for idx, day in enumerate(dateList):

        
        df = df_org[(df_org['data_date'] >= str(day) + ' ' + timeRg[0]) &
                        (df_org['data_date'] < str(day) + '' + timeRg[1])]
        
        df['fv'] = 17.1+ 5.7 * df['Wv']
        alphatau = 0.9
        ita = 0.1545
        beta = 0.0043
        Tr= 25
    
        df['Tcell'] = (df['fv'] * df['T0'] + df['Fs2m']*(alphatau - ita -beta*ita*Tr))  / (df['fv']-beta*ita*df['Fs2m'])
             
        df = df.drop(['data_date'], axis=1)
            # print('add columns')
        df['EN'] = df['I1m'] * df['V1m']/1000
        
        deta = -0.43
        Gstc = 1000 #w/m^2
        df['G_POA'] = df['Fs2m']
        Pstc = 300.0/1000.0
    
        df['input']= Pstc * ( df['G_POA']/Gstc) * (1- (deta/100) * (Avg_Tcell- df['Tcell']))

        
        #print('computing...', df.shape)
        if df.shape[0] >= 100:
            CPRArray[idx] = df['EN'].sum() / df['input'].sum()
            dailyinput[idx] = df['input'].sum()
    
    dailyCPR = pd.DataFrame(data=CPRArray, columns=['CPR'])
    dailyCPR['Date'] = pd.DataFrame(data=dayList)
 
    
        #remove outliers
    med_cpr, upper = tool.removeOutliers(dailyCPR.CPR, 1)
    #print(med_cpr)

    dailyCPR['CPR'] = med_cpr
    
    
    
    dailyCPR['dailyinput'] = dailyinput
    
    dailyCPR.to_csv('/Users/zhaoyingying/surfacesoiling/data/dailyCPR.csv', sep=',', header=True)
    print('Completed computing daily CPR')


if __name__ == "__main__":
    
    #alignNBQandQXZ()
    
    #getGPI(qxz_nqb)
    
    #getDailySolarRad()
    
    #avgTcell()
    
    dailyCPR()
    

    
    
    
    