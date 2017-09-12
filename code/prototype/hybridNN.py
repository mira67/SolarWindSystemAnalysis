#Core Model + Neural Network Model
#Target: For time series forcasting
#Author: Qi Liu

from keras.models import Sequential
from keras.layers import Dense

import warnings
import itertools
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import scipy.stats as stats
import matplotlib.mlab as mlab
from sklearn import preprocessing

plt.style.use('fivethirtyeight')

inpath = "E:/myprojects/pv_detection/code/code/prototype/SN_y_tot_V2.0.csv"

def dataProcess(train_ratio,plot_on):
    #read in full data   
    df = pd.read_csv(inpath,sep=';',header=None)
    yr = df.iloc[:,0]
    sunspot = df.iloc[:,1]
    df_len = len(yr)
        
    #train and test partition
    train_num = round(df_len*train_ratio)
    train_data = sunspot[0:train_num+1]
    test_data = sunspot[train_num:]
    
    if plot_on == 1:
        f1 = plt.figure(1)
        plt.plot(yr,sunspot, label='Data Time Series',color='blue')
        plt.plot(yr[0:train_num+1],train_data,color = 'red')
        plt.plot(yr[train_num:],test_data,color = 'green')
        f1.show()
    
    return train_data, test_data

def arimaSelection(train_data,test_data):
    # ARIMA(p,d,q)(P,D,Q)s
    seaPed = 11 #every 11 years?
    #
    y = train_data
    
    # The term bfill means that we use the value before filling in missing values
    y = y.fillna(y.bfill()).as_matrix()
    
    # Define the p, d and q parameters to take any value between 0 and 2
    p = range(9,10)
    d = q = range(0, 2)
    
    # Generate all different combinations of p, q and q triplets
    pdq = list(itertools.product(p, d, q))
    
    # Generate all different combinations of seasonal p, q and q triplets
    # use 12 or what?
    seasonal_pdq = [(x[0], x[1], x[2], seaPed) for x in list(itertools.product(p, d, q))]
    
    
    warnings.filterwarnings("ignore") # specify to ignore warning messages
    
    allModels = []    
    
    '''
    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                mod = sm.tsa.statespace.SARIMAX(y,
                                                order=param,
                                                seasonal_order=param_seasonal,
                                                enforce_stationarity=False,
                                                enforce_invertibility=False,
                                                verbose = False)
    
                results = mod.fit()
                
                allModels.append('ARIMA{}x{}11 - AIC:{}'.format(param, param_seasonal, results.aic))
    
                print('ARIMA{}x{}11 - AIC:{}'.format(param, param_seasonal, results.aic))
            except:
                continue
    
    print('allModels: {}'.format(allModels))
    '''
    # optimal parameters fitting
    # ARIMA(9, 1, 0)x(9, 1, 1, 11)11 - AIC:1100.520795191043
    mod = sm.tsa.statespace.SARIMAX(y,
                                order=(2, 0, 0),
                                seasonal_order=(2, 0, 0, seaPed),
                                enforce_stationarity=False,
                                enforce_invertibility=False)

    arimaModel = mod.fit()
    #print(results.summary().tables[1])
    '''
    f1 = plt.figure(1)
    results.plot_diagnostics(figsize=(15, 12))
    plt.show()
    '''
    
    # Prediction test, how to use prediction
    pred = arimaModel.get_prediction(start = 1, end = 239,dynamic=False)
    pred_ci = pred.conf_int()
    
    # accuracy validation
    y_predicted = pred.predicted_mean
    y_truth = train_data.as_matrix()#test_data.as_matrix()
    
    '''
    f2 = plt.figure(2)
    plt.plot(y_truth,label='observed',color='red')
    plt.plot(y_predicted, label='One-step ahead Forecast', alpha=.7,color='blue')

    plt.legend()
    f2.show()
    '''
    
    # Compute the mean square error
    mse = ((y_predicted[4:] - y_truth[4:]) ** 2).mean()
    print('ARIMA MSE of our forecasts is {}'.format(round(mse, 2)))
    
    # arimaModel
    remainder = y_truth - y_predicted
    
    return arimaModel,y_predicted,y_truth,remainder

