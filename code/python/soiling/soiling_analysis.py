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
from scipy.signal import medfilt
from scipy import stats
from math import sqrt
invertnum = 74

powerPath = '/Users/zhaoyingying/surfacesoiling/data/results/siglepowers/S01-NBA.csv'
allpowerPath = '/Users/zhaoyingying/surfacesoiling/data/results/'
qxzclean = '/Users/zhaoyingying/surfacesoiling/data/qxzclean.csv'
figPath = '/Users/zhaoyingying/surfacesoiling/data/fig/'
qxjl = '/Users/zhaoyingying/surfacesoiling/data/qxjl.csv'
resPath = '/Users/zhaoyingying/surfacesoiling/data/inverter/processed/'
pmfile = '/Users/zhaoyingying/surfacesoiling/data/DezhouPM25.csv'
corPath = '/Users/zhaoyingying/surfacesoiling/data/cor/'
wsSlopePath ='/Users/zhaoyingying/surfacesoiling/data/inverter/slope/weatherstation/'


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
    
    #qxz_qx = qxz_qx[(qxz_qx['CleanDate'] >= str(dayList[0])) & (qxz_qx['CleanDate'] < str(dayList[-1]))]
    qxz_qx.set_index(['CleanDate'], inplace=True)
    
    df = pd.read_csv(powerPath)
    df['Date'] = pd.to_datetime(df['Date'],format='%Y-%m-%d')
    df.set_index(['Date'], inplace=True)
    df['Powerloss'] = (df['Pe_cleaning']-df['Pe_syn'])/df['Pe_cleaning'] 
    df['Powerloss'] = medfilt(df['Powerloss'], 7)
    df['avg_powerloss'] = df['Powerloss'].mean()
    print(df['Powerloss'].mean())



    plt.plot(df.index, df.Powerloss, label='MRE Power Loss')
    plt.plot(df.index, df.avg_powerloss, label='Daily MRE = 4.97%')
    

   # plt.plot(df.index, y1, label='7-day Med Filtered')

    # add clean record
    n_clean = [0.0] * qxz_qx.index.shape[0]

    plt.plot(qxz_qx.index, n_clean, 'x', label='Cleaning Event')
    plt.ylabel('MRE of Power Loss')
    plt.xlabel('Date')
    plt.legend(loc='upper right')
    plt.xticks(rotation=30)
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
    nbq_List = []
    invertPos = 5
    cleaningPanelPos = 6
    synPanelPos =7
    
    flist = glob.glob(corPath+'*.csv')        
    for idx, f in enumerate(flist):
        
        df = pd.read_csv(f)
        nbqName = os.path.basename(f)[0:7]
        
        #get the correlation of inverter and factors
        fs2m_list[idx] = df.at[invertPos,'Fs2m']
        sd_list[idx] = df.at[invertPos,'Sd']
        t0_list[idx] = df.at[invertPos,'T0']
        Wd_list[idx] = df.at[invertPos,'Wd']
        Wv_list[idx] = df.at[invertPos,'Wv']
        nbq_List.append(nbqName)
        
        #get the correlation in weather station
        if idx == (invertnum-1):
            
            # for the cleaning panel 
            fs2m_list[idx+1] = df.at[cleaningPanelPos,'Fs2m']
            sd_list[idx+1] = df.at[cleaningPanelPos,'Sd']
            t0_list[idx+1] = df.at[cleaningPanelPos,'T0']
            Wd_list[idx+1] = df.at[cleaningPanelPos,'Wd']
            Wv_list[idx+1] = df.at[cleaningPanelPos,'Wv']
            nbq_List.append('1cleaning Panel')
            
            #for the synchronized panel
            fs2m_list[idx+2] = df.at[synPanelPos,'Fs2m']
            sd_list[idx+2] = df.at[synPanelPos,'Sd']
            t0_list[idx+2] = df.at[synPanelPos,'T0']
            Wd_list[idx+2] = df.at[synPanelPos,'Wd']
            Wv_list[idx+2] = df.at[synPanelPos,'Wv']
            nbq_List.append('1Sync Panel')
    
     #merge in dataframe and sort         
    new_df = pd.DataFrame(data = nbq_List, columns=['nbqName'])
    new_df['nbqName'] = nbq_List
    new_df['Fs2m'] = fs2m_list
    new_df['Sd'] = sd_list
    new_df['T0'] = t0_list
    new_df['Wd'] = Wd_list
    new_df['Wv'] = Wv_list
    new_df = new_df.sort_values(by=['nbqName'])
    new_df.set_index(['nbqName'], inplace=True)
   
    
     
    #plot
    plt.plot(new_df.index,new_df['Fs2m'], linewidth=2, label='Solar Radiation')
