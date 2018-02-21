#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 09:12:05 2018

@author: zhaoyingying
"""
import glob
import os
import soil_model_inverter
import pandas as pd
import soiling_rate
import evaluation
import tool

nbqDataPath = '/Users/zhaoyingying/surfacesoiling/data/inverter/processed/'
singleslopePath = '/Users/zhaoyingying/surfacesoiling/data/inverter/slope/singleransac/'
MultiSlopePath = '/Users/zhaoyingying/surfacesoiling/data/inverter/slope/multiransac/'
wsSlopePath ='/Users/zhaoyingying/surfacesoiling/data/inverter/slope/weatherstation/'
dustRatePath = '/Users/zhaoyingying/surfacesoiling/data/'
qxjl = '/Users/zhaoyingying/surfacesoiling/data/qxjl.csv'
figPath = '/Users/zhaoyingying/surfacesoiling/data/fig/'

siglepowers = '/Users/zhaoyingying/surfacesoiling/data/results/siglepowers/'
multiPowers = '/Users/zhaoyingying/surfacesoiling/data/results/multipowers/'
wsPowers ='/Users/zhaoyingying/surfacesoiling/data/results/wspowers/'
cprPath = '/Users/zhaoyingying/surfacesoiling/data/dailyCPR.csv'
mrePath = '/Users/zhaoyingying/surfacesoiling/data/results/mre/mre.csv'
cleanlistPath = '/Users/zhaoyingying/surfacesoiling/data/cleaninglist.csv'


extSlope = False
getSoilRate = False
eva = False
#verify on weather station
VerWS = True



if __name__ == "__main__":
    
    #extrace slope features
    if extSlope == True:
        flist = glob.glob(nbqDataPath+'*.csv')        
        for f in flist:
            nbqname = os.path.basename(f)
            nbqData = pd.read_csv(f, delimiter=',')
            nbqData = nbqData.fillna(method='ffill')
            soil_model_inverter.extractSlopeFea(nbqData,nbqname)
            #soil_model_inverter.extractMultiSlopeFea(nbqData,nbqname)
        
    #get soiling rate
    if getSoilRate == True:
        soiling_rate.countdust(singleslopePath,method = 'single')
        #soiling_rate.countdust(MultiSlopePath,method = 'multi')
    
    #evaluation, cal mean relative power loss
    if eva == True:
        allnbq = tool.getnbqList()   
        for idx, nbq in enumerate(allnbq):
            #evaluation.getpowers(siglepowers,nbq)
            evaluation.getmultipowers(multiPowers,nbq)
        evaluation.MRE(siglepowers,method = 'single')
        #evaluation.MRE(multiPowers,method = 'multi')
    if VerWS == True:
        
        #extract weather sataion data form either inverter
        wsPath =  nbqDataPath+'S01-NBA.csv'  
        wsData = pd.read_csv(wsPath, delimiter=',')
        
        #for daily clean panle
        #soil_model_inverter.extractWSSlopeFea(wsData,field = 'P_cln')
        #soil_model_inverter.extractWSSlopeFea(wsData,field = 'P_syn')
        #get soiling rate
        #soiling_rate.countdust(wsSlopePath,method = 'ws')
        #evaluation
        evaluation.getwspowers(wsPowers,invertname='P_synsl')
        evaluation.wsMRE(wsPowers,method = 'ws')
        
        
    