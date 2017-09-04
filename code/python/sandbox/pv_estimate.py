#Estimate PV Output using solar irradiance and other parameters
#using SVR model
#Author: Qi Liu

print(__doc__)

import numpy as np
import pandas as pd
from sklearn.preprocessing import normalize,scale
from sklearn.svm import SVR
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.model_selection import GridSearchCV

#data path
inpath = "E:/myprojects/pv_detection/data/prediction_data/qxz_s18_02_min.csv"

#training and test data
df = pd.read_csv(inpath)

df_data = df.iloc[:,1:12]

df_fea = df.iloc[:,2:12]

smLen = 60

df_data = pd.rolling_mean(df_data, smLen)

df_sm = df_data.as_matrix()

x_train = df_sm[smLen:7000,2:10]
y_train = df_sm[smLen:7000,1]
x_test = df_sm[smLen:20000,2:10]
y_test = df_sm[smLen:20000,1]

#set up model
'''
svr_rbf = GridSearchCV(SVR(kernel='rbf', gamma=0.1), cv=5,
                   param_grid={"C": [1e0, 1e1, 1e2, 1e3],
                               "gamma": np.logspace(-2, 2, 5)})
'''


svr_rbf = SVR(kernel='rbf', C=1e1, gamma=0.1)

svr = svr_rbf.fit(x_train, y_train)
y_pred = svr.predict(x_test)

'''
train_sizes, train_scores_svr, test_scores_svr = \
    learning_curve(svr, train_x, train_y, train_sizes=np.linspace(0.1, 1, 10),
                   scoring="neg_mean_squared_error", cv=10)
plt.plot(train_sizes, -test_scores_svr.mean(1), 'o-', color="r",
         label="SVR")

plt.show()

'''

# The mean squared error
print("Mean squared error: %.4f"
      % np.mean((y_pred - y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.4f' % svr.score(x_test, y_test))

lw = 2
plt.plot(y_test, color='darkorange', label='Test_Y',fontsize=15)
plt.hold('on')
plt.plot(y_pred, color='navy', lw=lw, label='RBF model Y',fontsize=15)
plt.xlabel('Time (min)')
plt.ylabel('Power')
plt.title('Support Vector Regression')
plt.legend()
plt.show()

'''
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=2)
y_lin = svr_lin.fit(X, y).predict(X)
y_poly = svr_poly.fit(X, y).predict(X)
plt.plot(X, y_lin, color='c', lw=lw, label='Linear model')
plt.plot(X, y_poly, color='cornflowerblue', lw=lw, label='Polynomial model')
'''