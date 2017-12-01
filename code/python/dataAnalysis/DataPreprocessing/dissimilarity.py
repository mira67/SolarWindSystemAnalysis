# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 15:55:38 2017

@author: xiaomei

analyzing the missimilairty among strings in the same combiner box

"""
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import time
import csv
import glob
import os
import datetime
import math
import scipy.stats as stats

StringName = ['I1','I10','I11','I12','I13','I14','I15','I16','I2','I3','I4','I5','I6','I7','I8','I9']

inPath_NormalCB = '/Users/zhaoyingying/SolarWindSystemAnalysis/code/python/dataAnalysis/DataPreprocessing/S01-NBA-HL01.csv'
inPath_AbnormalCB = '/Users/zhaoyingying/SolarWindSystemAnalysis/code/python/dataAnalysis/DataPreprocessing/S35-NBA-HL06.csv'
outPath_Normal='/Users/zhaoyingying/SolarWindSystemAnalysis/code/python/dataAnalysis/DataPreprocessing/normal.csv'
outPath_Abormal='/Users/zhaoyingying/SolarWindSystemAnalysis/code/python/dataAnalysis/DataPreprocessing/abnormal.csv'

start = datetime.datetime.strptime("2016-06-01", "%Y-%m-%d").date()
end = datetime.datetime.strptime("2016-06-01", "%Y-%m-%d").date()
dateList = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
# this is just for one day testing
dateName = '#data_date'
timeRg = ['08:00','17:00'];#maybe calculate based on the sunshine value, contextual information
interval = 10;#every n min sampling
dayList = []
for day in dateList:
    dayList.append(str(day))
#print(dayList)
    
CBNum = 553
    
#daily clustering results
numDays = len(dateList)
                           
def Dissimilarity():
    '''
    analyzing the dissimilairity for different combiner box during a month in pingyuan site
    '''
    df = pd.read_csv(inPath_AbnormalCB)
    #assume the combiner box have 16 strings
    stringNum = 16
    results = np.zeros((stringNum,stringNum))
    # get the startline and endline :0601: 08:00-17:00
    startline = 198
    endline = 738
    
    for i in range(len(StringName)):
        for j in range(i+1):
            dfi = np.array(df.loc[startline:endline,StringName[i]])
            dfj = np.array(df.loc[startline:endline,StringName[j]])
            #print the similarity
            #print(stats.pearsonr(dfi,dfj)[0])
            tmp = stats.pearsonr(dfi,dfj)[0]
            #print the dissimilairty
            results[i,j] = math.sqrt((1-tmp)/2)
            results[j,i] = results[i,j]
            #print(results[i,j])
        
    for k in range(len(StringName)):
        results[k,k] = 0.0
    Results = pd.DataFrame(results)          
    Results.to_csv(outPath_Abormal)
    flat = results.flatten()  
    newflat = np.unique(flat)
    print(newflat)
    newflat.sort()
    maxvalue = newflat[-1]
    secondmaxvalue = newflat[-2]
    different = maxvalue - secondmaxvalue
    print('maxvalue, secondmaxvalue, and the diff are: ')
    print(maxvalue)
    print(secondmaxvalue)
    print (format(different,'.6f'))
    
if __name__ == '__main__':
    starttime = time.time()

    Dissimilarity()
    endtime = time.time()
    print ('Processing Data use :%s sencods'%(endtime-starttime))
 