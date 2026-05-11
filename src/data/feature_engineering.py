import ta



def add_rsi(df):
    indicator = ta.momentum.RSIIndicator(df['Close'])
    df['RSI'] = indicator.rsi()
    return df



def add_macd(df):
    macd = ta.trend.MACD(df['Close'])

    df['MACD'] = macd.macd()
    df['MACD_SIGNAL'] = macd.macd_signal()

    return df



def add_sma(df, window=20):
    df[f'SMA_{window}'] = df['Close'].rolling(window=window).mean()
    return df