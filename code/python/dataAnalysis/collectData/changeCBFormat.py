import pandas as pd
from mathtool import StamptoTime
import glob
import time
#import multiprocessing as mp
import dataprocess_cms as dp
from mathtool import StamptoBJTime

#converter all combiner box format in a pv system: 56 stands for yongwen site!
inPath = 'F:/PVData/56/202/'


class data_processed:
    

    def __init__(self):

        self.StringName = ['I1','I10','I11','I12','I13','I14','I15','I16','I2','I3','I4','I5','I6','I7','I8','I9']
   
    def hlx_processed_offline(self,fullname):
        """
        tranfrom the combiner box format from the Table in azure to the currently used format:
        Timestamp, 'I1','I10','I11','I12','I13','I14','I15','I16','I2','I3','I4','I5','I6','I7','I8','I9', PV ,T
        """
        print(fullname)

        df = pd.read_csv(fullname)
        df = df.loc[:,['s','HL107','HL101','HL102']]
        for i in range(df.shape[0]):
            df.loc[i,'s'] = StamptoBJTime(df.loc[i, 's'])  
            print(df.loc[i,'s'])
            
            #get 16 strings' current
            for inx, j in enumerate(self.StringName):
                
                if str(df.loc[i, 'HL107']) == 'nan':
                    break
                df.loc[i, j] = str(df.loc[i, 'HL107']).split(',')[inx]
        df.drop('HL107', axis=1, inplace=True)
        df.rename(columns={'s': 'TimeStamp', 'HL101': 'PV','HL102':'T'}, inplace=True)
        cols = list(df)
        cols.insert(18,cols.pop(cols.index('PV')))
        cols.insert(18,cols.pop(cols.index('T')))
        df =df.ix[:,cols]
        df.to_csv(fullname,index=False)
            

if __name__ == '__main__':
    process = data_processed()
    #traverse all folder 
    folderlist = dp.each_file(inPath,0)
   # print(folderlist)
    for i in range(len(folderlist)):
        flist = glob.glob(folderlist[i]+'/*.csv')
        print(folderlist[i])
        startTime = time.time()
        for f in flist:
            process.hlx_processed_offline(f)
        endTime = time.time()
        msg = 'Took {Time} seconds to complete'
        print(msg.format(time= endTime-startTime))
        
        
    """
    pool = mp.Pool(3)
    results = pool.map(process.hlx_processed_offline, flist)
    """
