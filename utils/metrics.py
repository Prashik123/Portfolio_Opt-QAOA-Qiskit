import numpy as np

def efficiency(returns):
    
    #Sharpe-like efficiency
   
    return returns.mean() / returns.std()
