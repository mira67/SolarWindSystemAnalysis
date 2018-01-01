import numpy as np
import pandas as pd
import os
import glob

#the raw signal
#inPath = '/Users/zhaoyingying/PVData/ADIbyCen/temporal_frq_features/frq_features.csv'
#the normalized signal
#outPath = '/Users/zhaoyingying/PVData/ADIbyCen/temporal_frq_features/frq_features_scale.csv'

#aggregation features
#the raw signal
#inPath = '/Users/zhaoyingying/PVData/ADIbyCen/n_interval_fft/'
#the normalized signal
#outPath = '/Users/zhaoyingying/PVData/ADIbyCen/n_interval_fft_scale/'


#adi raw signal
inPath = '/Users/zhaoyingying/PVData/ADIbyCen/similarity_features/'
#the normalized signal
outPath = '/Users/zhaoyingying/PVData/ADIbyCen/similarity_features/similarity_features_scale/'

flist = glob.glob(inPath+'*.csv')
for f in flist:
    df= pd.read_csv(f)
    #max_min normaize
    #df.iloc[:,1:-1] = df.iloc[:,1:-1].apply(lambda x:(x-np.min(x))/(np.max(x)-np.min(x)))
    #z-score normalize
    df.iloc[:,1:-1] = df.iloc[:,1:-1].apply(lambda x:(x-np.mean(x))/np.std(x))
    fftname = os.path.basename(f)
    print(fftname)
    df.to_csv(outPath+fftname,index= False)
