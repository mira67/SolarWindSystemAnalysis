"""PV String Level Fault Detection
   Author: Qi Liu
   Email: qliu.hit@gmail.com
"""
import pandas as pd
import numpy as np
from sklearn.mixture import GMM
from matplotlib import pyplot as plt
import time

# fit models with N components, String Number, worst case, need proof of minimal number of strings for this method
def fdGMM(x,nStr):

    N = np.arange(1, nStr)
    
    models = [None for i in range(len(N))]
    
    for i in range(len(N)):
        models[i] = GMM(N[i],covariance_type='full').fit(x)
    
    # compute the BIC
    BIC = [m.bic(x) for m in models]
    
    # get minimal BIC index as optimal number of clusters
    fK = BIC.index(min(BIC)) + 1
    
    fmodel = GMM(fK,covariance_type='full').fit(x)
    clusters = fmodel.predict(x)
    return clusters,fmodel.means_,fK
    
#test data
#tStrs = np.array([[7.49],[7.535],[7.43],[7.43],[7.5],[7.51],[7.31],[7.49],[7.5],[7.4],[7.42],[7.58],[7.56],[7.49],[6.425],[6.87],[6.8],[3.3]])

def timerfunc(func):
    """
    A timer decorator
    """
    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "The runtime for {func} took {time} seconds to complete"
        print(msg.format(func=func.__name__,
                         time=runtime))
        return value
    return function_timer