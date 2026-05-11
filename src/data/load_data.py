import pandas as pd
from pathlib import Path


FEATURE_COLUMNS = [
    'Open',
    'High',
    'Low',
    'Close',
    'Adj Close',
    'Volume'
]


def load_stock_csv(filepath):
    df = pd.read_csv(filepath)
    df = df.dropna()
    return df



def load_nasdaq_stock(ticker, data_dir):
    filepath = Path(data_dir) / f'{ticker}.csv'
    return load_stock_csv(filepath)



def filter_valid_companies(folder_path, min_rows=120):
    valid = []

    for file in Path(folder_path).glob('*.csv'):
        try:
            df = pd.read_csv(file)
            if len(df) >= min_rows:
                valid.append(file.stem)
        except:
            pass

    return valid