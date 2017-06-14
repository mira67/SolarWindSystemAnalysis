#Create DTW distance matrix
#Author: Qi Liu
#Email: qliu.hit@gmail.com

from ts_classifier import ts_classifier
import numpy as np
import pandas as pd
import multiprocessing


import time

#global settings
kfold = 3 # cross validation
inPath = 'E:/myprojects/pv_detection/code/python/test.csv'
outPath = 'E:/myprojects/pv_detection/code/python/dtwMatrix.csv'
w = 4

#KNN class
knn = ts_classifier()

#matrix size
num_data = 8#968

#global dtw_matrix = np.zeros((num_data, num_data))

#create DTW matrix
def dtwMatrix(shared,data,w,startline,endline):
    for ind_row,i in enumerate(data):
        if(ind_row>=startline and ind_row<endline):
            for ind_col,j in enumerate(data):
                if(ind_col>ind_row):
                    dist = knn.DTWDistance(i,j,w)
                    shared[ind_row,ind_col] = dist

#main starting point        
if __name__ == '__main__':
    #profiling
    start = time.time()
    
    data = pd.read_csv(inPath, delimiter=',', header=None)
    nCols = data.shape[1]

    #extract attributes and class target
    data = data.iloc[:,1:nCols-1].as_matrix()
    jobs = []
    listk = [[0,2],[2,4],[4,6],[6,8]];
    # dtw_matrix = np.zeros((num_data, num_data))
    shared_data = multiprocessing.Array ('i', (0,0)) #a shared array
    
    for i in range(4):
        p = multiprocessing.Process(target=dtwMatrix, args=(shared_data,data,w,listk[i][0],listk[i][1]))
        jobs.append(p)
        p.start()
    
    #mymatrix = dtwMatrix()
    np.savetxt(outPath, shared_data, delimiter=',')
    
    end = time.time()
    runtime = end - start
    msg = "DTW Creation Tooks {time} seconds to complete"
    print(msg.format(time=runtime))