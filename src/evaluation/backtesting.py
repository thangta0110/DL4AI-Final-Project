import numpy as np



def calculate_returns(prices):
    return np.diff(prices) / prices[:-1]



def sharpe_ratio(returns, risk_free_rate=0.01):
    excess_returns = returns - risk_free_rate
    return np.mean(excess_returns) / np.std(excess_returns)