#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
# import queue
import datetime
from dateutil import parser
import taskscript_config as tc
import pandas as pd
from azure.storage.table import TableService, Entity
import mathtool


class ReadAzureTable(object):

    def __init__(self):
        self.table_service = TableService(account_name=tc.account_name, account_key=tc.account_key,endpoint_suffix=tc.endpoint_suffix) 
        self.PT_azuretable=5
        # self.station = pd.read_csv('station.csv')
        # self.deviceType = pd.read_csv('deviceType.csv')
        # self.deviceMode = pd.read_csv('deviceMode.csv')

    def readData(self,deviceCode,deviceModeCode,startTime,endTime):
        '''
            deviceCode='350M202M4M2' #需要访问的设备编号

        '''
        sTime=parser.parse(startTime)
        eTime=parser.parse(endTime)
        # print (startTime)
        # print (endTime)
        print (type(eTime))
        print ((sTime))
        sRowKey=mathtool.TimetoStamp(sTime) #用来把时间转换为TimeStamp
        eRowKey=mathtool.TimetoStamp(eTime)
        # print (sRowKey)
        # print (eRowKey)

        if sTime.month == eTime.month:
            azureTableNameSuffix = 'T' + sTime.strftime('%Y%m') + 'PT' + str(self.PT_azuretable) + 'S'
            filter_string = 'PartitionKey eq ' + '\'' + str(deviceCode) + '\'' + ' and RowKey ge ' + '\'' + str(
                    sRowKey) + '\'' + ' and RowKey le ' + '\'' + str(eRowKey) + '\''
            tableName='S' + str(deviceModeCode) + azureTableNameSuffix
            distinguish_hlx = deviceModeCode.split('M')[1]
            selectStr = 'HL101,HL102,HL107,s'
            print (tableName)
            try:
                if distinguish_hlx == '202':
                    tasks = self.table_service.query_entities(tableName, filter_string,select=selectStr)
                else:
                    tasks = self.table_service.query_entities(tableName,filter_string)
                rows_list = []
                for item in tasks:
                    rows_list.append(item)

                df = pd.DataFrame(rows_list)

                return df
            except:
                print ('cannot find the specific table:%s'%tableName)
                return None
        else:
            azureTableNameSuffix1 = 'T' + sTime.strftime('%Y%m') + 'PT' + str(self.PT_azuretable) + 'S'
            azureTableNameSuffix2 = 'T' + eTime.strftime('%Y%m') + 'PT' + str(self.PT_azuretable) + 'S'
            filter_string = 'PartitionKey eq ' + '\'' + str(deviceCode) + '\'' + ' and RowKey ge ' + '\'' + str(
                                sRowKey) + '\'' + ' and RowKey le ' + '\'' + str(eRowKey) + '\''
            tableName1 = 'S' + str(deviceModeCode) + azureTableNameSuffix1
            tableName2 = 'S' + str(deviceModeCode) + azureTableNameSuffix2
            distinguish_hlx = deviceModeCode.split('M')[1]
            selectStr = 'HL101,HL102,HL107,s'
            try:
                if distinguish_hlx == '202':
                    tasks1 = self.table_service.query_entities(tableName1, filter_string, select=selectStr)
                    tasks2 = self.table_service.query_entities(tableName2, filter_string, select=selectStr)
                else:
                    tasks1 = self.table_service.query_entities(tableName1, filter_string)
                    tasks2 = self.table_service.query_entities(tableName2, filter_string)
                rows_list = []
                for item1 in tasks1:
                    rows_list.append(item1)
                for item2 in tasks2:
                    rows_list.append(item2)

                df = pd.DataFrame(rows_list)

                return df
            except:
                print ('cannot find the specific table:%s or %s' % (tableName1,tableName2))
                return None


    def BaseInformation(self):
        pass


if __name__ == '__main__':
    start = time.time()
    azReader=ReadAzureTable()
    df=azReader.readData('492','350M202M3','2017-08-31 23:00:00','2017-09-01 01:00:00')
    # df.to_csv('C:\Users\Pan\Desktop\\article\classify\python\labelledRowData\\350M202M3M492.csv',index=False)
    end = time.time()
    print (df)
    print ('consume time:%s seconds'%(end-start))

    # df = pd.read_csv('C:\Users\Pan\Desktop\\article\classify\python\labelled.csv')
    # print df['after'].unique()

    
