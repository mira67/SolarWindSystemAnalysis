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



inPath = '/Users/zhaoyingying/PVData/ADIbyCen/ADIALLTimeSeriesrenameId_rawsignal.csv'
outPath = '/Users/zhaoyingying/PVData/ADIbyCen/shape_tsne.csv'
def tsne():
    tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
    df = pd.read_csv(inPath, header= None)
    tsne_results = tsne.fit_transform(df.iloc[:n_sne,1:-1].values)
    #df_tsne = df.iloc[:n_sne,1:-1].copy()
    df_tsne = pd.DataFrame()
    df_tsne['x-tsne'] = tsne_results[:,0]
    df_tsne['y-tsne'] = tsne_results[:,1]
    print(df_tsne)
    df_tsne.to_csv(outPath)

if __name__ == '__main__':
    tsne()