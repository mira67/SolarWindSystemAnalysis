#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 09:54:48 2018

@author: zhaoyingying
"""

# give the normal range for each field due to experience of each PV site
# the following range is obtained in Pingyuan Site
#the current and voltage range for each inverter is limited by the number of PV panels in the inverter
import pandas as pd
import glob
import os

Fs2mRg = [50,1000]
I1mRg=[0,8.79]
I2mRg=[0,8.79]
V1mRg=[0,45.30]
tempRg = [-10,50]
WdRg = [0,365]
WvRg = [0,50]
SdRg = [0,100]
panelNum = 16
rawPath = '/Users/zhaoyingying/surfacesoiling/data/inverter/'
processedPath = '/Users/zhaoyingying/surfacesoiling/data/inverter/processed/'

def IVRg(invertname):
    '''
    get the current and voltage range for each inverter
    '''
    nbqinfo = pd.read_csv('/Users/zhaoyingying/surfacesoiling/data/nbqinfo.csv').loc[:,['nbqno','cuan']]
    index = nbqinfo[nbqinfo.nbqno==invertname].index.tolist()[0]
    cuanNum = nbqinfo.at[index,'cuan']
    IRg=[0,cuanNum*I1mRg[1]]
    VRg=[0,panelNum*V1mRg[1]]
    return IRg,VRg
def preProcessData(inPath,outPath):
    '''
    remove the errors due to sensor for the import fields for each inverter
    med filter data using 60 minute, medfiltLen = 61 , 
    
    '''
    medfiltLen = 61 
    smlen = 31
    flist = glob.glob(inPath+'*.csv')        
    for f in flist:
        df_org = pd.read_csv(f)
        #get the invert name
        invertName = os.path.basename(f)[0:7]
        IRg,VRg = IVRg(invertName)
        
        #remove errors 
        df = df_org[(df_org['Fs2m'] < Fs2mRg[1]) & (df_org['Fs2m'] > Fs2mRg[0]) &
                        (df_org['I1m'] < I1mRg[1]) & (df_org['I1m'] > I1mRg[0]) &
                        (df_org['I2m'] < I2mRg[1]) & (df_org['I2m'] > I2mRg[0]) &
                        (df_org['V1m'] < V1mRg[1]) & (df_org['V1m'] > V1mRg[0]) &
                        (df_org['T0'] < tempRg[1]) & (df_org['T0'] > tempRg[0]) &
                        (df_org['Wd'] < WdRg[1]) & (df_org['Wd'] > WdRg[0]) &
                        (df_org['Wv'] < WvRg[1]) & (df_org['Wv'] > WvRg[0]) &
                        (df_org['Sd'] < SdRg[1]) & (df_org['Sd'] > SdRg[0]) &
                        (df_org['I'] < IRg[1]) & (df_org['I'] > IRg[0]) &
                        (df_org['V'] < VRg[1]) & (df_org['V'] > VRg[0])]
        
        # med filt using one hour data
        columns =['Fs2m','I1m','I2m','V1m','T0','Wd','Wv','Sd','I','V']
        tmpdf = df.copy()
        #print(tmpdf.iloc[0:smlen,:])
        df.loc[:,columns] = df.loc[:,columns].rolling(window=medfiltLen,center=True).median()
        #print(tmpdf.iloc[0:smlen,:])
        df.iloc[0:smlen,:] = tmpdf.iloc[0:smlen,:]
        df.iloc[-smlen:,:] = tmpdf.iloc[-smlen:,:]     
        
       # print(invertName+' has been processed sucessfully!')
        df.to_csv(outPath+invertName+'.csv',index = False)
        

    
if __name__ == "__main__":
    preProcessData(rawPath,processedPath)

    