# Clean Event Analysis
# Author: Qi Liu
# Email: qi.liu@colorado.edu

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import medfilt

hlxInfo = '/Users/mira67/Documents/concord/concord_work/hlxinfo.csv'
qxjl = '/Users/mira67/Documents/concord/concord_work/qxjl.csv'
feaPath = '/Users/mira67/Documents/concord/concord_work/soiling_slope/'
figPath = '/Users/mira67/Documents/concord/concord_work/analysis/slopes/'


def removeOutliers(a, outlierConstant):
    upper_quartile = np.percentile(a, 75)
    lower_quartile = np.percentile(a, 25)
    IQR = (upper_quartile - lower_quartile) * outlierConstant
    quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
    resultList = []
    for y in a.tolist():
        if y >= quartileSet[0] and y <= quartileSet[1]:
            resultList.append(y)
        else:
            resultList.append(np.median(a))
    return resultList, upper_quartile


# Grab features from a nbq
hlx_info = pd.read_csv(hlxInfo)
nbqList = ['S01-NBA', 'S01-NBB', 'S02-NBA']

# visualize the clean record for this nbq
nbq_qx = pd.read_csv(qxjl)
nbq_qx = nbq_qx[nbq_qx['nbqno'] == nbqList[0]]
print(nbq_qx.shape)

nbq_qx['qxdate'] = pd.to_datetime(nbq_qx['qxdate'], format='%Y-%m-%d %H:%M:%S')
nbq_qx.set_index(['qxdate'], inplace=True)

#
'''
plt.plot(nbq_qx.index, nbq_qx['cpr1'], 'o-')
plt.plot(nbq_qx.index, nbq_qx['cpr2'], 'x-')
plt.plot(nbq_qx.index, nbq_qx['pr1'], '.-')
plt.ylabel('CPR in Database')
plt.xlabel('Clean Date')
plt.show()
'''


# Collect all features in this nbq
hlxList = hlx_info[hlx_info['nbqno'] == nbqList[1]]
hlxs = hlxList['combinerbox']
# plot all slopes trends in each hlx
for idx, cb in enumerate(hlxs):
    df = pd.read_csv(feaPath + cb + '.csv')

    df['data_date'] = pd.to_datetime(df['data_date'],
                                     format='%Y-%m-%d %H:%M:%S')
    df.set_index(['data_date'], inplace=True)

    if idx == 0:
        slope = df.iloc[:, 1:17]
    else:
        # for other cb with strings < 16, need to remove empty strings
        # fix in feature extraction
        slope = np.concatenate((slope, df.iloc[:, 1:17]), axis=1)

med_slope = np.median(slope, axis=1)
# print(med_slope.shape)
plt.plot(df.index, med_slope, label='Median of Slopes in An Inverter')
med_slope, upper = removeOutliers(med_slope, 1.5)
print('upper', upper)
plt.plot(df.index, med_slope, label='Outliers/Missing Data Fixed')
# med filtering
y1 = medfilt(med_slope, 7)
plt.plot(df.index, y1, label='7-day Med Filtered')
# overlap clean marks
n_clean = [0.008] * nbq_qx.index.shape[0]
plt.plot(nbq_qx.index, n_clean, 'x', label='Clean Event')
plt.legend()
plt.show()
plt.savefig(figPath + cb + '.png', dpi=300)
plt.close()


'''
plt.plot(df.index, slope)
# overlap clean marks
n_clean = [0.008] * nbq_qx.index.shape[0]
plt.plot(nbq_qx.index, n_clean, 'x')
# plt.show()
plt.savefig(figPath + cb + '.png', dpi=300)
plt.close()
'''
# Trial 3, use the total current vs solar ratio from inverter level
# check the trend
