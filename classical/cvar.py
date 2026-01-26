import numpy as np

def compute_cvar(returns, alpha=0.95):
   
    #CVaR computed from empirical return distribution
    portfolio_returns = returns.mean(axis=1)
    losses = -portfolio_returns

    var = np.quantile(losses, alpha)
    cvar = losses[losses >= var].mean()

    return cvar
