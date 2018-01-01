import pandas as pd
import numpy as np
from mathtool import StamptoBJTime
import glob
import os
from scipy import signal
from transformCB import hlx_processed_offline
CurrentColumns = ['I1', 'I10', 'I11', 'I12', 'I13', 'I14', 'I15', 'I16', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9','PV','T','mean','median','std','var']

class preprocess(object):

    def __init__(self):
        pass

    def medfilter_plus(self,df,existString):
        newColumns = ['TimeStamp','I1', 'I10', 'I11', 'I12', 'I13', 'I14', 'I15', 'I16', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9','PV','T','mean','median','std','var']
        #for i in range(df.iloc[:, 1:17].shape[1]):
            #df.iloc[:, 1:17].iloc[:, i] = signal.medfilt(df.iloc[:, 1:17].iloc[:, i], 721)
        df.iloc[:, 1:17] = df.iloc[:, 1:17].rolling(720).median()
        df.loc[:, 'mean'] = df.loc[:, existString].mean(axis=1)
        df.loc[:, 'median'] = df.loc[:, existString].median(axis=1)
        df.loc[:, 'std'] = df.loc[:, existString].std(axis=1)
        df.loc[:, 'var'] = df.loc[:, existString].var(axis=1)
        return df

    def transform_format(self,df):
        StringName = ['TimeStamp', 'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'I11', 'I12', 'I13','I14', 'I15', 'I16', 'PV', 'T']
        df.columns = StringName
        return df


if __name__ == '__main__':
    preprocess = preprocess()
    df_existString = pd.read_excel('F:PVData/yongren.xlsx',index_col='new')
    df_existString = df_existString.fillna(0)
    print (df_existString.index)
    for csvfile in glob.glob('F:/PVData/test/adcTest/2017-08-05/'+'*.csv'):
        try:
            combinerbox = os.path.basename(csvfile[:-15])
            existString = df_existString.loc[combinerbox,'I1':'I16']
            existString = existString[existString==1].index
            df = pd.read_csv(csvfile)
            # df = preprocess.transform_format(df)
            df = preprocess.medfilter_plus(df,existString)

            df.to_csv('F:/PVData/test/adcTest/2017-08-15_medfilter/'+combinerbox + '_preprocessed.csv', index=False)
        except ValueError:
            print ('Oops! That was no valid number....')