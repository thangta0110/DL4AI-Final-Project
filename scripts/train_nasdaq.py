from src.data.load_data import load_nasdaq_stock
from src.data.preprocess import (
    normalize_features,
    create_sequences,
    chronological_split,
)

from src.models.lstm_model import build_lstm_model
from src.models.train import train_model


DATA_DIR = 'data/nasdaq/csv'


df = load_nasdaq_stock('AAPL', DATA_DIR)

scaled_data = normalize_features(df)

X, y = create_sequences(scaled_data)

X_train, X_val, X_test, y_train, y_val, y_test = chronological_split(X, y)

model = build_lstm_model((X_train.shape[1], X_train.shape[2]))

history = train_model(
    model,
    X_train,
    y_train,
    X_val,
    y_val,
)

model.save('saved_models/nasdaq/lstm_aapl.keras')