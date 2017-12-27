import pandas as pd
from mathtool import StamptoTime
import glob
import time
import multiprocessing as mp
import dataprocess_cms as dp
from mathtool import StamptoBJTime
import threading
import numpy as np

# converter all combiner box format in a pv system: 56 stands for yongwen site!
inPath = 'F:/PVData/350/202/'
#inPath = 'F:/PVData/test/adcTest/'

def hlx_processed_offline(fullname):
    """
    tranfrom the combiner box format from the Table in azure to the currently used format:
    Timestamp, 'I1','I10','I11','I12','I13','I14','I15','I16','I2','I3','I4','I5','I6','I7','I8','I9', PV ,T
    """
    # print(fullname)
    StringName = ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'I11', 'I12', 'I13', 'I14', 'I15', 'I16']
    transform_col = ['TimeStamp','I1', 'I10', 'I11', 'I12', 'I13', 'I14', 'I15', 'I16', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9','PV','T']
    df = pd.read_csv(fullname)
    df = df[df['HL107'].isnull() == False].reset_index()
    df = df.loc[:, ['s', 'HL107', 'HL101', 'HL102']]
    # hlx = df['HL107']
    # hlx1 = hlx.apply(lambda x: pd.Series(x.split(',')))
    #
    # print hlx1
    # print df.count(axis=1)
    for i in range(df.shape[0]):
        df.loc[i, 's'] = StamptoBJTime(df.loc[i, 's'])
        # print(df.loc[i, 's'])

        # get 16 strings' current
        # for inx, j in enumerate(StringName):
        #     #
        #     # if str(df.loc[i, 'HL107']) == 'nan':
        #     #     break
        #     df.loc[i, j] = str(df.loc[i, 'HL107']).split(',')[inx]
    hlx = df['HL107'].apply(lambda x: pd.Series(x.split(',')))
    hlx.columns = StringName
    # print hlx
    df.drop('HL107', axis=1, inplace=True)
    df.rename(columns={'s': 'TimeStamp', 'HL101': 'PV', 'HL102': 'T'}, inplace=True)
    df = df.join(hlx)
    # cols = list(df)
    # cols.insert(18, cols.pop(cols.index('PV')))
    # cols.insert(18, cols.pop(cols.index('T')))
    df = df.ix[:, transform_col]
    df.to_csv(fullname, index=False)
    # return df
    # print df


if __name__ == '__main__':

    # traverse all folder
    #folderlist = glob.glob(inPath+'\*.csv')

    # print folderlist[1111]
    # hlx_processed_offline(folderlist[2222])
    # print folderlist
    folderlist = dp.each_file(inPath, 0)
    #print(folderlist)
    for i in range(len(folderlist)):
         flist = glob.glob(folderlist[i] + '/*.csv')
    #print(flist)
    #     print(folderlist[i])
    #     for f in flist:
    #         data_processed.hlx_processed_offline(f)
    # print folderlist[1586]
    # data_processed.hlx_processed_offline(folderlist[1586])


    # print mp.cpu_count()



    mp.freeze_support()
    pool = mp.Pool(3)
    for i in range(len(flist)):
        #print (folderlist[i])
        try:
            pool.apply_async(hlx_processed_offline,args=(flist[i],))
        except ValueError:
            print ('Oops! That was no valid number....')
       # except BaseException as e:
            #print ('error but pass,this exception is %s'%e)


    pool.close()
    pool.join()

    print ('finish')




    # threads = []
    # for num in folderlist:
    #     threads.append(threading.Thread(target=data_processed.hlx_processed_offline, args=(num,))
    #
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    # t.join()

    # """
    # pool = mp.Pool(3)
    # results = pool.map(process.hlx_processed_offline, flist)
    # """
