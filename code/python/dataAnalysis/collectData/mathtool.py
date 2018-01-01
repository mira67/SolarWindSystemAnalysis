#!/usr/bin/python
# coding=utf-8

'''
Created on 2016年10月28日
包含计算数据的数学方法函数

@author: lin
'''

import numpy as np
import datetime
import time
# from _overlapped import NULL


#给定value值  返回在列表list中的位置
def GetIndex(list,value):
    if value in list:
        return list.index(value)
    else:
        return -1

#输入：给定值value、数组、value在数组的第i列、对应的数组第j列
#返回：i列满足value值所对应的j列值
def FindPos(value,entity,list_i,list_j):
    try: 
        pos=[]
        for v in range(0,len(entity)): 
            if value==entity[v][list_i]: 
                pos.append(entity[v][list_j])
        return pos 
    except: 
        print ("FindPos() Exception!")
        
#给定风速计算对应的标准功率
def StdPical(windspeed,power,value):
    index=GetIndex(windspeed, value)
    if index>=0: 
        stdPi=power[index]
    elif value>=10:
        stdPi=2000.00
    else:
        stdPi=0.0
    return stdPi

#计算给定一个列表的平均值
def Mean(value):
    if np.mean(value)!=np.mean(value):
        return NULL
    else:
        return np.mean(value)
    
#计算给定一个列表的标准差
def Std(value):
    if np.std(value)!=np.std(value):
        return NULL
    else:
        return np.std(value)
    
#计算给定一个列表的和
def Sum(value):
    if np.sum(value)!=np.sum(value):
        return NULL
    else:
        return np.sum(value)
    
#计算给定一个列表的最大值
def Max(value):
    if np.max(value)!=np.max(value):
        return NULL
    else:
        return np.max(value)
    
#计算给定一个列表的最小值
def Min(value):
    if np.min(value)!=np.min(value):
        return NULL
    else:
        return np.min(value)

#计算给定一个列表的方差
def Var(value):
    if np.var(value)!=np.var(value):
        return NULL
    else:
        return np.var(value)

#计算给定列表的末尾与首的差 
def Dif(value):
    return value[-1]-value[0]  
 
#计算给定一个列表的湍流（标准差/均值）
def TurbuCal(value ):
    if np.mean(value)==0:
        return -1
    else:
        return np.std(value)/np.mean(value)


# #计算给定一个列表的众数
# from scipy import stats
# def Mode(list):
#     if len(stats.mode(list)[0])>0:
#         mode=int(stats.mode(list)[0][0])
#     else:
#         mode=int(stats.mode(list)[0])
#     return mode

# 众数  
def Mode(arr):  
    mode = [] 
    arr=list(arr)
    arr_appear = dict((a, arr.count(a)) for a in arr)# 统计各个元素出现的次数  
    if max(arr_appear.values()) == 1:  # 如果最大的出现为1  
        return arr[0]  # 则没有众数,默认返回列表第一个值  
    else:  
        for k, v in arr_appear.items():  # 否则，出现次数最大的数字，就是众数  
            if v == max(arr_appear.values()):  
                mode.append(k) 
    return mode[0] 

#计算时间差返回秒  
def Caltime(date1,date2):
    date1=str(date1).split('.')[0]
    date2=str(date2).split('.')[0]
    date1=time.strptime(str(date1),"%Y-%m-%d %H:%M:%S")
    date2=time.strptime(str(date2),"%Y-%m-%d %H:%M:%S")
    date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
    date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
    return ((date2-date1).days)*24*60*60+(date2-date1).seconds

#18位时间戳转化为标准时间
def StamptoTime(value):
    value=float(value)
    epoch=116444736000000000
    timestamp =  float(value-epoch)/10**7
    dateArray = datetime.datetime.utcfromtimestamp(timestamp)
    #转换成新的时间格式(2016-05-05 20:28:54)
    dt = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    return dt

def StamptoBJTime(value):
    value = float(value)
    epoch = 116444448000000000
    timestamp = float(value - epoch) / 10 ** 7
    dateArray = datetime.datetime.utcfromtimestamp(timestamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    dt = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    return dt

#标准时间转化为时间戳
def TimetoStamp(value):
    value=str(value).split('.')[0]
    epoch=116444736000000000

    timeArray = time.strptime(value, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    timeStamp18=timeStamp*10**7+epoch
    return timeStamp18

       
#风速转化为风速区间
def WTspeed(speed):
    if speed==NULL:
        return NULL
    else:
        if speed>=0 and speed<=0.25:
            return 0
        else:
            for i in range(60):
                if speed>=0.25+i*0.5 and speed<=0.25+(i+1)*0.5:
                    return (i+1)*0.5

#风向绝对值计算成16位风向
def WNACDirCalc(WNAC_Dir):
    if WNAC_Dir==NULL:
        return NULL
    else:
        mode_Dir=int(Mode(WNAC_Dir))
        if mode_Dir<11.25 or mode_Dir>=348.75:
            return 1
        else:
            for i in range(2,17):
                low=(i-1)*22.5-11.25
                high=(i-1)*22.5+11.25
                if low<=0:
                    low=360-11.25
                if mode_Dir<high and mode_Dir>=low:
                    return i

if __name__ == '__main__':
    # print(StamptoTime(131487912000000000))
   # print TimetoStamp('2017-10-25 00:00:05')
  #  print TimetoStamp('2017-10-25 00:00:00')
    print (StamptoBJTime('131533632000000000'))
 #   # print(StamptoTime(131491848000000000))
    # print(StamptoTime(131491884000000000))
    # print(StamptoTime(131491890000000000))
    