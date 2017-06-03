"""Plot string signals on certain day
   Author: Qi Liu
   Email: qliu.hit@gmail.com
"""

import pandas as pd
import numpy as np
from pvalgs import fdGMM
from sklearn.mixture import GMM
from matplotlib import pyplot as plt
import datetime
import multiprocessing as mp
import glob
import os
import time
import filecmp
from sklearn.cluster import KMeans
from scipy import signal

dateRg = '2016-07-01'
dateName = '#data_date'
stringNum = 16
interval = 10;#every n min sampling
timeRg = ['04:00','20:00'];
inPath = 'E:/myprojects/pv_detection/data/filtered/'
figPath = 'E:/myprojects/pv_detection/data/experiment_results/string_plot_06_02_07_01_2016/'
#column names
colNames = ['I1','I10','I11','I12','I13','I14','I15','I16','I2','I3','I4','I5','I6','I7','I8','I9'];

def plotStrings(fullname):
    # read module    
    print(fullname)
    df = pd.read_csv(fullname)
    # grab certain date range for plotting
    df = df.iloc[::interval,:]
    df_select = df[(df[dateName] > dateRg+' '+timeRg[0]) & (df[dateName] < dateRg+' '+timeRg[1])]
    string_current = df_select.iloc[:,1:stringNum+1].as_matrix()
    # plot time series for all strings
    plt.plot(string_current)
    plt.legend(labels = colNames)
    #save figure to folder
    hlx = os.path.basename(fullname)
    plt.title(hlx[:-4])
    plt.grid()
    #plt.show()
    plt.savefig(figPath+hlx[:-4]+'.png', format='png',dpi=100)
    plt.close()
    
if __name__ == '__main__':
    flist = glob.glob(inPath+'*.csv')
    for fn in flist:
    #fullname = inPath+'S14-NBB-HL13-14.csv'
        plotStrings(fn)