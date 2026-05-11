import numpy as np



def generate_buy_labels(df, threshold=0.03):
    future_return = (df['Close'].shift(-5) - df['Close']) / df['Close']

    df['BUY_SIGNAL'] = np.where(future_return > threshold, 1, 0)

    return df