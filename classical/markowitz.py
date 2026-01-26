import numpy as np

def markowitz_score(mu, sigma, lam):
    
    #Classical Markowitz scoring (baseline)
    
    return mu - lam * np.diag(sigma)
