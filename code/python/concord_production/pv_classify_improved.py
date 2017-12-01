import pandas as pd
from sklearn.metrics import mean_squared_error
import numpy as np
from ts_classifier import ts_classifier



# =============================================================================
# inpath = glob.glob('C:\Users\Pan\Desktop\svd\\'+'*rate.csv')
# standard = 'C:\Users\Pan\Desktop\svd\\SVD.csv'
# adi_inpath = 'C:\Users\Pan\Desktop\\test\\adi\\'
# =============================================================================
sampling_interval = 20 


# =============================================================================
# def fillna(inpath1):
#     for csvfile in inpath1:
#         df = pd.read_csv(csvfile)
#         mean_value = df.mean(axis = 1)
#         index = df[df.isnull().values == True].index
#         for i in index:
#             df.loc[i,df.iloc[i,:].isnull() == True] = mean_value[i]
#         # print df
#         df.to_csv(csvfile,index=False)
# 
# 
# def calculate_mse(inpath1,standard1):
#     df_true = pd.read_csv(standard1)
#     true_value = df_true.loc[:,'I1']
#     for csvfile in inpath1:
#         title = os.path.basename(csvfile[:-4])
#         df = pd.read_csv(csvfile)
#         pred_value = df.loc[:,'I1']
#         mse_value = mean_squared_error(true_value,pred_value)
#         print ('with %s none value, the MSE:%s'%(title,mse_value))
# =============================================================================


def calculate_adi_dist(test_adi_path,standard_adi_path,step_interval=None):
    df_testAdi = pd.read_csv(test_adi_path,header=None)
    df_standardAdi = pd.read_csv(standard_adi_path,header=None)
    if step_interval:
        df_standardAdi.iloc[:, 1:-1] = df_standardAdi.iloc[:,1:-1].iloc[:,::step_interval]
        df_standardAdi.dropna(axis=1,inplace=True)
        df_standardAdi.headers= None
    df_dist = df_testAdi.iloc[:,[0,-1]]
    df_dist.columns = ['StringName-TimeStamp','label']
    # print df_standardAdi
    train = df_testAdi.iloc[:,1:-1].as_matrix()
    test = df_standardAdi.iloc[:,1:-1].as_matrix()
    dists = pvKNN(train,test)
    df_dist=df_dist.copy()
    print(df_standardAdi.shape[0])
    for i in range(df_testAdi.shape[0]):
        print(dists[i])
        print(i)
        #df_dist.loc[i,'dist'] = dists[i]
        
        df_dist.loc[i,'dist'] = dists[i]
    
    print(df_dist['dist'].min())
    df_dist.iloc[:,2] = (df_dist['dist']-df_dist['dist'].min())/(df_dist['dist'].max()-df_dist['dist'].min())
    print(df_dist)
    df_dist.to_csv(outPath)
    return df_dist
    # print df_dist
    # for i in range(df_standardAdi.shape[0]):
    #     standardshape = df_standardAdi.iloc[i,1:].as_matrix().reshape(1,df_standardAdi.shape[1]-1)
    #     for ind,j in enumerate(df_testAdi):
    #         testadi = df_testAdi.iloc[j,1:].as_matrix().reshape(1,df_testAdi.shape[1]-1)
    #         dist = ts_classifier().DTWDistance(standardshape[:-1],testadi[:-1],w=5)
    #         print dist

    #         df_dist.loc[ind,'dist'] = dist
    # return df_dist
 
def pvKNN(train,test):
    dists = []
    for ind,i in enumerate(test):
        for ind_j,j in enumerate(train):
            dist = ts_classifier().DTWDistance(i[:-1],j[:-1],4)
            dists.append(dist)

    return dists


if __name__ == '__main__':

    test_adi_path = '/Users/zhaoyingying/PVData/ADIbyCen/processedtimeSeriesADIType.csv'
   # test_adi_path = '/Users/zhaoyingying/PVData/ADIbyCen/test.csv'
    standard_adi_path = '/Users/zhaoyingying/PVData/ADIbyCen/standardshape.csv'
    outPath='/Users/zhaoyingying/PVData/ADIbyCen/DisWithStd.csv'
    calculate_adi_dist(test_adi_path,standard_adi_path,sampling_interval)

