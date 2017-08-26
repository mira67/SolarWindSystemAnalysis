#PV Estimator Based Fault Detection
#Author: Qi Liu
#Email: qi.liu@colorado.edu

"""Test 1: real-time online detection with raw 1min data without filtering"""

import pymysql.cursors
import numpy as np
from pandas import DataFrame
from sklearn.linear_model import LinearRegression

#Make database connetion
db = pymysql.connect(host='localhost',
                            user='liuqi',
                            password='1234',
                            db='pingyuan',
                            port=3306,
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor,local_infile=True)

cursor=db.cursor()

"""
Step 1: Extract data from database, table-hlx
Input: String Info: hlxID, strID, Datetime: startDT,endDT
Output: String current
"""
def queryStrData(hlxID, strID, startDT,endDT):
    
    sql = """SELECT {} FROM pingyuan.hlx WHERE combinerbox = '{}' 
            AND riqi BETWEEN '{}' AND '{}';"""
    sqlSts = sql.format(strID, hlxID, startDT,endDT)
    print(sqlSts)
    try:
        cursor = db.cursor()
        cursor.execute(sqlSts)
        db.commit()
        
        #collect query data
        strCurrent = DataFrame(cursor.fetchall())
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
    sql = """SELECT {} FROM pingyuan.qxz WHERE riqi BETWEEN '{}' AND '{}';"""
    sqlSts = sql.format(FeatureList,startDT,endDT)
    print(sqlSts)
    try:
        cursor = db.cursor()
        cursor.execute(sqlSts)
        db.commit()
        
        #collect query data
        features = DataFrame(cursor.fetchall())
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
def strPowerModel(Features, StrCurrent):
    #Libear model
    lm = LinearRegression()
    lm.fit(Features,StrCurrent)
    return lm
    
#Step 4: Fault detection for individual string
def strFaultDetection(Features, StrCurrent):
    lm = strPowerModel(Features, StrCurrent)
    """using model to check new data for faults
        grab test data from database, using last 10 days in June
        Method 1: directly compare difference error > 10%
    """
    testX = [000]#update to real data from database
    testY = [000]
    predY = lm.predict(testX)
    resErr = (testY-predY)/testY*100
    #set resErr > 10 to Fault label in restult file
    
#Step 5: Summarize fault detection results for ground truth comparison
def rankFaultString():
    pass
    

#Main
def main():
    pass

if __name__ == "__main__":
    main()

#Alert! Thinking programming in multi-processing ways and easier to configure with
#new alsogithms and data pre-processing methods

