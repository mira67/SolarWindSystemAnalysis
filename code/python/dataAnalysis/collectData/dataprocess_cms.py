# -*- coding: utf-8 -*-
import sys,os
import pandas as pd
import csv
import time

from multiprocessing import Process

def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        print(path + ' 创建成功')
        # 创建目录操作函数
        os.makedirs(path)
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False

# 遍历指定目录，file_type=0显示所有文件夹  file_type=1显示所有文件
def each_file(filepath, file_type):
    pathDir = os.listdir(filepath)
    childs = []
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, '/' + allDir))
        #print(child) # .decode('gbk')是解决中文显示乱码问题
        if file_type == 0:
            if os.path.isdir(child):
                childs.append(child)
        else:
            if os.path.isfile(child):
                childs.append(child)

    return childs

#移除含有*****的行
def removeDuplicateLines(inputfile,outputfile):
    open(outputfile,'w',newline='')
    csv_reader = csv.reader(open(inputfile, encoding='utf-8'))
    for row in csv_reader:
        if '****' not in row[2]:
            with open(outputfile,'a',newline='', encoding='utf-8') as data:
                writer = csv.writer(data)
                writer.writerow(row)

def data_transfer(input_file, output_file):

    f = open(input_file, 'r') #encoding='gbk'))
    temp = []
    for row in f:
        temp.append(row.replace('\n', ''))

    f1 = open(output_file, "w")
    for i in range(0, 7):
        f1.write(str(temp[i]) + '\n')

    data = temp[7].split(' ')
    for dat in data:
        f1.write(str(dat) + '\n')

    f.close()
    f1.close()


def process(v):

    sup_all_file = each_file(v + '/' + v.split('/')[-1], 0)
    print(sup_all_file)
    for w in sup_all_file:
        folder = each_file(w, 0)
        file = each_file(w, 1)

        for fol in folder:
            pass
            output_path = '../data/cms/' + fol.split('/')[-3] + '/' + fol.split('/')[-2] + '/' + fol.split('/')[
                -1] + '/'
            mkdir(output_path)
            fol_file = each_file(fol, 1)
            for bo in fol_file:
                output_file = output_path + '/' + bo.split('/')[-1]
                isExists = os.path.exists(output_file)
                if not isExists:
                    data_transfer(bo, output_file)


        for fi in file:
            pass
            output_path = '../data/cms/' + fi.split('/')[-3] + '/' + fi.split('/')[-2] + '/' + '长波形' + '/'
            mkdir(output_path)

            output_file = output_path + '/' + fi.split('/')[-1]
            isExists = os.path.exists(output_file)
            if not isExists:
                data_transfer(fi, output_file)

if __name__=="__main__":

    '''
        处理cms
    '''
    pass

    all_file = each_file('h:/CMSdata/莲花山CMS数据', 0)
    print(all_file)
    print(all_file[0] + '/' + all_file[0].split('/')[-1])

    jobs = []
    for v in all_file:
        p = Process(target=process, args=(v,))
        print('创建进程 ' + v)
        p.start()
        jobs.append(p)

    for p in jobs:
        p.join()