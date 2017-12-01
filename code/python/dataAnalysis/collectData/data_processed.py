import pandas as pd
import numpy as np
from mathtool import StamptoTime
import glob


class data_processed:

    def __init__(self):
        self.path = 'C:\Users\Pan\Desktop\\test'
        self.StringName = ['I1','I10','I11','I12','I13','I14','I15','I16','I2','I3','I4','I5','I6','I7','I8','I9']

    def hlx_processed(self,df):
        # for csvfile in glob.glob(self.path + '\\' + stationName + '\\' + hlxName + '\\' + date + '\\' + '*.csv'):
        df = df.loc[:,['s','HL107','HL101','HL102']]
        for i in range(df.shape[0]):
            df.loc[i, 's'] = StamptoTime(df.loc[i, 's'])
            for inx, j in enumerate(self.StringName):
                df.loc[i, j] = df.loc[i, 'HL107'].split(',')[inx]
        df.drop('HL107', axis=1, inplace=True)
        return df

    def hlx_processed_offline(self,stationName,hlxName,date):
        for csvfile in glob.glob(self.path + '\\' + stationName + '\\' + hlxName + '\\' + date + '\\' + '*.csv'):
            df = pd.read_csv(csvfile)
            df = df.loc[:,['s','HL107','HL101','HL102']]
            for i in range(df.shape[0]):
                df.loc[i,'s'] = StamptoTime(df.loc[i, 's'])
                for inx, j in enumerate(self.StringName):
                    df.loc[i, j] = df.loc[i, 'HL107'].split(',')[inx]
            df.drop('HL107', axis=1, inplace=True)
            df.rename(columns={'s': 'TimeStamp', 'HL101': 'PV','HL102':'T'}, inplace=True)
            cols = list(df)
            cols.insert(18,cols.pop(cols.index('PV')))
            cols.insert(18,cols.pop(cols.index('T')))
            df =df.ix[:,cols]
            df.to_csv(csvfile,index=False)


if __name__ == '__main__':
    process = data_processed()
    process.hlx_processed_offline('350','202','2017-07-01')





# StringName = ['I1','I10','I11','I12','I13','I14','I15','I16','I2','I3','I4','I5','I6','I7','I8','I9']
# path = 'C:\Users\Pan\Desktop\\test\\350\\202\\2017-07-01'
# df = pd.read_csv(path+'\\' + '350M202M3M490_2017-07-01.csv')
# df = df.loc[:,['RowKey','HL107']]
# for i in range(df.shape[0]):
#     df.loc[i,'RowKey'] = StamptoTime(df.loc[i,'RowKey'])
#     for inx,j in enumerate(StringName):
#         df.loc[i,j] = df.loc[i,'HL107'].split(',')[inx]
# df.drop('HL107',axis =1,inplace = True)
# print df
#        for df1 in glob.glob(self.path+'\\'+stationName+'\\'+deviceName+'\\'+date+'\\'+'*.csv'):
