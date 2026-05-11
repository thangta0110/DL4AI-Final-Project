from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GRU, Dense, Dropout



def build_gru_model(input_shape, output_size=1):
    model = Sequential([
        GRU(64, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),

        GRU(64),
        Dropout(0.2),

        Dense(32, activation='relu'),
        Dense(output_size)
    ])

    model.compile(
        optimizer='adam',
        loss='mse',
        metrics=['mae']
    )

    return model