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
import xlrd
import matplotlib.pyplot as plt
import matplotlib as mpl
from windrose import WindroseAxes
import matplotlib.cm as cm



qxjl = '/Users/zhaoyingying/surfacesoiling/data/qxjl.csv'
qxzclean = '/Users/zhaoyingying/surfacesoiling/data/qxzclean.csv'
allnbqData = '/Users/zhaoyingying/surfacesoiling/data/Inv_GPI_pingyuan.csv'
qxz = '/Users/zhaoyingying/surfacesoiling/data/pingyuan_weather_station2016.csv'
qxz_nqb = '/Users/zhaoyingying/surfacesoiling/data/qxz_nqb.csv'
figPath = '/Users/zhaoyingying/surfacesoiling/data/fig/'
cleanlistPath = '/Users/zhaoyingying/surfacesoiling/data/cleaninglist.csv'
wscleanlistPath = '/Users/zhaoyingying/surfacesoiling/data/wscleaninglist.csv'

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

        if df.shape[0] >= 100:
            CPRArray[idx] = df['EN'].sum() / df['input'].sum()
            dailyinput[idx] = df['input'].sum()
    
    dailyCPR = pd.DataFrame(data=CPRArray, columns=['CPR'])
    dailyCPR['Date'] = pd.DataFrame(data=dayList)

        #remove outliers
    med_cpr, upper = tool.removeOutliers(dailyCPR.CPR, 1)
    dailyCPR['CPR'] = med_cpr  
    dailyCPR['dailyinput'] = dailyinput
    
    dailyCPR.to_csv('/Users/zhaoyingying/surfacesoiling/data/dailyCPR.csv', sep=',', header=True)
    print('Completed computing daily CPR')


def new_axes():
    fig = plt.figure(figsize=(4, 4), dpi=80, facecolor='w', edgecolor='w')
    rect = [0, 0, 1, 1]
    ax = WindroseAxes(fig, rect, axisbg='w')
    fig.add_axes(ax)
    return ax
#...and adjust the legend box
def set_legend(ax):
    l = ax.legend(shadow=False, bbox_to_anchor=[1, 0])
    plt.setp(l.get_texts(), fontsize=12)


def windRose():
    '''
    plot wind rose for pingyuan site in 2016
    '''
    filePath = '/Users/zhaoyingying/surfacesoiling/data/inverter/processed/S01-NBA.csv'

    numDays = len(dayList)
    print('there are '+str(numDays)+' days in total.')
    df_org = pd.read_csv(filePath)
    df = df_org[(df_org['data_date'] >= str(dateList[0]) + ' ' + timeRg[0]) &
                        (df_org['data_date'] < str(dateList[-1]) + '' + timeRg[1])]
    df = df.loc[:,['Wv','Wd']]
    tool.windrose(df, dirn='Wd', speed='Wv', loc_0 = 'N', loc_90='E')
    tool.windrose_cbar()

def boxplot(field):
    '''
    plot monthly box figure for solar radiation, hd, t0 in pingyuan site in 2016
    '''
    filePath = '/Users/zhaoyingying/surfacesoiling/data/inverter/processed/S01-NBA.csv'

    numDays = len(dayList)
    print('there are '+str(numDays)+' days in total.')
    df_org = pd.read_csv(filePath)
    df = df_org[(df_org['data_date'] >= str(dateList[0]) + ' ' + timeRg[0]) &
                        (df_org['data_date'] < str(dateList[-1]) + '' + timeRg[1])]
    
    df = df.loc[:,['data_date','Fs2m','T0','Sd','Wv','Wd','I1m','V1m','I2m']]
    
    #monthly
    datelist = [item[0:7] for item in df['data_date'].values]
    df['Date']= datelist
    df['P_cln'] = df['I1m']*df['V1m']
    df['P_syn'] = df['I2m']*df['V1m']
    
    del df['data_date']
    
    new_df = df.pivot(columns='Date', values=field)

