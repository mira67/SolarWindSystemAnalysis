#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:50:30 2017

@author: zhaoyingying
"""


import pandas as pd
#import matplotlib.pyplot as plt
from ggplot import ggplot,aes,geom_point,ggtitle

from sklearn.manifold import TSNE

n_sne = 1034



#inPath = '/Users/zhaoyingying/PVData/ADIbyCen/ADIALLTimeSeriesrenameType_rawsignal.csv'

inPath = '/Users/zhaoyingying/PVData/ADIbyCen/FFTADIALLTimeSeries_rawsignal_fmt_forPlot.csv'
#outPath = '/Users/zhaoyingying/PVData/ADIbyCen/shape_tsne.csv'
outPath = '/Users/zhaoyingying/PVData/ADIbyCen/fft_tsne.csv'
def tsne():
    tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
    df = pd.read_csv(inPath, header= None)
    tsne_results = tsne.fit_transform(df.iloc[:n_sne,1:-1].values)
    #df_tsne = df.iloc[:n_sne,1:-1].copy()
    df_tsne = pd.DataFrame()
    df_tsne['Type']= df.iloc[:,0]
    df_tsne['x-tsne'] = tsne_results[:,0]
    df_tsne['y-tsne'] = tsne_results[:,1]
    #df_tsne_plot = pd.DataFrame(columns=['#Type','#type1-x-tsne','type1-y-tsne','type2-x-tsne','type2-y-tsne','type3-x-tsne','type3-y-tsne','type4-x-tsne','type4-y-tsne','type5-x-tsne','type5-y-tsne'])
    # results['Method'] = pd.DataFrame(data=method, columns=['Method'])
 
    print(df_tsne.iloc[0:475,1:3])
    df_tsne_t1 =df_tsne.iloc[0:475,1:3].copy()
    df_tsne_t2 =df_tsne.iloc[475:704,1:3].copy()
    df_tsne_t2.index = range(len(df_tsne_t2))
    df_tsne_t3 =df_tsne.iloc[704:900,1:3].copy()
    df_tsne_t3.index = range(len(df_tsne_t3))
    df_tsne_t4 =df_tsne.iloc[904:,1:3].copy()
    df_tsne_t4.index = range(len(df_tsne_t4))
    df_tsne_t5 =df_tsne.iloc[900:904,1:3].copy()
    df_tsne_t5.index = range(len(df_tsne_t5))
    res = pd.concat([df_tsne_t1, df_tsne_t2, df_tsne_t3,df_tsne_t4,df_tsne_t5],axis=1)
    

    
   # df_tsne_plot['#type1-x-tsne','type1-y-tsne']=pd.DataFrame(data=df_tsne.iloc[0:475,1:3])
                 
                

                                            
                                         
    res.to_csv(outPath)

if __name__ == '__main__':
    tsne()