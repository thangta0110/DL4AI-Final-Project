import streamlit as st
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# API Endpoint (Task 5.1)
API_URL = "http://localhost:8501/v1/models/vn_stock:predict"

st.set_page_config(page_title="Stock Predictor SaaS", layout="wide")
st.title("📈 Vietnam Stock Market Predictor (SaaS)")
st.write("This tool predicts the next 7 days of closing prices based on the last 30 days of market data.")

st.sidebar.header("Data Input")
st.sidebar.write("Simulate 30 days of market data (Low, High, Open, Close, Volume):")

# Generate dummy historical data for demonstration
if st.sidebar.button("Generate Sample Market Data"):
    sample_data = np.random.rand(30, 5).tolist()
    st.session_state['market_data'] = sample_data
    st.sidebar.success("Sample data generated!")

if 'market_data' in st.session_state:
    st.write("### Last 30 Days (Normalized Inputs)")
    df_input = pd.DataFrame(st.session_state['market_data'], columns=['Low', 'High', 'Open', 'Close', 'Volume'])
    st.line_chart(df_input['Close'])
    
    if st.button("Predict Next 7 Days"):
        with st.spinner("Calling Prediction API..."):
            payload = {"instances": [st.session_state['market_data']]}
            try:
                response = requests.post(API_URL, json=payload)
                if response.status_code == 200:
                    predictions = response.json()['predictions'][0]
                    
                    st.success("Prediction Successful!")
                    st.write("### 7-Day Forecast")
                    
                    # Plot historical vs predicted
                    fig, ax = plt.subplots(figsize=(10, 4))
                    ax.plot(range(30), df_input['Close'], label="Historical Close (30 Days)", color="blue")
                    ax.plot(range(30, 37), predictions, marker='o', linestyle='--', color="red", label="Predicted Close (7 Days)")
                    ax.legend()
                    st.pyplot(fig)
                else:
                    st.error(f"API Error: {response.text}")
            except Exception as e:
                st.error(f"Connection failed. Is the API running on port 8501? Error: {e}")