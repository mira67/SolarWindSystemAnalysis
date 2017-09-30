#Create DTW distance matrix
#Author: Qi Liu
#Email: qliu.hit@gmail.com

from ts_classifier import ts_classifier
import numpy as np
import pandas as pd

import time

#global settings
kfold = 3 # cross validation
inPath = 'E:/myprojects/pv_detection/code/python/smoothedTimeSeriesADI.csv'
outPath = 'E:/myprojects/pv_detection/code/python/dtwMatrix.csv'
w = 4

#KNN class
knn = ts_classifier()

#matrix size
num_data = 4
dtw_matrix = np.zeros((num_data, num_data))

#create DTW matrix
def dtwMatrix(data,w):
    for ind_row,i in enumerate(data):
        for ind_col,j in enumerate(data):
            dist = knn.DTWDistance(i,j,w)
            dtw_matrix[ind_row,ind_col] = dist
    return dtw_matrix

#main starting point        
if __name__ == '__main__':
    #profiling
    start = time.time()
    
    data = pd.read_csv(inPath, delimiter=',', header=None)
    nCols = data.shape[1]
    #extract attributes and class target
    data = data.iloc[:,1:nCols].as_matrix()
    
    mymatrix = dtwMatrix(data,w)
    np.savetxt(outPath, mymatrix, delimiter=',')
    
    end = time.time()
    runtime = end - start
    msg = "DTW Creation Tooks {time} seconds to complete"
    print(msg.format(time=runtime))