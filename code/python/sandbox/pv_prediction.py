#Daily PV Production Prediction Test
#Using LSTM, or combined with theoretical model [PV model and Sun Model]

#Author: qliu.hit@gmail.com

#Import Python Packages
from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

#Prepare the varlist
sym=["nbqno","d_date","the_hour","aP","aI","aV","a_r","Fs1m","Fs2m","Wv","Wd","Sd","T"]

#get data
data_path = 'E:/myprojects/pv_detection/data/prediction_data/nbq_qxz_hour.csv'

inpath = "E:/myprojects/pv_detection/data/prediction_data/qxz_s18_02_min.csv"

df=pd.read_csv(inpath)

#Compute Percentage Change
df1 = df.iloc[:,2:11]
rets = df1.pct_change()

#Compute Correlation
corr = rets.corr()

#Plot Correlation Matrix using Matplotlib
plt.figure(figsize=(10, 10))
plt.imshow(corr, cmap='RdYlGn', interpolation='none', aspect='auto')
plt.colorbar()
plt.xticks(range(len(corr)), corr.columns, rotation='vertical')
plt.yticks(range(len(corr)), corr.columns);
plt.suptitle('PV Variables Correlations Heat Map', fontsize=15, fontweight='bold')
plt.show()