#    plt.plot(new_df.index,new_df['Sd'], linewidth=2, label='Humidity')
#    plt.plot(new_df.index,new_df['T0'], linewidth=2, label='Ambient Temperature')
    plt.plot(new_df.index,new_df['Wd'], linewidth=2, label='Wind direction')
    plt.plot(new_df.index,new_df['Wv'], linewidth=2, label='Wind Speed')
    plt.xticks(rotation=90,fontsize=4)
    
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

def dailycorrelation():
    '''
    get the daily correlation of p_cln and p_syn of all other factors, such as temperature, humidity, wind speed, wind direction
    
    purpose: learn dust accumulation characteristics using weather station data
    
    '''
    
    #read weather stataion data for a random inverter
    wsdata = pd.read_csv(resPath + 'S01-NBB.csv').loc[:,['data_date','Fs2m','I1m','I2m','Sd','T0','V1m','Wd','Wv']]
    wsdata['P_cln'] = wsdata['I1m'] * wsdata['V1m']
    wsdata['P_syn'] = wsdata['I2m'] * wsdata['V1m']
    wsdata = wsdata.drop(['I1m'], axis=1)
    wsdata = wsdata.drop(['I2m'], axis=1)
    wsdata = wsdata.drop(['V1m'], axis=1)
    dateList = [item[0:10] for item in wsdata['data_date'].values] 
    wsdata['Date'] = dateList
    wsdata = wsdata.drop(['data_date'], axis=1)
    
    wsdata.set_index(['Date'], inplace=True)
    dateList = np.unique(dateList)
    
    #datafram to save daily corr
    col_Pcln = ['Fs2m_Pcln', 'Sd_Pcln', 'T0_Pcln', 'Wd_Pcln', 'Wv_Pcln']
    col_Psyn = ['Fs2m_Psyn', 'Sd_Psyn', 'T0_Psyn', 'Wd_Psyn', 'Wv_Psyn']
    col = ['Fs2m_Pcln', 'Sd_Pcln', 'T0_Pcln', 'Wd_Pcln', 'Wv_Pcln','Fs2m_Psyn', 'Sd_Psyn', 'T0_Psyn', 'Wd_Psyn', 'Wv_Psyn']
    corr = ['Fs2m','Sd','T0', 'Wd','Wv']
    
    dailyCorr = pd.DataFrame(index=dateList, columns=col)
    dailyCorr.index = pd.to_datetime(dailyCorr.index, format='%Y-%m-%d') 
    
    #analysis daily correlation
    for idx, item in enumerate(dateList):
        #daily data
        tmp_df = wsdata[wsdata.index == item]
        #daily correlation
        corr_df = tmp_df.corr()
        #for cleaning panel
        for jdx,jtem in enumerate(col_Pcln):
            dailyCorr.at[item,col_Pcln[jdx]] = corr_df.at['P_cln',corr[jdx]]
        #for sync panel
        for jdx,jtem in enumerate(col_Psyn):
            dailyCorr.at[item,col_Psyn[jdx]] = corr_df.at['P_syn',corr[jdx]]
    
    
    #remove outliers for each column and med filt
    for idx, item in enumerate(col):
        med, upper = tool.removeOutliers_raw(dailyCorr[item], 1)
        med = medfilt(med, 7)
        dailyCorr[item] = med
        


    
    #aligh with cleaning event
    qxz_qx = pd.read_csv(qxzclean)
    qxz_qx['CleanDate'] = pd.to_datetime(qxz_qx['CleanDate'], format='%Y-%m-%d')      
    qxz_qx.set_index(['CleanDate'], inplace=True)

    
    #plot
    col = ['Fs2m_Pcln', 'Sd_Pcln', 'T0_Pcln', 'Wd_Pcln', 'Wv_Pcln','Fs2m_Psyn', 'Sd_Psyn', 'T0_Psyn', 'Wd_Psyn', 'Wv_Psyn']
    plt.figure(1)
    plt.plot(dailyCorr.index, dailyCorr.Fs2m_Pcln, label='Fs2m_Pcln')
    plt.plot(dailyCorr.index, dailyCorr.Fs2m_Psyn, label='Fs2m_Psyn')
    n_clean = [0.0] * qxz_qx.index.shape[0]

    plt.plot(qxz_qx.index, n_clean, 'x', label='Cleaning Event')
    plt.ylabel('Correlation')
    plt.xlabel('Date')
    plt.legend()
    plt.ylim((-1, 1.25))
    plt.xticks(rotation=30)
    plt.savefig(figPath + 'qxzFs2mCorr.png', dpi=300)
    
    plt.figure(2)
    plt.plot(dailyCorr.index, dailyCorr.T0_Pcln, label='T0_Pcln')
    plt.plot(dailyCorr.index, dailyCorr.T0_Psyn, label='T0_Psyn')
    n_clean = [0.0] * qxz_qx.index.shape[0]

    plt.plot(qxz_qx.index, n_clean, 'x', label='Cleaning Event')
    plt.ylabel('Correlation')
    plt.xlabel('Date')
    plt.legend()
    plt.ylim((-1, 1))
    plt.xticks(rotation=30)
    plt.savefig(figPath + 'qxzT0Corr.png', dpi=300)

    plt.figure(3)
    plt.plot(dailyCorr.index, dailyCorr.Sd_Pcln, label='Sd_Pcln')
    plt.plot(dailyCorr.index, dailyCorr.Sd_Psyn, label='Sd_Psyn')
    n_clean = [0.0] * qxz_qx.index.shape[0]

    plt.plot(qxz_qx.index, n_clean, 'x', label='Cleaning Event')
    plt.ylabel('Correlation')
    plt.xlabel('Date')
    plt.legend()
    plt.ylim((-1, 1))
    plt.xticks(rotation=30)
    plt.savefig(figPath + 'qxzSd2mCorr.png', dpi=300)
    
    plt.figure(4)
    plt.plot(dailyCorr.index, dailyCorr.Wv_Pcln, label='Wv_Pcln')
    plt.plot(dailyCorr.index, dailyCorr.Wv_Psyn, label='Wv_Psyn')
    
    n_clean = [0.0] * qxz_qx.index.shape[0]

    plt.plot(qxz_qx.index, n_clean, 'x', label='Cleaning Event')
    plt.ylabel('Correlation')
    plt.xlabel('Date')
    plt.legend()
    plt.ylim((-1, 1))
    plt.xticks(rotation=30)
    plt.savefig(figPath + 'qxzWvCorr.png', dpi=300)
    
    plt.figure(5)
    plt.plot(dailyCorr.index, dailyCorr.Wd_Pcln, label='Wd_Pcln')
    plt.plot(dailyCorr.index, dailyCorr.Wd_Psyn, label='Wd_Psyn')
    n_clean = [1.0] * qxz_qx.index.shape[0]

    plt.plot(qxz_qx.index, n_clean, 'x', label='Cleaning Event')
    plt.ylabel('Correlation')
    plt.xlabel('Date')
    plt.legend()
    plt.ylim((-1, 1))
    plt.xticks(rotation=30)
    plt.savefig(figPath + 'qxzWdCorr.png', dpi=300)
    
    
    
    


    plt.show()
        
 
