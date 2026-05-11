import numpy as np



def generate_sell_labels(df, threshold=-0.03):
    future_return = (df['Close'].shift(-5) - df['Close']) / df['Close']

    df['SELL_SIGNAL'] = np.where(future_return < threshold, 1, 0)

    return df