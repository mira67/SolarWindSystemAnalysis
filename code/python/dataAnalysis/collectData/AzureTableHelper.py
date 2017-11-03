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
        self.station = pd.read_csv('station.csv')
        self.deviceType = pd.read_csv('deviceType.csv')
        self.deviceMode = pd.read_csv('deviceMode.csv')

    def readData(self,deviceCode,deviceModeCode,startTime,endTime):
        sTime=parser.parse(startTime)
        #print(sTime)
        eTime=parser.parse(endTime)
       # print(eTime)
        sRowKey=mathtool.TimetoStamp(sTime) #用来把时间转换为TimeStamp
        eRowKey=mathtool.TimetoStamp(eTime)

        azureTableNameSuffix = 'T' + sTime.strftime('%Y%m') + 'PT' + str(self.PT_azuretable) + 'S'
        filter_string = 'PartitionKey eq ' + '\'' + str(deviceCode) + '\'' + ' and RowKey ge ' + '\'' + str(
                sRowKey) + '\'' + ' and RowKey le ' + '\'' + str(eRowKey) + '\''
        tableName='S' + str(deviceModeCode) + azureTableNameSuffix
        tasks = self.table_service.query_entities(tableName,filter_string)
        rows_list = []
        for item in tasks:
            rows_list.append(item)

        df = pd.DataFrame(rows_list)

        return df

    def BaseInformation(self):
        pass


if __name__ == '__main__':
    azReader=ReadAzureTable()
    df=azReader.readData('3','350M201M2','2017-07-09 00:00:00','2017-07-09 01:00:00')
    print (df)
    # print azReader.deviceMode[azReader.deviceMode['DeviceModeCode'] == 4]

    