def alignSlopeCleanqxz():
    '''
    align slopes (cleaning panel and sync panel) with the cleaning records in qixiangzhan
    
    the temporal characteristics of dust accumulation
    
    '''
    qxz_qx = pd.read_csv(qxzclean)
    qxz_qx['CleanDate'] = pd.to_datetime(qxz_qx['CleanDate'], format='%Y-%m-%d')   
    
    #qxz_qx = qxz_qx[(qxz_qx['CleanDate'] >= str(dayList[0])) & (qxz_qx['CleanDate'] < str(dayList[-1]))]
    qxz_qx.set_index(['CleanDate'], inplace=True)
    
    df_cln = pd.read_csv(wsSlopePath+'P_clnslope_ransac.csv')
    df_syn = pd.read_csv(wsSlopePath+'P_synslope_ransac.csv')
    
    df_cln['Date'] = pd.to_datetime(df_cln['data_date'],format='%Y-%m-%d')
    df_cln.set_index(['Date'], inplace=True)
    
    df_syn['Date'] = pd.to_datetime(df_syn['data_date'],format='%Y-%m-%d')
    df_syn.set_index(['Date'], inplace=True)
    
    #normalized slope
    #df_syn['Pr'] = (df_syn['Pr'] - df_syn['Pr'].min()) / (df_syn['Pr'].max() - df_syn['Pr'].min())
   # df_cln['Pr'] = (df_cln['Pr'] - df_cln['Pr'].min()) / (df_cln['Pr'].max() - df_cln['Pr'].min())
    df_syn['Pr'],upper_quartile = tool.removeOutliers_raw(df_syn['Pr'],1)
    df_cln['Pr'],upper_quartile = tool.removeOutliers_raw(df_cln['Pr'],1)
    
    df_syn['Pr'] = medfilt(df_syn['Pr'], 5)
    df_cln['Pr'] = medfilt(df_cln['Pr'],5)



    plt.plot(df_syn.index, df_syn.Pr, label='Slope of Synchronized PV Panel')
    plt.plot(df_cln.index, df_cln.Pr, label='Slope of daily clean PV Panel')
    
    # add clean record
    n_clean = [0.37] * qxz_qx.index.shape[0]

    plt.plot(qxz_qx.index, n_clean, 'x', label='Cleaning Event')
    plt.ylabel('Slope')
    plt.xlabel('Date')
    plt.legend()
    plt.ylim((0.3,0.5))
    plt.xticks(rotation=30)
    plt.savefig(figPath + 'qxzSlope.png', dpi=300)
    plt.show()

