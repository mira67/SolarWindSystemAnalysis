#PV Fault Classification using DTW and K-NN
#Author: Qi Liu
#Email: qliu.hit@gmail.com

import ts_classifier as tsc
import numpy as np
import pandas as pd 

#dataset partition to train and test
def PVPartition(file):
    return 'ok'

#classification
def PVKNN(train,test,w):
    preds=[]
    for ind,i in enumerate(test):
        min_dist=float('inf')
        closest_seq=[]
        #print ind
        for j in train:
            if tsc.LB_Keogh(i[:-1],j[:-1],5)<min_dist:
                dist=tsc.DTWDistance(i[:-1],j[:-1],w)
                if dist<min_dist:
                    min_dist=dist
                    closest_seq=j
        preds.append(closest_seq[-1])
    return tsc.classification_report(test[:,-1],preds)
    
if __name__ == '__main__':
    kfold = 5 # cross validation
    
    
    print 'ok'