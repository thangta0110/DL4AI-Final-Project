from sklearn.model_selection import TimeSeriesSplit



def get_time_series_split(n_splits=5):
    return TimeSeriesSplit(n_splits=n_splits)