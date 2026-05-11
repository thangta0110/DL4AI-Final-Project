from src.models.lstm_model import build_lstm_model



def test_model_creation():
    model = build_lstm_model((30,6))
    assert model is not None