#    #boxplot   
    new_df.boxplot(sym='r*',patch_artist=True)       
    plt.xlabel('Month')
    plt.xticks(rotation=30)
    #plt.ylabel('Humidity')
    #plt.ylabel('Ambient Temperature (℃)')
    #plt.ylabel('Solar Radiation (W/m^2)')
    #plt.ylabel('Wind Speed (m/s)')
    #plt.ylabel('Wind Direction')
    plt.ylabel('Power of Synchronized PV Panel')
    plt.subplots_adjust(left=0.18, wspace=0.25, hspace=0.25,bottom=0.20, top=0.91)

    #plt.savefig(figPath + 'Fs2mMonthlyVar.png', dpi=300)
   # plt.savefig(figPath + 'WdMonthlyVar.png', dpi=300)
    plt.ylim((0,400))
    plt.savefig(figPath + 'PsynMonthlyVar.png', dpi=300)
    
    plt.show()

def cleaninglist(outPath):
    '''
    get cleaning list for each inverter
    the number day of dust accumulation
    
    '''
    #get date list
    dayList = tool.getDayList()
    
    #get cleaning list for each inverter
    nbqList = tool.getnbqList()
    
    df = pd.DataFrame(columns=nbqList)
    df['Date'] = dayList
    
    for idx, nbqname in enumerate(nbqList):
        #get cleaning record
        nbq_qx = pd.read_csv(qxjl)
        #find the inverter
        nbq_qx = nbq_qx[nbq_qx['nbqno'] == nbqname]  # reorganize code and make a flow
     
        
        #get cleaning list for the invert
        cleaningList = [item[0:10] for item in nbq_qx['qxdate'].values]
        
        
        startIDX = 0
        #calculate the number of dust accumulation
        for jdx, riqi in enumerate(cleaningList):
            
            #get end index
            endIDX = df[df.Date == riqi].index.tolist()[0]
            
            if (endIDX -startIDX) < 50: #set experience value, 
                dustacclist = range(0, endIDX-startIDX+1)
                df.loc[startIDX:endIDX,nbqname] = dustacclist 
            else:  # it is impossible that the dust accumulation interval is larger than 50 days. in pingyuan site
                dustacclist = [0]*( endIDX-startIDX+1)
                df.loc[startIDX:endIDX,nbqname] = dustacclist         
                
            #next cleaning event
            startIDX = endIDX
            #startDate = riqi
        
        
        #for the last cleaning record
        endIDX = len(dayList)-1
        dustacclist = range(0, endIDX-startIDX+1)
        df.loc[startIDX:endIDX,nbqname] = dustacclist       
    df.to_csv(outPath)

def wscleaninglist(outPath):
    '''
    get cleaning list for weather station
    the number day of dust accumulation
    
    '''
    #get date list
    dayList = tool.getDayList()
    
    #get cleaning list for each inverter
    nbqList = ['syn']
    nbqname = 'syn'
    
    df = pd.DataFrame(columns=nbqList)
    df['Date'] = dayList
    

        #get cleaning record
    nbq_qx = pd.read_csv(qxzclean)
     
        
        #get cleaning list for the invert
    cleaningList = [item[0:10] for item in nbq_qx['CleanDate'].values]
        
        
    startIDX = 0
        #calculate the number of dust accumulation
    for jdx, riqi in enumerate(cleaningList):
            
            #get end index
        endIDX = df[df.Date == riqi].index.tolist()[0]
            
        if (endIDX -startIDX) < 50: #set experience value, 
            dustacclist = range(0, endIDX-startIDX+1)
            df.loc[startIDX:endIDX,nbqname] = dustacclist 
        else:  # it is impossible that the dust accumulation interval is larger than 50 days. in pingyuan site
            dustacclist = [0]*( endIDX-startIDX+1)
            df.loc[startIDX:endIDX,nbqname] = dustacclist         
                
            #next cleaning event
        startIDX = endIDX
            #startDate = riqi
        
        
        #for the last cleaning record
    endIDX = len(dayList)-1
    dustacclist = range(0, endIDX-startIDX+1)
    df.loc[startIDX:endIDX,nbqname] = dustacclist       
    df.to_csv(outPath)        
    
if __name__ == "__main__":
    
    #alignNBQandQXZ()
    
    #getGPI(qxz_nqb)
    
    #getDailySolarRad()
    
    #avgTcell()
    
    #dailyCPR()
    
    #windRose()
    
   # boxplot(field = 'Fs2m')
   #boxplot(field = 'Wd')
   #boxplot(field = 'P_cln')
   #boxplot(field = 'P_syn')
   
   #get cleaning list for each inverter
   #cleaninglist(cleanlistPath)
   wscleaninglist(wscleanlistPath)
    

    
    
    
    