# using model with physical meaning
# estimate expected PV output
# using linear model

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import scipy.stats as stats
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats
import math

inpath = "E:/myprojects/pv_detection/data/prediction_data/qxz_s18_02_min.csv"

df = pd.read_csv(inpath)

df_data = df.iloc[:,1:12]

df_fea = df.iloc[:,2:12]

smLen = 1

df_data = pd.rolling_mean(df_data, smLen)

df_sm = df_data.as_matrix()

x_train = df_sm[smLen:7000,2:10]
y_train = df_sm[smLen:7000,1]
x_test = df_sm[smLen:18000,2:10]
y_test = df_sm[smLen:18000,1]

#x_test = sm.add_constant(x_test)

X = x_train
y = y_train

#x_train = sm.add_constant(X)
est = sm.OLS(y, x_train)
est2 = est.fit()
print(est2.summary())

#plt.plot(df_sm.iloc[:,0:2])
#plt.show()

lm = LinearRegression()
lm.fit(x_train,y_train)

#linear model coefficients
#pd.DataFrame(zip(df_fea.columns, lm.coef_),columns=['Features','EstimatedCoefs'])

pred_train = lm.predict(x_train)
pred_test = lm.predict(x_test)

# The coefficients
print('Coefficients: \n', lm.coef_)
# The mean squared error
print("Root mean squared error: %.4f"
      % math.sqrt(np.mean((y_test - pred_test) ** 2)))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.4f' % lm.score(x_test, y_test))

# Plot outputs
f1 = plt.figure(1)
plt.plot(y_test, label='Actual Power from String 1')
plt.plot(pred_test, label='Predicted Power from String 1')
plt.plot(df_sm[smLen:18000,0],label='Actual Power from String 2')

plt.xlabel('Time (min)')
plt.ylabel('Power')
plt.title('Linear Regression')
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.07),
          fancybox=True, shadow=True, ncol=5)

f1.show()

# Plot error distribution
f2 = plt.figure(2)
err = abs(y_test-pred_test)

histc, bin_edges = np.histogram(err,bins=50)

weights = np.ones_like(err)#/float(len(err))
print(bin_edges)
err_hist = histc/float(len(err))
plt.bar(bin_edges[:-1],err_hist,width=0.1)
plt.xlabel('Absolute Error')
plt.ylabel('Probability')
f2.show()