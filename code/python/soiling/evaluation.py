#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:14:39 2018

@author: zhaoyingying
"""
import datetime
import pandas as pd
import tool
import math
import glob
import numpy as np
import matplotlib.pyplot as plt
import os

invertPath= '/Users/zhaoyingying/surfacesoiling/data/inverter/processed/'
singleslopePath = '/Users/zhaoyingying/surfacesoiling/data/inverter/slope/singleransac/'
multislopePath = '/Users/zhaoyingying/surfacesoiling/data/inverter/slope/multiransac/'
siglepowers = '/Users/zhaoyingying/surfacesoiling/data/results/siglepowers/'
cprPath = '/Users/zhaoyingying/surfacesoiling/data/dailyCPR.csv'
figPath = '/Users/zhaoyingying/surfacesoiling/data/fig/'
mrePath = '/Users/zhaoyingying/surfacesoiling/data/results/mre/mre.csv'
multiPowers = '/Users/zhaoyingying/surfacesoiling/data/results/multipowers/'
cleanlistPath = '/Users/zhaoyingying/surfacesoiling/data/cleaninglist.csv'
wscleanlistPath = '/Users/zhaoyingying/surfacesoiling/data/wscleaninglist.csv'
wsSlopePath ='/Users/zhaoyingying/surfacesoiling/data/inverter/slope/weatherstation/'

panelNum = 16
invertnum = 74

def MRE(powerPath,method):
    '''
    get power's mean relative error of true power and estimatied powers by different methods: gpi, cpr, weather-station
    '''
    MRE_syn = np.zeros((invertnum, 1))
    MRE_cpr = np.zeros((invertnum, 1))
    MRE_slope = np.zeros((invertnum, 1))
    nbq_List = []
    
    
    flist = glob.glob(powerPath+'*.csv')        
    for idx,f in enumerate(flist):
        nbqName = os.path.basename(f)[0:7]
        df_org = pd.read_csv(f).loc[:,['P_true','Pe_syn','Pe_cpr','Pe_slope']]
        
        #get mre for the syn panel
        df_org['MRE_syn'] = abs(df_org['P_true']-df_org['Pe_syn'])/df_org['P_true']  
        #get mre for the cpr panel
        df_org['MRE_cpr'] = abs(df_org['P_true']-df_org['Pe_cpr'])/df_org['P_true']
        #get mre for the syn panel
        df_org['MRE_slope'] = abs(df_org['P_true']-df_org['Pe_slope'])/df_org['P_true']  
        
        
        #print(df_org)

        #reove outliers
        df = df_org[ (df_org['MRE_syn']<0.5) & (df_org['MRE_cpr']<0.5) & (df_org['MRE_slope']<0.5)]
        
        #print(df)
        
        MRE_syn[idx] = df['MRE_syn'].mean()
        MRE_cpr[idx] = df['MRE_cpr'].mean()
        MRE_slope[idx] = df['MRE_slope'].mean()
        nbq_List.append(nbqName)
        
    MRE_df = pd.DataFrame(data=MRE_syn, columns=['MRE_syn'])
    MRE_df['MRE_cpr']= MRE_cpr
    MRE_df['MRE_slope']= MRE_slope
    MRE_df['nbqName'] = nbq_List
    MRE_df = MRE_df.sort_values(by=['nbqName'])
    MRE_df.set_index(['nbqName'], inplace=True)
    print(MRE_df['MRE_slope'].min())
    print(MRE_df['MRE_slope'].max())
    
    MRE_df.to_csv(mrePath)

    
    #print(MRE_df)
        
        #plot
    plt.plot(MRE_df.index,MRE_df['MRE_syn'],label='MRE_syn')
    plt.plot(MRE_df.index,MRE_df['MRE_cpr'],label='MRE_cpr')
    plt.plot(MRE_df.index,MRE_df['MRE_slope'],label='MRE_slope')
        
    plt.xlabel('No. of inverter')
    plt.ylabel('Mean Relative Error')
    plt.legend()
    plt.xticks(rotation=90,fontsize=4)


        
    plt.savefig(figPath + method+'mre.png', dpi=300)
    plt.show() 
        
    plt.close()
        
        
    
def getpowers(outPath,invertname):
    '''
    get powers from differnt methods for an invert  affected by irradiance

    '''
    # get powers from weather satation methods, it is the same for all inverters
    filePath = '/Users/zhaoyingying/surfacesoiling/data/inverter/processed/S01-NBA.csv'
    df = pd.read_csv(filePath)
    df.fillna(method='ffill')
    
    #convert datetime to date: 
    
    dateList = [item[0:10] for item in df['data_date'].values]  
    df['Date'] = dateList
    df['Pe_cleaning'] = df['I1m'] * df['V1m']
    df['Pe_syn'] = df['I2m'] * df['V1m']
    sum_df = df.groupby(['Date']).sum()
    avg_df = df.groupby(['Date']).mean()

    #get daily factors    
    df =sum_df.loc[:,['Fs2m','Pe_cleaning','Pe_syn']]
    df['Sd'] = avg_df['Sd']
    df['Wv'] = avg_df['Wv']
    df['Wd'] = avg_df['Wd']
    df['T0'] = avg_df['T0']
    print('get estimated power from weather satation data sucessfully!')
    
    
    #get the true power for the  inverter 
    file = tool.getnbqFile(invertPath,invertname)
    invert_df = pd.read_csv(file)
    invert_df.fillna(method='ffill')
        #convert datetime to date: 
    
    dateList = [item[0:10] for item in invert_df['data_date'].values]
    invert_df['Date'] = dateList
    invert_df['P_true'] = invert_df['I'] * invert_df['V']
    invert_df = invert_df.groupby(['Date']).sum()
    invert_df =invert_df.loc[:,['P_true']]
    
    #get string number for the inverter
    nbqinfo = pd.read_csv('/Users/zhaoyingying/surfacesoiling/data/nbqinfo.csv').loc[:,['nbqno','cuan','rongliang']]
    index = nbqinfo[nbqinfo.nbqno==invertname].index.tolist()[0]
    cuanNum = nbqinfo.at[index,'cuan']
    rongliang = nbqinfo.at[index,'rongliang']
    print('the string num for the inverer is : '+str(cuanNum))
    
    #re-obtain the true power of the inver
    merged = pd.merge(invert_df, df,left_index=True, right_index=True, how='inner')
    merged['Pe_cleaning']= merged['Pe_cleaning']*cuanNum*panelNum
    merged['Pe_syn']= merged['Pe_syn']*cuanNum*panelNum
    merged['capacity']= rongliang*1000
    
    #get powerestimation from cpr
    dustRate = tool.soilingrate(invertname, method='dustMedian')
    
    cpr_df = pd.read_csv(cprPath)
    cpr_df = cpr_df.loc[:,['dailyinput', 'CPR','Date']]
    cpr_df['Pe_cpr'] = cpr_df['dailyinput']*cpr_df['CPR']*cuanNum*panelNum*1000
    dateList = [item[0:10] for item in cpr_df['Date'].values]
    cpr_df['Date'] = dateList
    cpr_df = cpr_df.groupby(['Date']).sum()
    merged = pd.merge(merged, cpr_df,left_index=True, right_index = True, how='inner')

    

    #get the estimated power by using slope method
    slope_file = tool.getnbqFile(singleslopePath, invertname)
    slope_df = pd.read_csv(slope_file)   
    slope_df = slope_df.loc[:,['Pr', 'data_date']]
    slope_df.columns = ['Pr', 'Date']
    dateList = [item[0:10] for item in slope_df['Date'].values]
    slope_df['Date'] = dateList      
    slope_df = slope_df.groupby(['Date']).sum()
    new_merged = pd.merge(merged, slope_df,left_index=True, right_index=True, how='inner')
    
    #get soiling rate for the inverter
    dustRate = tool.soilingrate(invertname, method='dustMedian')  
    print(dustRate)
    
    clean_df = pd.read_csv(cleanlistPath).loc[:,['Date',invertname]]    
    clean_df.set_index(['Date'], inplace=True)
    new_merged = pd.merge(new_merged,clean_df,left_index=True, right_index=True, how='inner')  
    
    #get predict power using slope method
    new_merged[invertname] = [math.log2(item+1) for item in new_merged[invertname].values]
    new_merged['Pe_slope'] = new_merged['Pr'] * new_merged['Fs2m']*(1+dustRate* new_merged[invertname])
    
    #adjust cpr
    new_merged['Pe_cpr'] = new_merged['Pe_cpr']*(1+dustRate* new_merged[invertname])
    

    
    
    new_merged.to_csv(outPath+invertname+'.csv')




def getmultipowers(outPath,invertname):
    '''
    get powers from differnt methods for an invert  affected by multi-factors

    '''
    # get powers from weather satation methods, it is the same for all inverters
    filePath = '/Users/zhaoyingying/surfacesoiling/data/inverter/processed/S01-NBA.csv'
    df = pd.read_csv(filePath)
    df.fillna(method='ffill')
    
    #convert datetime to date: 2017-01-01 00:00:00 to 2017-01-01
    
    dateList = [item[0:10] for item in df['data_date'].values]  
    df['Date'] = dateList
    df['Pe_cleaning'] = df['I1m'] * df['V1m']
    df['Pe_syn'] = df['I2m'] * df['V1m']
    sum_df = df.groupby(['Date']).sum()
    avg_df = df.groupby(['Date']).mean()

    #get daily factors    
    df =sum_df.loc[:,['Fs2m','Pe_cleaning','Pe_syn']]
    df['Sd'] = avg_df['Sd']
    df['Wv'] = avg_df['Wv']
    df['Wd'] = avg_df['Wd']
    df['T0'] = avg_df['T0']
    print('get estimated power from weather satation data sucessfully!')
    
    #get powers from GPI
    
    #get the true power for the  inverter 
    file = tool.getnbqFile(invertPath,invertname)
    invert_df = pd.read_csv(file)
    invert_df.fillna(method='ffill')
         #convert datetime to date: 
    dateList = [item[0:10] for item in invert_df['data_date'].values] 
    invert_df['Date'] = dateList
    invert_df['P_true'] = invert_df['I'] * invert_df['V']
    invert_df = invert_df.groupby(['Date']).sum()
    invert_df =invert_df.loc[:,['P_true']]
     
     #get string number for the inverter
    nbqinfo = pd.read_csv('/Users/zhaoyingying/surfacesoiling/data/nbqinfo.csv').loc[:,['nbqno','cuan','rongliang']]
    index = nbqinfo[nbqinfo.nbqno==invertname].index.tolist()[0]
    cuanNum = nbqinfo.at[index,'cuan']
    rongliang = nbqinfo.at[index,'rongliang']
    print('the string num for the inverer is : '+str(cuanNum))
     
     #re-obtain the true power of the inver
    merged = pd.merge(invert_df, df,left_index=True, right_index=True, how='inner')
    merged['Pe_cleaning']= merged['Pe_cleaning']*cuanNum*panelNum
    merged['Pe_syn']= merged['Pe_syn']*cuanNum*panelNum
    merged['capacity']= rongliang*1000
     
     #get powerestimation from cpr
    cpr_df = pd.read_csv(cprPath)
    cpr_df = cpr_df.loc[:,['dailyinput', 'CPR','Date']]
    dustRate = tool.soilingrate(invertname, method='dustMedian')
    
    cpr_df['Pe_cpr'] = cpr_df['dailyinput']*cpr_df['CPR']*cuanNum*panelNum*1000*(1+dustRate)
    dateList = [item[0:10] for item in cpr_df['Date'].values] 
    cpr_df['Date'] = dateList
    cpr_df = cpr_df.groupby(['Date']).sum()
    merged = pd.merge(merged, cpr_df,left_index=True, right_index = True, how='inner')
     
     #get the estimated power by using multislope method
    slope_file = tool.getnbqFile(multislopePath, invertname)
    slope_df = pd.read_csv(slope_file)   
    slope_df = slope_df.loc[:,['Pr', 'data_date','PrSd','PrWv','PrWd','PrT0']]
    #slope_df = slope_df.loc[:,['Pr', 'data_date','PrSd','PrT0']]
    dateList = [item[0:10] for item in slope_df['data_date'].values]
    slope_df['Date'] = dateList  
     
    slope_df = slope_df.groupby(['Date']).sum()
 
    new_merged = pd.merge(merged, slope_df,left_index=True, right_index=True, how='inner')
    
    dustRate = tool.soilingrate(invertname, method='dustMedian')
    
    clean_df = pd.read_csv(cleanlistPath).loc[:,['Date',invertname]]    
    clean_df.set_index(['Date'], inplace=True)
    new_merged = pd.merge(new_merged,clean_df,left_index=True, right_index=True, how='inner')  
    #get predict power using slope method
    new_merged[invertname] = [math.log2(item+1) for item in new_merged[invertname].values]    
    new_merged['Pe_slope'] = (1+dustRate* new_merged[invertname])*(new_merged['Pr'] * new_merged['Fs2m'] + new_merged['PrSd'] * new_merged['Sd'] + new_merged['PrWv'] * new_merged['Wv'] + new_merged['PrWd'] * new_merged['Wd'] + new_merged['PrT0'] * new_merged['T0']) 
    #new_merged['Pe_slope'] = (1+dustRate* new_merged[invertname])*(new_merged['Pr'] * new_merged['Fs2m'] + new_merged['PrSd'] * new_merged['Sd']  + new_merged['PrT0'] * new_merged['T0']) 
       
    
    #adjust cpr
    new_merged['Pe_cpr'] = new_merged['Pe_cpr']*(1+dustRate* new_merged[invertname])
     #get the estimated power by using CPR-based method
     
     
    new_merged.to_csv(outPath+invertname+'.csv')   

def getwspowers(outPath,invertname):
    '''
    get powers from differnt methods for panels in weathersatation affected by irradiance

    '''
    # get powers from weather satation methods, it is the same for all inverters
    filePath = '/Users/zhaoyingying/surfacesoiling/data/inverter/processed/S01-NBA.csv'
    df = pd.read_csv(filePath)
    df.fillna(method='ffill')
    
    #convert datetime to date:    
    dateList = [item[0:10] for item in df['data_date'].values]  
    df['Date'] = dateList
    df['Pe_cleaning'] = df['I1m'] * df['V1m']
    
    df['P_true'] =df['I1m'] * df['V1m']
    df['Pe_syn'] = df['I2m'] * df['V1m']
    
    sum_df = df.groupby(['Date']).sum()
    
    #get daily factors    
    df =sum_df.loc[:,['Fs2m','Pe_cleaning','Pe_syn','P_true']]


    print('get estimated power from weather satation data sucessfully!')
    

    
    #get powerestimation from cpr
    dustRatePath='/Users/zhaoyingying/surfacesoiling/data/wsdustRate.csv' 
    sr = pd.read_csv(dustRatePath)
    sr = sr[sr.nbqName == invertname]    
    sr.set_index(['nbqName'], inplace=True)
    method='dustMedian'
    dustRate = sr.at[invertname, method]
  
    
    cpr_df = pd.read_csv(cprPath)
    cpr_df = cpr_df.loc[:,['dailyinput', 'CPR','Date']]
    cpr_df['Pe_cpr'] = cpr_df['dailyinput']*cpr_df['CPR']*1000
    dateList = [item[0:10] for item in cpr_df['Date'].values]
    cpr_df['Date'] = dateList
    cpr_df = cpr_df.groupby(['Date']).sum()
    merged = pd.merge(df, cpr_df,left_index=True, right_index = True, how='inner')

    

    #get the estimated power by using slope method
    slope_file = wsSlopePath+'P_synslope_ransac.csv'
    slope_df = pd.read_csv(slope_file)   
    slope_df = slope_df.loc[:,['Pr', 'data_date']]
    slope_df.columns = ['Pr', 'Date']
    dateList = [item[0:10] for item in slope_df['Date'].values]
    slope_df['Date'] = dateList      
    slope_df = slope_df.groupby(['Date']).sum()
    new_merged = pd.merge(merged, slope_df,left_index=True, right_index=True, how='inner')
    

    
    invertname = 'syn'
    clean_df = pd.read_csv(wscleanlistPath).loc[:,['Date',invertname]]    
    clean_df.set_index(['Date'], inplace=True)
    new_merged = pd.merge(new_merged,clean_df,left_index=True, right_index=True, how='inner')  
    
    #get predict power using slope method
    new_merged[invertname] = [math.log2(item+1) for item in new_merged[invertname].values]
    new_merged['Pe_slope'] = new_merged['Pr'] * new_merged['Fs2m']*(1+dustRate* new_merged[invertname])
    
    #adjust cpr
    new_merged['Pe_cpr'] = new_merged['Pe_cpr']*(1+dustRate* new_merged[invertname])   
    new_merged.to_csv(outPath+invertname+'.csv')   

def wsMRE(powerPath,method):
    '''
    for weather station, get power's mean relative error of true power and estimatied powers by different methods: gpi, cpr, weather-station
    '''
    MRE_syn = np.zeros((invertnum, 1))
    MRE_cpr = np.zeros((invertnum, 1))
    MRE_slope = np.zeros((invertnum, 1))

    
    
    flist = glob.glob(powerPath+'*.csv')  
    print(flist)      
    for idx,f in enumerate(flist):
        

        df_org = pd.read_csv(f).loc[:,['Date','P_true','Pe_syn','Pe_cpr','Pe_slope']]
        
        #get mre for the syn panel
        df_org['MRE_syn'] = abs(df_org['P_true']-df_org['Pe_syn'])/df_org['P_true']  
        #get mre for the cpr panel
        df_org['MRE_cpr'] = abs(df_org['P_true']-df_org['Pe_cpr'])/df_org['P_true']
        #get mre for the syn panel
        df_org['MRE_slope'] = abs(df_org['P_true']-df_org['Pe_slope'])/df_org['P_true']  
        
        
        #print(df_org)

        #reove outliers
        df = df_org[ (df_org['MRE_syn']<0.5) & (df_org['MRE_cpr']<0.5) & (df_org['MRE_slope']<0.5)]

        
    
    df.to_csv(mrePath)

    
    #print(MRE_df)
    print(df['MRE_syn'].mean())
    print(df['MRE_cpr'].mean())
    print(df['MRE_slope'].mean())
    
    
    
        
    #plot
    plt.plot(df['MRE_syn'],label='MRE_syn (mean= 0.0549)')
    plt.plot(df['MRE_cpr'],label='MRE_cpr (mean = 0.0023)')
    plt.plot(df['MRE_slope'],label='MRE_slope (mean = 0.0385)')
        
    plt.xlabel('Time Stamp (Day)')
    plt.ylabel('MRE of Power Loss')
    plt.legend()
    plt.xticks()


        
    plt.savefig(figPath + method+'mre2.png', dpi=300)
    plt.show() 
        
    plt.close()
            

#if __name__ == "__main__":
    
    
#    allnbq = tool.getnbqList()   
#    for idx, nbq in enumerate(allnbq):
#        getpowers(siglepowers,nbq)
#        #break
#    MRE(siglepowers,method = 'single')
    
    #get powers affected by multiple factors
#    allnbq = tool.getnbqList()   
#    for idx, nbq in enumerate(allnbq):
#        getmultipowers(multiPowers,nbq)
#
#    MRE(multiPowers,method = 'multi')
    