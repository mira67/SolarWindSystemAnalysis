#Soiling model using slope-based method - Test
#Author: Qi Liu
#Email: qi.liu@colorado.edu

import pymysql.cursors
import numpy as np
import pandas as pd
from sklearn import linear_model
import time
import math
import datetime
import multiprocessing as mp
from itertools import cycle, islice

#Parameters configuration
startDTModel = '2016-01-01'
endDTModel = '2017-03-27'

# date list
start = datetime.datetime.strptime(startDTModel, "%Y-%m-%d").date()
end = datetime.datetime.strptime(endDTModel, "%Y-%m-%d").date()
dateList = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]

dayList = []
for day in dateList:
    dayList.append(str(day))

timeRg = ['05:30','19:30'];#use pandas to get data within this range

resPath = 'E:/myprojects/pv_detection/data/concord_work/soiling_slope/'

"""
Data Query Module: Extract data from database, table-hlx
Input: String Info: hlxID, strID, Datetime: startDT,endDT
Output: String current
"""
def queryStrData(hlxID, startDT,endDT, timeRg):
    # AND TIME(data_date) BETWEEN '08:00'AND '17:00'
    # AND TIME(data_date) BETWEEN '08:00'AND '17:00'
    sql1 = """SELECT * FROM pingyuan.hlx WHERE combinerbox = '{}' 
            AND data_date BETWEEN '{}' AND '{}' 
            AND TIME(data_date) BETWEEN '{}'AND '{}'"""
    sqlSts1 = sql1.format(hlxID, startDT,endDT, timeRg[0], timeRg[1])
    
    sql2 = """SELECT data_date,Fs2m FROM pingyuan.qxz 
            WHERE data_date BETWEEN '{}' AND '{}'
            AND TIME(data_date) BETWEEN '{}'AND '{}';"""
    sqlSts2 = sql2.format(startDT,endDT,timeRg[0], timeRg[1])
    
    #Make database connetion
    db = pymysql.connect(host='localhost',
                                user='liuqi',
                                password='1234',
                                db='pingyuan',
                                port=3306,
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor,local_infile=True)

    try:
        '''training data'''        
        cursor = db.cursor()
        cursor.execute(sqlSts1)
        db.commit()
        
        #collect query data
        strCurrent = pd.DataFrame(cursor.fetchall())
        
        cursor.execute(sqlSts2)
        db.commit()
        
        #collect query data
        features = pd.DataFrame(cursor.fetchall())
        
        #join table to avoid missing dates problem
        cbData = strCurrent.join(features.set_index('data_date'),on='data_date')
        
    except Exception as e:
        # Rollback in case there is any error
        db.rollback()
        print('Not able to query hlx %s' % (hlxID))
        
    #close connection
    db.close()
    return cbData

#Module: Linear Regression
def strSlopeModel(Features,stringCurrent, estimator):
    '''
    multiple regression estimation methods
    simple-simple linear
    theil-theil-sen, median
    '''
    if estimator == 'simple':
        lm = linear_model.LinearRegression()
        lm.fit(Features,stringCurrent)
    elif estimator == 'theil':
        pass
    elif estimator == 'ransac':
        lm = linear_model.RANSACRegressor()
        lm.fit(Features,stringCurrent)
    else:
        print('Invalid Estimator')
    return lm
    
#Module: Extract hlx slope features
def extractSlopeFea(hlxID):
    """
    Grab daily slopes and put in dataframe and save to csv files
    """
    # grab daily slopes -> upgrade code to spark later for multiple columns computing in parallel
    # create an array to store slopes for each strings
    numDays = len(dayList[:-1])
    numStrs = 16
    slopeArray = np.zeros((numDays, numStrs))
    try:
        for idx, day in enumerate(dayList[:-1]):
            # query data
            df = queryStrData(hlxID, day, dayList[idx+1], timeRg)
            df = df.dropna(axis=0, how='any')
            # all strings currents
            df_strings = df.iloc[:,0:16]
            colName = df_strings.columns.values
            strNames = colName[0:16]
            # feature data
            df_fea = df.iloc[:,-1]
            #fft feature holder for each CB
            all_slopes = pd.DataFrame()
            
            for idy, strName in enumerate(strNames):
                # compute slope for each string
                currents = df_strings[strName]
                # features, currents
                lm = strSlopeModel(df_fea.values.reshape(-1, 1), currents.values.reshape(-1, 1), 'ransac')
                slope = lm.estimator_.coef_[0]#lm.coef_[0]#extract slopes
                # put in array
                slopeArray[idx,idy] = slope
    
        #obtain dataframe and record to file
        slopeDF = pd.DataFrame(data=slopeArray, columns=strNames)
        slopeDF['data_date'] = pd.DataFrame(data=dayList)
        filename = resPath + 'slope_'+hlxID+'.csv'
        slopeDF.to_csv(filename, sep=',',header=True)
    
    except Exception as e: 
        print('Exception: ',e)
        print('Not able to process string %s:' % (hlxID))
        
    return '2018' 
    
#Main
def main():
    # list of combiner boxes
    hlx_info = pd.read_csv('E:/myprojects/pv_detection/data/concord_work/cuaninfo_pingyuan.csv')
    hlxList = hlx_info['combinerbox'].unique().tolist()
    #hlxList = map(str, hlxList)
    #extractSlopeFea(hlxList[0])
    # profiling

    start = time.time()

    with mp.Pool(4) as pool:
        results = pool.map(extractSlopeFea, hlxList)
    end = time.time()
    runtime = end - start
    
    msg = "Feature Extraction Multi-Processing Took {time} seconds to complete"
    print(msg.format(time=runtime))

    '''
    start = time.time()
    #patternDetection('1191278995')
    with mp.Pool(3) as pool:
        results = pool.map(test, strings)
    end = time.time()
    runtime = end - start
    msg = "Fault Detection Multi-Processing Took {time} seconds to complete"
    print(msg.format(time=runtime))
    ''' 

if __name__ == "__main__":
    main()

#Alert! Thinking programming in multi-processing ways and easier to configure with
#new alsogithms and data pre-processing methods