#-*- coding: UTF-8 -*-
import taskfiles.S27_20170725062335 as s27
import taskfiles.S51_20170731153430 as s51
import taskfiles.S53_20170731153508 as s53
import taskfiles.S56_20170816143439 as s56
import taskfiles.S59_20170731153527 as s59
import taskfiles.S60_20170731153541 as s60
import taskfiles.S73_20170731153914 as s73
import taskfiles.S75_20170731153128 as s75
import taskfiles.S76_20170804082838 as s76
import taskfiles.S77_20170731153945 as s77
import taskfiles.S79_20170731161311 as s79
import taskfiles.S80_20170731161325 as s80
import taskfiles.S83_20170804103223 as s83
import taskfiles.S302_20170816143446 as s302
import taskfiles.S340_20170816143435 as s340
import taskfiles.S350_20170814062951 as s350
import taskfiles.S360_20170814063231 as s360
import taskfiles.S380_20170822154618 as s380
import taskfiles.S392_20170809052238 as s392
import taskfiles.S393_20170816190432 as s393
import taskfiles.S394_20170816143442 as s394
import taskfiles.S401_20170816190906 as s401
import taskfiles.S402_20170816190936 as s402
import taskfiles.S403_20170816191558 as s403
import taskfiles.S406_20170816191627 as s406
import taskfiles.S404_20170816191612 as s404
import taskfiles.S407_20170816191009 as s407
import taskfiles.S502_20170816191028 as s502
from AzureTableHelper import ReadAzureTable
import pandas as pd
import os
import datetime
import time
from data_processed import data_processed


#stationDevice = s350.allDevice # need reverse,eg. shandongpingyuan code is 350, should generate instance s350.allDevice
stationDevice = s56.allDevice # yongren pv farm
path = '/Users/zhaoyingying/PVData/' # need add path
devicetypelist = [202] #201,202,203, type = int, need add device type code

date_duration = ['2017-09-01','2017-09-30']#UTC date
# time_duration = ['20:00:00','12:00:00']#UTE time
# delta_days = datetime.datetime.strptime(date_duration[1][:10], '%Y-%m-%d')-datetime.datetime.strptime(date_duration[0][:10], '%Y-%m-%d')
# for day in range(delta_days.days):
#     day_duration = [date_duration[0]]

azReader = ReadAzureTable()
dataprocess = data_processed()


def gen_datelist(date_duration1):
    datelists = []
    delta_days = datetime.datetime.strptime(date_duration1[1], '%Y-%m-%d')-datetime.datetime.strptime(date_duration1[0], '%Y-%m-%d')
    for day in range(delta_days.days):
        begin = datetime.datetime.strptime(date_duration1[0], '%Y-%m-%d') + datetime.timedelta(days=day,hours=20)
        begintime = datetime.datetime.strftime(begin,'%Y-%m-%d %H:%M:%S')
        end = begin + datetime.timedelta(hours=16)
        endtime = datetime.datetime.strftime(end,'%Y-%m-%d %H:%M:%S')
        datelists.append([begintime,endtime])
    return datelists
        # print begintime,endtime


def selectData(deviceType):
    deviceList = []
    allDevice = stationDevice
    for device in allDevice:
        if device['DeviceTypeCode'] == deviceType:
            deviceList.append([str(device['DeviceModeFullCode']),str(device['DeviceCode'])])
    return deviceList


def writeCsv(df,path,deviceName,date):
    df.to_csv(path + '\\' + deviceName + '_'+date + '.csv',index=False)


def start(deviceType,startTime,endTime):
    deviceList = selectData(deviceType)
    # print deviceList
    for device in deviceList:
        df = azReader.readData(device[1], device[0], startTime, endTime)
        if df is None:
            print ('error,but pass')
        else:
            df = dataprocess.hlx_processed_offline(df=df)
            deviceName = device[0] + 'M' + device[1]
            stationName1,deviceName1,devicetypeName,deviceId \
                = deviceName.split('M')[0],deviceName.split('M')[1],\
                  deviceName.split('M')[2],deviceName.split('M')[3]
            # print stationName1,deviceName1,devicetypeName,deviceId
            if os.path.exists(path+'\\'+str(stationName1)+'\\'+str(deviceName1)+'\\'+endTime[:10]):
                path1 = path+'\\'+str(stationName1)+'\\'+str(deviceName1)+'\\'+endTime[:10]
                writeCsv(df=df, path=path1, deviceName=deviceName, date=endTime[:10])
            else:
                os.makedirs(path+'\\'+str(stationName1)+'\\'+str(deviceName1)+'\\'+endTime[:10])
                path2 = path + '\\' + str(stationName1) + '\\' + str(deviceName1) + '\\' + endTime[:10]
                writeCsv(df=df, path=path2, deviceName=deviceName, date=endTime[:10])



def main_strat():
    pass

if __name__ == '__main__':
    # start(202,'2017-08-01 00:00:00','2017-08-01 01:00:00')
    starttime = time.time()

    datelists = gen_datelist(date_duration)
    for devicetype in devicetypelist:
        for datedetail in datelists:
            start(deviceType=devicetype,startTime=datedetail[0],endTime=datedetail[1])
    endtime = time.time()
    print ('download Data use :%s sencods'%(endtime-starttime))

    # print delta_days.days



    # df = azReader.readData('3', '350M201M2', '2017-07-09 00:00:00', '2017-07-09 01:00:00')

