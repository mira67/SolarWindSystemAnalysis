#PV Estimator Based Fault Detection
#Author: Qi Liu
#Email: qi.liu@colorado.edu

"""Test 1: real-time online detection with raw 1min data without filtering"""

import pymysql.cursors
import numpy as np
from pandas import DataFrame

#Make database connetion
db = pymysql.connect(host='localhost',
                            user='liuqi',
                            password='1234',
                            db='pingyuan',
                            port=3306,
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor,local_infile=True)

cursor=db.cursor()

#Step 1: Extract data from database
def queryStrData(hlxID, strID, startDate,endDate):
    
    sql = """SELECT {} FROM pingyuan.hlx WHERE combinerbox = '{}' 
            AND riqi BETWEEN '{}' AND '{}';"""
    sqlSts = sql.format(strID, hlxID, startDate,endDate)
    print(sqlSts)
    try:
        cursor = db.cursor()
        cursor.execute(sqlSts)
        db.commit()
        
        #collect query data
        df = DataFrame(cursor.fetchall())
        print(df.head())
    except:
        # Rollback in case there is any error
        db.rollback()
        print('Not able to query string %s' % (strID))
        
    #close connection
    cursor.close()
    db.close()

queryStrData('S01-NBA-HL0111','I1','2016-01-01','2016-01-02')
#consider to also write to files for later easier access?

#Step 2: Build model for individual string

#Step 3: Fault detection for individual string

#Step 4: Summarize fault detection results for ground truth comparison

#Alert! Thinking programming in multi-processing ways and easier to configure with
#new alsogithms and data pre-processing methods

