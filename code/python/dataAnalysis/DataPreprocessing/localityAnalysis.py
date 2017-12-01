# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 15:55:38 2017

@author: xiaomei

"""
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
import time
import csv
import glob
import os
import datetime
import scipy.stats as stats

StringName = ['I1','I10','I11','I12','I13','I14','I15','I16','I2','I3','I4','I5','I6','I7','I8','I9']
colName =['#data_date','Std','Median','Mean']
inPath = 'D:/Xiaomei/SolarEnergy/SolarEnergy/data/pingyuan/smoothedMedian_Jun/'
#inPath = 'D:/Xiaomei/SolarEnergy/SolarEnergy/data/pingyuan/test/'
outPath='F:/PVData/LocalityAnalysis/pingyuan/'
Globalpath='F:/PVData/LocalityAnalysis/pingyuan/Globalpath/'
Corrpath='F:/PVData/LocalityAnalysis/pingyuan/Globalpath/corr/'
localStage = False
globalStage = True
CBNum = 553;

start = datetime.datetime.strptime("2016-06-01", "%Y-%m-%d").date()
end = datetime.datetime.strptime("2016-07-01", "%Y-%m-%d").date()
dateList = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
# this is just for one day testing
dateName = '#data_date'
timeRg = ['08:00','17:00'];#maybe calculate based on the sunshine value, contextual information
interval = 10;#every n min sampling
dayList = []
for day in dateList:
    dayList.append(str(day))
#print(dayList)
    
#daily clustering results
numDays = len(dateList)


def removingNULLValues(inputfile,outputfile):
    '''
    removing the invalidate values: null, denoted by '' or 'nan'
    '''
    print(inputfile)
    print(outputfile)
    hlx = os.path.basename(inputfile)
    outputfile = outPath+'test'+hlx
    open(outputfile,'w',newline='')
    csv_reader = csv.reader(open(inputfile, encoding='utf-8'))
    for row in csv_reader:
        flg = len(str(row[1]))
        #if (flg!=0) or ('nan' not in (row[1]) ):
        if flg != 0:
            print(str(flg))
            with open(outputfile,'a',newline='', encoding='utf-8') as data:
                writer = csv.writer(data)
                writer.writerow(row)
                           
def GlobalCorrAnalysisPingyuan():
    '''
    analyzing the corrlation for different combiner box during a month in pingyuan site
    for a specific data_date

    '''

    #there are 553 combiner boxes in pingyuan site
    CBNum = 553
    #CBNum = 10
    
    GlobalcolName=['Median']
    results = np.zeros((CBNum,CBNum))
    flist = glob.glob(inPath+'*.csv')

    #analyzing each feature: median variation, mean variation, and std variation
    for idex, item in enumerate(GlobalcolName):  
        #compare each combiner box with other combiner box
        for i in range(72,CBNum):
            for j in range(i+1,CBNum):
                hlxi = os.path.basename(flist[i])
                hlxj = os.path.basename(flist[j])
                print('start processing combiner box: '+ hlxi+ ' and '+ hlxj )
                dfi = pd.read_csv(flist[i])
                dfj = pd.read_csv(flist[j])
                # get the startline and endline 
                startline = 198
                endline = 738
#                with open (flist[i]) as csvfile:
#                    print('opening')
#                    reader = csv.reader(csvfile)
#                    for lineNum,row in enumerate(reader):
#                        if row[0].find('2016-06-01'+' '+timeRg[0]) != -1 :              
#                            startline = lineNum 
#                            print(startline)
#                        if row[0].find('2016-06-01'+' '+ timeRg[1]) != -1:
#                            endline = lineNum
#                            print(endline)
#                dfi = np.array(dfi.loc[startline:endline:interval,item])
#                
#                #get combiner box j
#                with open (flist[j]) as csvfile:
#                    reader = csv.reader(csvfile)
#                    for lineNum,row in enumerate(reader):
#                        if row[0].find('2016-06-01'+' '+timeRg[0]) != -1 :              
#                            startline = lineNum 
#                            print(startline)
#                        if row[0].find('2016-06-01'+' '+ timeRg[1]) != -1:
#                            endline = lineNum
#                            print(endline)
                dfi = np.array(dfi.loc[startline:endline,item])
                dfj = np.array(dfj.loc[startline:endline,item])
                print(stats.pearsonr(dfi,dfj)[0])
                results[i,j] = stats.pearsonr(dfi,dfj)[0]
                results[j,i] = results[i,j]
                print('the correlation between:'+ hlxi+ ' and '+ hlxj+' is:')
                print(results[i,j])
        for k in range(CBNum):
            results[k,k] = 1.0
        Results = pd.DataFrame(results)          
        Results.to_csv(Corrpath+item+'10min.csv')

def FillMatrix():
    '''
    analyzing the corrlation for different combiner box during a month in pingyuan site
    for a specific data_date

    '''

    #there are 553 combiner boxes in pingyuan site
    CBNum = 553
    #CBNum = 10

    results = np.zeros((CBNum,CBNum))
    matrixPath = 'F:/PVData/LocalityAnalysis/pingyuan/Globalpath/corr/MedianTotal.csv'
    df = pd.read_csv(matrixPath).iloc[:,1:]
    results= df.as_matrix()
    print(results[0,0])
    print(results[0,1])
    print(results[0,2])
    print(results[0,3])
    print(results )
    for i in range(1,CBNum):
        for j in range(i):
            results[i,j] = results[j,i]
    for i in range(CBNum):
            results[i,i] = 1.0
    Results = pd.DataFrame(results)          
    Results.to_csv('F:/PVData/LocalityAnalysis/pingyuan/Globalpath/corr/ResultsMedianTotal.csv')

def testMatrix():
    '''
    analyzing the corrlation for different combiner box during a month in pingyuan site
    for a specific data_date

    '''

    #there are 553 combiner boxes in pingyuan site
    CBNum = 550
    #CBNum = 10

    results = np.zeros((CBNum,CBNum))
    matrixPath = 'F:/PVData/LocalityAnalysis/pingyuan/Globalpath/corr/plotMedianCorr.csv'
    df = pd.read_csv(matrixPath,header = None)
    results= df.as_matrix()
    print(results[0,0])
    print(results[0,1])
    print(results[0,2])
    print(results[0,3])
    print(results )
    for i in range(CBNum):
        for j in range(CBNum):
            if(results[i,j]<0.95):
                print(i)
                print(j)
                print(results[i,j])
                       
def GlobalAnalysisPingyuan():
    '''
    analyzing the variance for different combiner box during a month in pingyuan site

    '''
    #there are 553 combiner boxes in pingyuan site
    CBNum = 553
    
    GlobalcolName=['Median','Mean','Std']
    flist = glob.glob(outPath+'*.csv')

    
    #get monthly median, mean, and std
    for idex, item in enumerate(GlobalcolName):   
        #from the file of each combiner box
        results = np.zeros((numDays,CBNum))
        #print ('start processing montly: '+ item)
        for jdx,f in enumerate(flist):
                hlx = os.path.basename(f)
                #print('start processing combiner box: '+ hlx)
                df = pd.read_csv(f)
                #subtotal values
                results[:,jdx] = df.loc[:,item].as_matrix()
                #print(jdx)
        Results = pd.DataFrame(results)
        Results.to_csv(Globalpath+item+'.csv')

    
                
def localLocalityAnalysis(path):
    '''
    analyzing the variance for all strings in the same combiner box during a day
    '''
    df = pd.read_csv(path)
    print(df)
    df = df.loc[:,StringName]
    df2 = np.zeros((df.shape[0],3))
    for i in range(df.shape[0]):
        #save mean,median,and variance
        df2[i,0] = np.mean(df.loc[i,StringName])
        df2[i,1] = np.median(df.loc[i,StringName])
        df2[i,2] = np.var(df.loc[i,StringName]) 
        print('sucessfully processed the '+str(i)+'th value: '+str(df2[i,2]) )
  
    np.savetxt('F:/PVData/test/test.csv',df2,delimiter=',')

    
   # plt.plot(mn,var,median)    

def localAnalysisPingyuan(path):
    '''
    analyzing the variance for all strings in the same combiner box during a day in pingyuan site
    '''
    df = pd.read_csv(path)
    #read the data_date, std, median, mean
    df = df.loc[:,colName]
    #4 cols: date , counted average daily std , median, mean 
    results = np.zeros((numDays,4))
    print ('start processing')

    for idx,item in enumerate(dateList):
        #grab start and end time 
        startline = 0
        endline = 0
        with open (path) as csvfile:
            reader = csv.reader(csvfile)
            for lineNum,row in enumerate(reader):
                if row[0].find(item.strftime('%Y-%m-%d')+' '+timeRg[0]) != -1 :              
                    startline = lineNum 
                    #print(startline)
                if row[0].find(item.strftime('%Y-%m-%d')+' '+ timeRg[1]) != -1:
                    endline = lineNum
                    #print(endline)
    
        results[idx,1] = np.mean(df.loc[startline:endline,'Std'])
        results[idx,2] = np.mean(df.loc[startline:endline,'Median'])
        results[idx,3] = np.mean(df.loc[startline:endline,'Mean'])
    
    Results = pd.DataFrame(results, columns=colName)
    datesArr = np.asarray(dateList)
    Results[dateName] = datesArr
           
    hlx = os.path.basename(path)
    Results.to_csv(outPath+hlx)
    #pd.savetxt('F:/test.csv',results,fmt='%.4f',delimiter=',')

    
   # plt.plot(mn,var,median)        

def localGlobalMeanVar():
    #give a specific time :
    timestamp = 350

    
    stringPath = 'F:/PVData/figures/allstrings.csv'
    df = pd.read_csv(stringPath,header= None)
    #get headername
    headerName = np.asarray(df.iloc[0,1:])
    #get data
    df = df.iloc[1:,1:]

    globalmean = df.iloc[timestamp,:].mean()
    globalvar = df.iloc[timestamp,:].var()
    
    print(globalmean)
    print(globalvar)
    
   #get all combiner box names
    startcol = 0 
    CBname = []
    #store mean and var
    localmean = []
    localvar=[]
    lastline = 0

    for idx,item in enumerate(headerName):
        tmp = item.split('I')
        
    #if the combiner box occurs at the first time 
        if tmp[0] not in CBname:
            CBname.append(tmp[0])
            endcol = idx
            localmean.append(df.iloc[timestamp,startcol:endcol].mean())
            localvar.append(df.iloc[timestamp,startcol:endcol].var())
            #start from a new combiner box
            startcol = endcol
        lastline = idx
    #for the last combiner box
    endcol=idx
    endcol = lastline
    localmean.append(df.iloc[timestamp,startcol:endcol].mean())
    localvar.append(df.iloc[timestamp,startcol:endcol].var())

    results= np.zeros((CBNum+1,2))
    for i in range(CBNum+1):
        results[i,0] = localmean[i]
        results[i,1] = localvar[i]
    results[0,0] = globalmean
    results[0,1] = globalvar
    Results = pd.DataFrame(results)  
    Results.to_csv('F:/PVData/figures/local.csv')
    

    
        
        
    

if __name__ == '__main__':
    starttime = time.time()
   # flist = glob.glob(inPath+'*.csv')
    
    '''
    the following is the local analysis 
    
    for f in flist:
        #removingNULLValues(f,outPath)
        #localLocalityAnalysis(f)
        localAnalysisPingyuan(f)        
        hlx = os.path.basename(f)
        print('sucessfully processing combiner box: '+ hlx)
    '''
    '''
        the following it the local analysis 
    '''
    #passing
    #GlobalAnalysisPingyuan()
    
    #GlobalCorrAnalysisPingyuan()
    #FillMatrix()
    #testMatrix()
    localGlobalMeanVar()
    endtime = time.time()
    print ('Processing Data use :%s sencods'%(endtime-starttime))

    """
    process = data_processed()
    #traverse all folder 
    folderlist = dp.each_file(inPath,0)
   # print(folderlist)
    for i in range(len(folderlist)):
        flist = glob.glob(folderlist[i]+'/*.csv')
        print(folderlist[i])
        startTime = time.time()
        for f in flist:
            process.hlx_processed_offline(f)
        endTime = time.time()
        msg = 'Took {Time} seconds to complete'
        print(msg.format(time= endTime-startTime))
   """   