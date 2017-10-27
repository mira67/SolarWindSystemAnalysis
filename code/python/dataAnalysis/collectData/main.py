#-*- coding: UTF-8 -*-
"""
@function: download data collected from different PV systems


"""
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
import dataprocess_cms as dp


stationDevice = s350.allDevice # need reverse,eg. shandongpingyuan code is 350, should generate instance s350.allDevices
#choice pv systems
stationName = 'pingyuan'

# add path for weather station
WSpath = '/Users/zhaoyingying/PVData/FiveSecondsData/rawdata/'+stationName+'/weatherStation/' 
#add path for combinerbox
CBpath = '/Users/zhaoyingying/PVData/FiveSecondsData/rawdata/'+stationName+'/combierBox/' 
#add path for converter
CTpath = '/Users/zhaoyingying/PVData/FiveSecondsData/rawdata/'+stationName+'/converter/' 
#201: converter , 202: combiner box, 203: weather station
devicetypelist = [201,202,203]
#get a time period of data
datelists = ['2017-09-01 00:00:00','2017-09-01 23:59:59']


def selectData(deviceType):
    deviceList = []
    allDevice = stationDevice
    for device in allDevice:
        if device['DeviceTypeCode'] == deviceType:
            deviceList.append([str(device['DeviceModeFullCode']),str(device['DeviceCode'])])
    return deviceList


def writeCsv(df,path,deviceName,date):
    #create the ouput path
    dp.mkdir(path)
    #output to file
    df.to_csv(path + deviceName + '_'+date + '.csv',index=False)


def start(deviceType,startTime,endTime):
    azReader = ReadAzureTable()
    deviceList = selectData(deviceType)
    for device in deviceList:
        print('device[1]:'+device[1])
        print('device[0]:'+device[0])
        print(startTime)
        print(endTime)
        df = azReader.readData(device[1], device[0], startTime, endTime)
        deviceName = device[0] + 'M' + device[1]

        #choice different out put path for different device
        if deviceType == 201:
            path = CTpath
        if deviceType == 202:
            path = CBpath
        if deviceType == 203:
            path = WSpath
        writeCsv(df=df,path=path,deviceName=deviceName,date=endTime[:10])

if __name__ == '__main__':
   # start(201,'2017-07-09 00:00:00','2017-07-09 01:00:00')

    for idx in range(len(devicetypelist)):
        deviceType = devicetypelist[idx]
        startTime = datelists[0]
        endTime = datelists[1]
        print(startTime)
        print(endTime)
        start(deviceType,startTime,endTime)    

   # df = azReader.readData('3', '350M201M2', '2017-07-09 00:00:00', '2017-07-09 01:00:00')

