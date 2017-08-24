from sklearn.neural_network import MLPClassifier
import numpy as np
import pandas as pd
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report,confusion_matrix

inpath = 'E:/myprojects/pv_detection/code/code/python/qxz_s18_02_min_labeled_subset.csv'
#inpath = '/home/mirabot/Documents/PyTorch/qxz_s18_02_min_labeled.csv'
df = pd.read_csv(inpath)
pvdata_obs = scale(df.iloc[0:15000,3:10].as_matrix())
pvdata_reward = df.iloc[0:15000,10].as_matrix()
pvdata_num = pvdata_obs.shape[0]
print(pvdata_num)
pvdata_counter = 0

clf = MLPClassifier(activation='relu', alpha=1e-05, batch_size=1,
       beta_1=0.9, beta_2=0.999, early_stopping=False,
       epsilon=1e-08, hidden_layer_sizes=(8, 12), learning_rate='constant',
       learning_rate_init=0.001, max_iter=1000, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
       solver='lbfgs', tol=0.0001, validation_fraction=0.1, verbose=False,
       warm_start=False)

clf = clf.fit(pvdata_obs, pvdata_reward)

x_test = scale(df.iloc[15000:18000,3:10].as_matrix())
y_test = df.iloc[15000:18000,10].as_matrix()

predictions = clf.predict(x_test)

print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

plt.plot(predictions*5)
plt.hold('on')
plt.plot(df.iloc[15000:18000,3].as_matrix())
plt.show()