# Train NN, residuals from ARIMA as input
def nnBuild(train_res):
    # create model
    model = Sequential()
    model.add(Dense(4, input_dim=5, activation='sigmoid'))
    model.add(Dense(4, activation='sigmoid'))
    model.add(Dense(1, activation='linear'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['mae', 'acc'])
    # Fit model
    # Fit the model, need adjust the parameters
    train_res_X = train_res[:,0:4]
    
    #get train_res_X standarized
    train_res_X = preprocessing.scale(train_res_X)
    train_res_X = sm.add_constant(train_res_X)
    print(train_res_X)
    
    train_res_Y = train_res[:,4]
    model.fit(train_res_X, train_res_Y, epochs=1000, batch_size=10)
    scores = model.evaluate(train_res_X, train_res_Y)
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
    # calculate predictions
    predictions = model.predict(train_res_X)
    return model,predictions

def buildResTrain(remainder, n_hist):#n_hist, need test this function
    lenRes = len(remainder)
    endStart = lenRes - n_hist
    res_train = np.zeros((endStart,n_hist+1))
    count = 0
    for s in range(0,endStart):
        res_train[s,:] = remainder[s:n_hist+1+count]
        count = count + 1
    return res_train

def hybridModel(train_data,test_data):
    #Method 1: ARIMA + NN, ARIMA(p, d, q), seasonal, trend, noise
    
    
    #ARIMA model selection
    #arimaModel, arimaPred, y_truth, remainder = arimaSelection(train_data,test_data)
    # construct input for neural network from remainder
    #res_train = buildResTrain(remainder,4)
    #Neural network training for residuals
    #nnModel,nnPred = nnBuild(res_train)
    
    #arPred = arimaPred[4:]
    
    #hybridPred = arPred.reshape(-1) + nnPred.reshape(-1)
    
    
    # solely using NN
    data_train = buildResTrain(train_data.as_matrix(),4)

    nnModel, nnPred2 = nnBuild(data_train)
    
    
    #normality test
    #print(stats.normaltest(remainder))
    
    #hybridRemainder = y_truth[4:]-hybridPred
    #print(stats.normaltest(hybridRemainder))
    
    # the histogram of the data
    #n, bins, patches = plt.hist(hybridRemainder, 50, normed=1, facecolor='green', alpha=0.45)
    #n, bins, patches = plt.hist(remainder, 50, normed=1, facecolor='red', alpha=0.75)
    #plt.show()
    
    
    f2 = plt.figure(2)
    plt.plot(train_data.as_matrix()[4:],label='observed',color='red')
    #plt.plot(hybridPred, label='One-step ahead Forecast - Hybrid', alpha=.7,color='blue')
    plt.plot(nnPred2, label='One-step ahead Forecast - NN', alpha=.7,color='green')
    plt.legend()
    f2.show()
    
    
    
    # Compute the mean square error
    #mse = ((hybridPred - train_data[4:]) ** 2).mean()
    #print('HYBRID MSE of our forecasts is {}'.format(round(mse, 2)))
    
    mse = ((nnPred2.reshape(-1) - train_data[4:]) ** 2).mean()
    print('NN Only MSE of our forecasts is {}'.format(round(mse, 2)))
    
    return nnModel
    
def modelCompare(train_data,test_data):
    #Hybrid NN accuracy and NN convergence 
    nnModel = hybridModel(train_data,test_data)
    # Apply test data to models and calculate MSE for pure ARIMA and Hybrid
    
    #Pure ARIMA accuracy
    
    #Pure NN accuracy and convergence
    
    return

def main():
    train_data,test_data = dataProcess(0.75,0)
    modelCompare(train_data,test_data)
    
if __name__ == "__main__":
    main()    
    