def effectsize():
    '''
    get the effect size  of power of all other factors, such as temperature, humidity, wind speed, wind direction
    
    '''
    nbqList = tool.getnbqList()
    
    #pvalues list for 74 inverters and two panels in weather satation
    
    fs2m_es = np.zeros((invertnum+2, 1))
    sd_es = np.zeros((invertnum+2, 1))
    t0_es = np.zeros((invertnum+2, 1))
    Wd_es = np.zeros((invertnum+2, 1))
    Wv_es = np.zeros((invertnum+2, 1))
    es =[fs2m_es,sd_es,t0_es,Wd_es,Wv_es]
    nbq_List = []

    #for all inverters
    for idx, nbqID in enumerate(nbqList):
        print(idx, nbqID)
        nbq_List.append(nbqID)
        nbqData = pd.read_csv(resPath + nbqID + '.csv').loc[:,['I','data_date','V','Fs2m','I1m','I2m','Sd','T0','V1m','Wd','Wv']]
        nbqData.fillna(method='ffill')

        nbqSample = nbqData
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
        #normalization
        nbqSample.iloc[:,:] = nbqSample.iloc[:,:].apply(lambda x:(x-np.min(x))/(np.max(x)-np.min(x)))
        
        #factors 
        factors= ['Fs2m','Sd','T0','Wd','Wv']

        for jdx, jtem in enumerate(factors):
            #slope, intercept, r_value, p_value, std_err = stats.linregress(nbqSample[jtem], nbqSample.P)
            #pvalues[jdx][idx] = "%.2f" %p_value
            cohens_d = abs(nbqSample[jtem].mean() - nbqSample.P.mean()) / (sqrt((nbqSample[jtem].std() ** 2 + nbqSample.P.std() ** 2) / 2))
            es[jdx][idx] = "%.2f" %cohens_d
            
    #get the effect size in weather station
    print(idx)
    # for the cleaning panel 
    for jdx, jtem in enumerate(factors):
        cohens_d = abs(nbqSample[jtem].mean() - nbqSample.P_cln.mean()) / (sqrt((nbqSample[jtem].std() ** 2 + nbqSample.P_cln.std() ** 2) / 2))
        es[jdx][idx+1] = "%.2f" %cohens_d
    nbq_List.append('1cleaning Panel')
    # for the sync panel 
    for jdx, jtem in enumerate(factors):
        cohens_d = abs(nbqSample[jtem].mean() - nbqSample.P_syn.mean()) / (sqrt((nbqSample[jtem].std() ** 2 + nbqSample.P_syn.std() ** 2) / 2))
        es[jdx][idx+2] = "%.2f" %cohens_d
    nbq_List.append('1sync Panel')
            
    #merge in dataframe and sort         
    new_df = pd.DataFrame(data = nbq_List, columns=['nbqName'])
    print(len(nbq_List))
    print(len(fs2m_es))
    new_df['nbqName'] = nbq_List
    new_df['Fs2m'] = fs2m_es
    new_df['Sd'] = sd_es
    new_df['T0'] = t0_es
    new_df['Wd'] = Wd_es
    new_df['Wv'] = Wv_es
    new_df['boudary'] = new_df['Wv']*0.0+0.2
    new_df = new_df.sort_values(by=['nbqName'])
    new_df.set_index(['nbqName'], inplace=True)

    #plot
    plt.plot(new_df.index,new_df['Fs2m'], linewidth=2, label='Solar Radiation')
    plt.plot(new_df.index,new_df['Sd'], linewidth=2, label='Humidity')
    plt.plot(new_df.index,new_df['T0'], linewidth=2, label='Ambient Temperature')
    plt.plot(new_df.index,new_df['Wd'], linewidth=2, label='Wind Direction')
    plt.plot(new_df.index,new_df['Wv'], linewidth=2, label='Wind Speed')
    plt.plot(new_df.index,new_df['boudary'], linewidth=2, label='Small (.2)')
    
    plt.ylabel('Effect Size with Power Output')
    plt.xlabel('No. of Inverters')
    plt.subplots_adjust(left=0.18, wspace=0.25, hspace=0.25,bottom=0.20, top=0.80)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
    plt.xticks(rotation=90,fontsize=4)
    plt.savefig(figPath + 'es.png', dpi=300)
    
    plt.show()

