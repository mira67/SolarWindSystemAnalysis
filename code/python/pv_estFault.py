#PV Estimator Based Fault Detection
#Author: Qi Liu
#Email: qi.liu@colorado.edu

"""Test 1: real-time online detection with raw 1min data without filtering"""

import pymysql.cursors
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import time
import multiprocessing as mp

#Make database connetion
db = pymysql.connect(host='localhost',
                            user='liuqi',
                            password='1234',
                            db='pingyuan',
                            port=3306,
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor,local_infile=True)

cursor=db.cursor()

#Parameters configuration
startDTModel = '2016-01-01'
endDTModel = '2016-03-31'

startDTTest = '2016-06-01'
endDTTest = '2016-06-30'

timeRg = ['10:00','16:00'];#use pandas to get data within this range

"""
Step 1: Extract data from database, table-hlx
Input: String Info: hlxID, strID, Datetime: startDT,endDT
Output: String current
"""
def queryStrData(hlxID, strID, startDT,endDT):
    
    sql = """SELECT {} FROM pingyuan.hlx WHERE combinerbox = '{}' 
            AND data_date BETWEEN '{}' AND '{}' AND TIME(data_date) BETWEEN '10:00'AND '16:00';"""
    sqlSts = sql.format(strID, hlxID, startDT,endDT)
    print(sqlSts)
    try:
        cursor = db.cursor()
        cursor.execute(sqlSts)
        db.commit()
        
        #collect query data
        strCurrent = pd.DataFrame(cursor.fetchall())
        print(strCurrent.head())
    except:
        # Rollback in case there is any error
        db.rollback()
        print('Not able to query string %s' % (strID))
        
    #close connection
    cursor.close()
    db.close()
    return strCurrent

"""
Step 2: Extract weather data from database, table-qxz
Input: Features: FeatureList, Datetime: startDT,endDT
Output: Features array
"""
def queryFeaData(FeatureList, startDT,endDT):
    sql = """SELECT FS1,Fs2,Fs1m,Fs2m,Wv,Wd,Sd,T0 FROM pingyuan.qxz WHERE data_date BETWEEN '{}' AND '{}'
    AND TIME(data_date) BETWEEN '10:00'AND '16:00';"""
    sqlSts = sql.format(startDT,endDT)
    print(sqlSts)
    try:
        cursor = db.cursor()
        cursor.execute(sqlSts)
        db.commit()
        
        #collect query data
        features = pd.DataFrame(cursor.fetchall())
        print(features.head())
    except:
        # Rollback in case there is any error
        db.rollback()
        print('Not able to query features')
        
    #close connection
    cursor.close()
    db.close()
    return features

#queryStrData('S01-NBA-HL0111','I1','2016-01-01','2016-01-02')
#consider to also write to files for later easier access?

#Step 3: Build model for individual string
def strPowerModel(Features,stringCurrent):
    #Build libear model
    lm = LinearRegression()
    lm.fit(Features,stringCurrent)
    return lm
    
#Step 4: Fault detection for individual string
def strFaultDetection(hlxID, strID, FeatureList, startDT,endDT):
    #Get data
    stringCurrent = queryStrData(hlxID, strID, startDT,endDT)
    Features = queryFeaData(FeatureList, startDT,endDT)
    
    #Build Model
    #lm = strPowerModel(Features, stringCurrent)
   
    """using model to check new data for faults
        grab test data from database, using last 10 days in June
        Method 1: directly compare difference error > 10%
    """
    
    #Get test data for this string [2016-06-01, 2016-06-30] data
    """
    testX = queryFeaData(FeatureList, startDTTest,endDTTest)
    testY = queryStrData(hlxID, strID, startDTTest,endDTTest)
    predY = lm.predict(testX)
    resErr = (testY-predY)/testY*100
    print(resErr)
    return resErr
    """
    #set resErr > 10 to Fault label in restult file
    
    
#Step 5: Summarize fault detection results for ground truth comparison
def rankFaultString():
    pass
    
def test(lists):
    print(lists)
    
#Main
def main():
    dataPath = 'E:/myprojects/pv_detection/code/code/python/testData.xlsx'
    strInfo = pd.read_excel(dataPath).values.tolist(); 
    #strings = map(str, strInfo)#seems only string list works for pool map
    #print(strInfo)
    
    testData = strInfo[0]
    hlxID = testData[0]
    strID = 'I'+str(testData[1])
    FeatureList = ['FS1','Fs2','Fs1m','Fs2m','Wv','Wd','Sd','T0']
    strFaultDetection(hlxID, strID, FeatureList, startDTModel,endDTModel)
    
    #profiling 1
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

