import numpy as np
from sklearn.preprocessing import MinMaxScaler


scaler = MinMaxScaler()


FEATURE_COLUMNS = [
    'Open',
    'High',
    'Low',
    'Close',
    'Adj Close',
    'Volume'
]



def normalize_features(df):
    scaled = scaler.fit_transform(df[FEATURE_COLUMNS])
    return scaled



def create_sequences(data, window_size=30, future_days=1):
    X = []
    y = []

    for i in range(window_size, len(data) - future_days):
        X.append(data[i-window_size:i])
        y.append(data[i + future_days - 1][0])

    return np.array(X), np.array(y)



def create_k_day_targets(data, window_size=30, k_days=7):
    X = []
    y = []

    for i in range(window_size, len(data) - k_days):
        X.append(data[i-window_size:i])
        y.append(data[i:i+k_days, 0])

    return np.array(X), np.array(y)



def chronological_split(X, y, train_ratio=0.7, val_ratio=0.15):
    train_end = int(len(X) * train_ratio)
    val_end = int(len(X) * (train_ratio + val_ratio))

    X_train = X[:train_end]
    y_train = y[:train_end]

    X_val = X[train_end:val_end]
    y_val = y[train_end:val_end]

    X_test = X[val_end:]
    y_test = y[val_end:]

    return X_train, X_val, X_test, y_train, y_val, y_test