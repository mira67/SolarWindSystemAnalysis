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
                                order=(9, 1, 0),
                                seasonal_order=(9, 1, 1, seaPed),
                                enforce_stationarity=False,
                                enforce_invertibility=False)

    results = mod.fit()
    print(results.summary().tables[1])
    #f1 = plt.figure(1)
    #results.plot_diagnostics(figsize=(15, 12))
    #f1.show()
    
    
    # Prediction test, how to use prediction
    pred = results.get_prediction(start = 238, end = 317,dynamic=False)
    pred_ci = pred.conf_int()
    
    f2 = plt.figure(2)
    plt.plot(test_data,label='observed',color='red')
    plt.plot(pred.predicted_mean, label='One-step ahead Forecast', alpha=.7,color='blue')

    plt.legend()
    f2.show()
    
    # accuracy validation
    y_forecasted = pred.predicted_mean
    y_truth = test_data
    
    # Compute the mean square error
    mse = ((y_forecasted - y_truth) ** 2).mean()
    print('The Mean Squared Error of our forecasts is {}'.format(round(mse, 2)))
    
    # arimaModel
    arimaModel = 0
    return arimaModel

# Train NN, residuals from ARIMA as input
def nnBuild(train_res,test_res):
    # create model
    model = Sequential()
    model.add(Dense(4, input_dim=4, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['mae', 'acc'])
    # Fit model
    # Fit the model, need adjust the parameters
    train_res_X = train_res[:,0:4]
    train_res_Y = train_res[:,4]
    model.fit(train_res_X, train_res_Y, epochs=150, batch_size=10)
    return model

def buildResTrain(remainder, n_hist):#n_hist, need test this function
    lenRes = len(remainder)
    endStart = lenRes - n_hist
    res_train = np.zeros(endStart,n_hist+1)
    
    for s in range(0,endStart):
        res_train[s,:] = remainder[s:n_hist]
    return res_train

def hybridModel(train_data,test_data):
    #Method 1: ARIMA + NN, ARIMA(p, d, q), seasonal, trend, noise
    #ARIMA model selection
    arimaModel, remainder = arimaSelection(train_data,test_data)
    # construct input for neural network from remainder
    res_train = buildResTrain(remainder)
    #Neural network training for residuals
    nnModel = nnBuild(res_train)
    
    return arimaModel,nnModel
    
def modelCompare(train_data,test_data):
    #Hybrid NN accuracy and NN convergence 
    arimaModel,nnModel = hybridModel(train_data,test_data)
    # Apply test data to models and calculate MSE for pure ARIMA and Hybrid
    
    #Pure ARIMA accuracy
    
    #Pure NN accuracy and convergence
    
    pass
    return

def main():
    train_data,test_data = dataProcess(0.75,0)
    modelCompare(train_data,test_data)
    
if __name__ == "__main__":
    main()    
    

