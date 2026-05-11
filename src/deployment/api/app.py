from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import tensorflow as tf
import uvicorn

# Initialize API
app = FastAPI(title="Vietnam Stock Prediction API", version="1.0")

# Load the saved model from Task 2.3
MODEL_PATH = "../models/vn_stock_7day_model.h5"
try:
    model = tf.keras.models.load_model(MODEL_PATH)
except Exception as e:
    print(f"Warning: Model not found at {MODEL_PATH}. Ensure the notebook has been run and models exported.")
    model = None

# Define the expected input schema
class StockDataInput(BaseModel):
    # Expecting a list of 30 days, each containing 5 features: [Low, High, Open, Close, Volume]
    instances: list

@app.get("/")
def health_check():
    return {"status": "Active", "message": "Stock Prediction API is running."}

@app.post("/v1/models/vn_stock:predict")
def predict_stock(data: StockDataInput):
    if model is None:
        raise HTTPException(status_code=500, detail="Model not loaded on server.")
    
    try:
        # Convert input to numpy array
        input_data = np.array(data.instances, dtype=np.float32)
        
        # Validate shape (Batch Size, Window Size, Features) -> (1, 30, 5)
        if len(input_data.shape) == 2:
            input_data = np.expand_dict(input_data, axis=0) # Add batch dimension
            
        if input_data.shape[1] != 30 or input_data.shape[2] != 5:
            raise ValueError(f"Expected shape (None, 30, 5), got {input_data.shape}")
        
        # Predict
        predictions = model.predict(input_data)
        
        return {
            "model": "vn_stock_7day_model",
            "predictions": predictions.tolist()
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    # Run server locally: python api/main.py
    uvicorn.run(app, host="0.0.0.0", port=8501)
