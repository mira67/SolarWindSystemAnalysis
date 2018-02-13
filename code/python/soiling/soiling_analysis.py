#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 10:33:15 2018

@author: zhaoyingying
"""
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import tool
import numpy as np
import glob
import os
invertnum = 74

powerPath = '/Users/zhaoyingying/surfacesoiling/data/results/S01-NBA.csv'
allpowerPath = '/Users/zhaoyingying/surfacesoiling/data/results/'
qxzclean = '/Users/zhaoyingying/surfacesoiling/data/qxzclean.csv'
figPath = '/Users/zhaoyingying/surfacesoiling/data/fig/'
qxjl = '/Users/zhaoyingying/surfacesoiling/data/qxjl.csv'
resPath = '/Users/zhaoyingying/surfacesoiling/data/inverter/processed/'
pmfile = '/Users/zhaoyingying/surfacesoiling/data/DezhouPM25.csv'
corPath = '/Users/zhaoyingying/surfacesoiling/data/cor/'


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
    
    
def soilingVar():
    
    '''
    analyzing daily soiling variation in qixiangzhan

    '''
    df = pd.read_csv(powerPath).loc[:,['Date','Pe_syn','Pe_cleaning']]
    df['Powerloss'] = (df['Pe_cleaning']-df['Pe_syn'])/df['Pe_cleaning'] 
    
            #plot
    print('start to plot...')
    plt.plot( df.Date,df.Powerloss,label='Power Loss')
        
    plt.xlabel('Date')
    plt.ylabel('Relative Power Loss')
    plt.legend()
    
    plt.show()
        
    plt.close()

def alignCleanqxz():
    '''
    align with the cleaning records in qixiangzhan
    
    the temporal characteristics of dust accumulation
    
    '''
    qxz_qx = pd.read_csv(qxzclean)
    qxz_qx['CleanDate'] = pd.to_datetime(qxz_qx['CleanDate'], format='%Y-%m-%d')   
    
    qxz_qx = qxz_qx[(qxz_qx['CleanDate'] >= str(dayList[0])) & (qxz_qx['CleanDate'] < str(dayList[-1]))]
    qxz_qx.set_index(['CleanDate'], inplace=True)
    
    df = pd.read_csv(powerPath)
    df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d')
    df.set_index(['Date'], inplace=True)
    df['Powerloss'] = (df['Pe_cleaning']-df['Pe_syn'])/df['Pe_cleaning'] 
    df['avg_powerloss'] = df['Powerloss'].mean()
    print(df['Powerloss'].mean())



    plt.plot(df.index, df.Powerloss, label='Relative Power Loss')
    plt.plot(df.index, df.avg_powerloss, label='Mean Relative Power Loss = 5.7%')
    

   # plt.plot(df.index, y1, label='7-day Med Filtered')

    # add clean record
    n_clean = [0.0] * qxz_qx.index.shape[0]

    plt.plot(qxz_qx.index, n_clean, 'x', label='Clean Event')
    plt.ylabel('Relative Power Loss')
    plt.xlabel('Date')
    plt.legend(loc='upper left')
    plt.savefig(figPath + 'qxzCleaning.png', dpi=300)
    plt.show()

def correlation():
    '''
    get the correlation of power of all other factors, such as temperature, humidity, wind speed, wind direction
    
    '''
    nbqList = tool.getnbqList()
    # hlxList = map(str, hlxList)

    for idx, nbqID in enumerate(nbqList):
        print(idx, nbqID)
        nbqData = pd.read_csv(resPath + nbqID + '.csv').loc[:,['I','data_date','V','Fs2m','I1m','I2m','Sd','T0','V1m','Wd','Wv']]
        nbqData.fillna(method='ffill')
    

        # downsample for quick plot
        nbqSample = nbqData.sample(n=2000, replace='False')
        nbqSample = nbqSample.drop(['data_date'], axis=1)
        nbqSample['P'] = nbqSample['I'] * nbqSample['V']
        nbqSample['P_cln'] = nbqSample['I1m'] * nbqSample['V1m']
        nbqSample['P_syn'] = nbqSample['I2m'] * nbqSample['V1m']
        nbqSample = nbqSample.drop(['I1m'], axis=1)
        nbqSample = nbqSample.drop(['I2m'], axis=1)
        nbqSample = nbqSample.drop(['V1m'], axis=1)
        nbqSample = nbqSample.drop(['I'], axis=1)
        nbqSample = nbqSample.drop(['V'], axis=1)
        nbqSample.fillna(method = 'backfill')
        nbqSample.fillna(0)
        
        
        nbqSample.corr().to_csv(corPath+nbqID+'.csv')


        # plot
#        nbqSample = nbqSample.astype(np.float32)  # must convert to float32 before scatter
#        tool.nbqPlot(nbqSample, nbqID)

def analyzeCor():
    '''
    Analyzing the correlation for each inverter
    
    '''
    #correlation list for 74 inverters and two panels in weather satation
    fs2m_list = np.zeros((invertnum+2, 1))
    sd_list = np.zeros((invertnum+2, 1))
    t0_list = np.zeros((invertnum+2, 1))
    Wd_list = np.zeros((invertnum+2, 1))
    Wv_list = np.zeros((invertnum+2, 1))
    invertPos = 5
    cleaningPanelPos = 6
    synPanelPos =7
    
    flist = glob.glob(corPath+'*.csv')        
    for idx, f in enumerate(flist):
        df = pd.read_csv(f)
        
        #get the correlation of inverter and factors
        fs2m_list[idx] = df.at[invertPos,'Fs2m']
        sd_list[idx] = df.at[invertPos,'Sd']
        t0_list[idx] = df.at[invertPos,'T0']
        Wd_list[idx] = df.at[invertPos,'Wd']
        Wv_list[idx] = df.at[invertPos,'Wv']
        
        #get the correlation in weather station
        if idx == (invertnum-1):
            
            # for the cleaning panel 
            fs2m_list[idx+1] = df.at[cleaningPanelPos,'Fs2m']
            sd_list[idx+1] = df.at[cleaningPanelPos,'Sd']
            t0_list[idx+1] = df.at[cleaningPanelPos,'T0']
            Wd_list[idx+1] = df.at[cleaningPanelPos,'Wd']
            Wv_list[idx+1] = df.at[cleaningPanelPos,'Wv']
            
            #for the synchronized panel
            fs2m_list[idx+2] = df.at[synPanelPos,'Fs2m']
            sd_list[idx+2] = df.at[synPanelPos,'Sd']
            t0_list[idx+2] = df.at[synPanelPos,'T0']
            Wd_list[idx+2] = df.at[synPanelPos,'Wd']
            Wv_list[idx+2] = df.at[synPanelPos,'Wv']
     
    #plot
    plt.plot(fs2m_list, linewidth=2, label='Solar Radiation')
    plt.plot(sd_list, linewidth=2, label='Humidity')
    plt.plot(t0_list, linewidth=2, label='Ambient Temperature')
    plt.plot(Wd_list, linewidth=2, label='Wind direction')
    plt.plot(Wv_list, linewidth=2, label='Wind Speed')
    
    # plt.legend()
    plt.xlabel('Power of Inverters and Weather Station')
    plt.ylabel('Correlation')
    plt.subplots_adjust(left=0.18, wspace=0.25, hspace=0.25,bottom=0.20, top=0.80)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
    plt.savefig(figPath  + 'Totalcorrelation.png', dpi=300)
    plt.show()
    
            
def correlationPM25():
    '''
    get the correlation of power of  pm2.5
    
    '''
    #get pm2.5 data
    pm25_df = pd.read_csv(pmfile).loc[:,['Date','PM2.5','PM10']]
    nbqList = tool.getnbqList()

    for idx, nbqID in enumerate(nbqList):
        print(idx, nbqID)
        nbqData = pd.read_csv(allpowerPath + nbqID+'.csv').loc[:,['Date','P_true']]
        
        merged = pd.merge(pm25_df, nbqData)
        print(merged)

        print( merged.corr())


        # plot
#        nbqSample = nbqSample.astype(np.float32)  # must convert to float32 before scatter
#        tool.nbqPlot(nbqSample, nbqID)        
    
    
if __name__ == "__main__":
    #soilingVar()
    #alignCleanqxz()
    #correlation()
    analyzeCor()
    #correlationPM25()