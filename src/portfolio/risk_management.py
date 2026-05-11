import numpy as np



def calculate_volatility(returns):
    return np.std(returns)



def calculate_drawdown(prices):
    cumulative_max = np.maximum.accumulate(prices)
    drawdown = (prices - cumulative_max) / cumulative_max
    return drawdown.min()