def pvalues():
    '''
    get the pvalues of power of all other factors, such as temperature, humidity, wind speed, wind direction
    
    '''
    nbqList = tool.getnbqList()
    
    #pvalues list for 74 inverters and two panels in weather satation
    
    fs2m_es = np.zeros((invertnum+2, 1))
    sd_es = np.zeros((invertnum+2, 1))
    t0_es = np.zeros((invertnum+2, 1))
    Wd_es = np.zeros((invertnum+2, 1))
    Wv_es = np.zeros((invertnum+2, 1))
    es =[fs2m_es,sd_es,t0_es,Wd_es,Wv_es]
    nbq_List = []

    #for all inverters
    for idx, nbqID in enumerate(nbqList):
        print(idx, nbqID)
        nbq_List.append(nbqID)
        nbqData = pd.read_csv(resPath + nbqID + '.csv').loc[:,['I','data_date','V','Fs2m','I1m','I2m','Sd','T0','V1m','Wd','Wv']]
        nbqData.fillna(method='ffill')

        nbqSample = nbqData
        dateList = [item[0:10] for item in nbqSample['data_date'].values] 
        nbqSample['Date'] = dateList
        nbqSample.set_index(['Date'], inplace=True)
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
        #normalization
        #nbqSample.iloc[:,:] = nbqSample.iloc[:,:].apply(lambda x:(x-np.min(x))/(np.max(x)-np.min(x)))
        
        #factors 
        factors= ['Fs2m','Sd','T0','Wd','Wv']
        Fs2m=[]
        Sd=[]
        T0=[]
        Wd=[]
        Wv=[]
        pvalues = [Fs2m,Sd,T0,Wd,Wv]
        #analysis daily pvalues
        dateList = np.unique(dateList)
        for zdx, item in enumerate(dateList):
            #get daily data
            tmp_df = nbqSample[nbqSample.index == item]
            #get daily pvalues
            for jdx, jtem in enumerate(factors):
                slope, intercept, r_value, p_value, std_err = stats.linregress(tmp_df[jtem], tmp_df.P)
                pvalues[jdx].append(p_value)
        #mean daily
        for i,item in enumerate(es):
            es[i][idx] = np.mean(pvalues[i])

        #cal pvalues for weather station  
        if idx == (invertnum-1):
            # for the cleaning panel 
            for jdx, jtem in enumerate(factors):
                slope, intercept, r_value, p_value, std_err = stats.linregress(tmp_df[jtem], tmp_df.P_cln)
                es[jdx][idx+1] = p_value
            nbq_List.append('1cleaning Panel')
            # for the sync panel 
            for jdx, jtem in enumerate(factors):
                slope, intercept, r_value, p_value, std_err = stats.linregress(tmp_df[jtem], tmp_df.P_syn)
                es[jdx][idx+2] = p_value
            nbq_List.append('1sync Panel')
            
    #merge in dataframe and sort         
    new_df = pd.DataFrame(data = nbq_List, columns=['nbqName'])
    new_df['nbqName'] = nbq_List
    new_df['Fs2m'] = fs2m_es
    new_df['Sd'] = sd_es
    new_df['T0'] = t0_es
    new_df['Wd'] = Wd_es
    new_df['Wv'] = Wv_es
    new_df['ls'] = new_df.Wv*0.0+0.05
    new_df = new_df.sort_values(by=['nbqName'])
    new_df.set_index(['nbqName'], inplace=True)

    #fill nan
    new_df.fillna(method ='ffill',inplace=True)
    new_df.fillna(method = 'backfill',inplace=True)
    print(new_df)
    #plot
    
    plt.plot(new_df.index,new_df['Fs2m'], linewidth=2, label='Solar Radiation')
    plt.plot(new_df.index,new_df['Sd'], linewidth=2, label='Humidity')
    plt.plot(new_df.index,new_df['T0'], linewidth=2, label='Ambient Temperature')
    plt.plot(new_df.index,new_df['Wd'], linewidth=2, label='Wind Direction')
    plt.plot(new_df.index,new_df['Wv'], linewidth=2, label='Wind Speed')
    plt.plot(new_df.index,new_df['ls'], linewidth=2, label='Significance ( .05)')
    
    plt.ylabel('Daily p-values')
    plt.xlabel('No. of Inverters')
    plt.subplots_adjust(left=0.18, wspace=0.25, hspace=0.25,bottom=0.20, top=0.80)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
    plt.xticks(rotation=90,fontsize=4)
    plt.savefig(figPath + 'pvalues.png', dpi=300)
    
    plt.show()
    
       

        
 
if __name__ == "__main__":
    #soilingVar()
    #alignCleanqxz()
    #correlation()
    #analyzeCor()
    #correlationPM25()
    
    #dailycorrelation()
   #alignSlopeCleanqxz()
   effectsize()
   #pvalues()
