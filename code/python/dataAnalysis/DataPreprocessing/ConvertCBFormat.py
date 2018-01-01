#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 10:18:38 2017

@author: zhaoyingying

@func: converter the original download data to the new data format for combiner box
raw file format: HL101, HL102, HL107, etag, s
new file format: #data_date, I1,I10,I11,I12,I13,I14,I15,I16,I2,I3,I4,I5,I5,I7,I8,I9,PV, T
mapping:
PV: HL101
T: HL102
I1~I9: HL107
"""
import pandas as pd
inPath = 'E:/test/'
outPath = 'E:/test/'
def ConverterFormat(path):
    print(path)
    df = pd.read_csv(path)
    with open(path,'r') as f:
        for line in f:
            
    
    
    
            
    
