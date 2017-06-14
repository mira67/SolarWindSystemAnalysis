#Create DTW distance matrix
#Author: Qi Liu
#Email: qliu.hit@gmail.com

from ts_classifier import ts_classifier
import numpy as np
import pandas as pd
import threading

import time

#global settings
kfold = 3 # cross validation
inPath = 'E:/myprojects/pv_detection/code/python/sortedADI.csv'
outPath = 'E:/myprojects/pv_detection/code/python/dtwMatrix-4.csv'
w = 4

#KNN class
knn = ts_classifier()

#matrix size
num_data = 968

dtw_matrix = np.zeros((num_data, num_data))
rowStartline = 323
rowEndline = 646
colStartline= 323
colEndline = 646
#create DTW matrix
def dtwMatrix(data,w,rst,ren,cst,cen):
    for ind_row,i in enumerate(data):
        if(ind_row>=rst and ind_row<ren):
            for ind_col,j in enumerate(data):
                if(ind_col>=cst and ind_col<cen):
                    if(ind_col>ind_row):
                        dist = knn.DTWDistance(i,j,w)
                        dtw_matrix[ind_row,ind_col] = dist
    #return dtw_matrix


 # the dtw matrix is symmetrical
def dtwMatrixSys():
    for ind_row,i in enumerate(dtw_matrix):
        for ind_col,j in enumerate(dtw_matrix):
            if(ind_col==ind_row):
                dtw_matrix[ind_row,ind_col] = 0.0
            if(ind_col<ind_row):
                dtw_matrix[ind_row,ind_col] = dtw_matrix[ind_col,ind_row]
    return dtw_matrix

#main starting point        
if __name__ == '__main__':
    #profiling
    start = time.time()
    
    data = pd.read_csv(inPath, delimiter=',', header=None)
    nCols = data.shape[1]

    #extract attributes and class target
    data = data.iloc[:,1:nCols-1].as_matrix()
    dtwMatrix(data,w,rowStartline,rowEndline,colStartline,colEndline)
    #mu = threading.Lock
    #threads =[]s
    #t1 = threading.Thread(target=dtwMatrix,args=(data,w,0,1)) #write dtw_matrix from the 0-the line to the 1-th line
    #threads.append(t1)
    #t2 = threading.Thread(target=dtwMatrix,args=(data,w,1,2))
    #threads.append(t2)
    #t3 = threading.Thread(target=dtwMatrix,args=(data,w,2,3))
    #threads.append(t3)
    #t4 = threading.Thread(target=dtwMatrix,args=(data,w,3,4))
    #threads.append(t4)
    #for t in threads:
    #    t.setDaemon(True)
    #    t.start()
    
    mymatrix = dtwMatrixSys()
    np.savetxt(outPath, mymatrix, delimiter=',', fmt = '%.6f')
    
    end = time.time()
    runtime = end - start
    msg = "DTW Creation Tooks {time} seconds to complete"
    print(msg.format(time=runtime))