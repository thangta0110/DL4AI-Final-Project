# Deep Learning for AI: Stock Market Prediction & Portfolio Optimization

## Project Overview

This project implements deep learning models for stock price prediction and portfolio optimization, focusing on NASDAQ and Vietnam stock markets. The system includes price forecasting, trading signal identification, risk management, and deployment infrastructure.

## Project Structure

```
DL4AI-240205-project/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── setup.py                     # Package setup
│
├── data/
│   ├── nasdaq/csv/             # 250+ NASDAQ stock CSV files
│   └── vietnam/                # Vietnam market data
│
├── notebooks/
│   ├── Final_project_DL4AI.ipynb           # Main notebook
│
├── src/
│   ├── config/
│   │   ├── config.py           # Configuration settings
│   │   └── paths.py            # Path definitions
│   │
│   ├── data/
│   │   ├── load_data.py        # Data loading utilities
│   │   ├── preprocess.py       # Data preprocessing
│   │   ├── feature_engineering.py  # Feature engineering
│   │   └── time_series_split.py    # Time series splitting
│   │
│   ├── models/
│   │   ├── lstm_model.py       # LSTM model architecture
│   │   ├── gru_model.py        # GRU model architecture
│   │   ├── transformer_model.py# Transformer model
│   │   └── train.py            # Training utilities
│   │
│   ├── deployment/
│   │   ├── api/
│   │   │   ├── flask_server.py # Flask REST API
│   │   │   └── model_server.py # Model serving
│   │   ├── streamlit_app/
│   │   │   └── app.py          # Streamlit SaaS interface
│   │   ├── airflow/
│   │   │   └── dags/
│   │   │       └── stock_prediction_dag.py  # Airflow workflow
│   │   └── docker/
│   │       ├── Dockerfile      # Docker configuration
│   │       └── docker-compose.yml
│   │
│   ├── evaluation/
│   │   ├── metrics.py          # Evaluation metrics
│   │   ├── backtesting.py      # Backtesting utilities
│   │   └── visualize.py        # Visualization tools
│   │
│   ├── signals/
│   │   ├── indicators.py       # Technical indicators
│   │   ├── buy_signal.py       # Buy signal identification
│   │   └── sell_signal.py      # Sell signal identification
│   │
│   ├── portfolio/
│   │   ├── portfolio_optimizer.py  # Portfolio optimization
│   │   ├── stock_selection.py      # Stock selection
│   │   └── risk_management.py      # Risk management
│   │
│   └── utils/
│       ├── helpers.py          # Helper functions
│       ├── logger.py           # Logging configuration
│       └── seed.py             # Random seed management
│
├── scripts/
│   ├── train_nasdaq.py         # NASDAQ model training
│   ├── train_vietnam.py        # Vietnam model training
│   ├── train_signals.py        # Signal model training
│   ├── train_portfolio.py      # Portfolio model training
│   └── inference.py            # Inference script
│
├── saved_models/
│   ├── nasdaq/                 # Saved NASDAQ models
│   ├── vietnam/                # Saved Vietnam models
│   ├── signals/                # Saved signal models
│   └── portfolio/              # Saved portfolio models
│
├── experiments/
│   ├── logs/                   # Training logs
│   ├── results/                # Experiment results
│   └── tensorboard/            # TensorBoard logs
│
├── reports/
│   ├── report_draft.md         # Project report
│   ├── figures/                # Report figures
│   └── tables/                 # Report tables
│
└── tests/
    ├── test_models.py          # Model testing
    ├── test_data.py            # Data testing
    └── test_api.py             # API testing
```

## Tasks Implemented

### Task 1: NASDAQ Stock Price Prediction (15%)
- **Task 1.1 (5%)**: Multi-feature CNN model using Low, High, Open, Close, Adjusted Close, and Volume
- **Task 1.2 (5%)**: k-day forecast model (predict price k days ahead)
- **Task 1.3 (5%)**: Multi-day consecutive forecast model (predict k consecutive days)

### Task 2: Vietnam Stock Price Prediction (15%)
- **Task 2.1 (5%)**: Multi-feature model for Vietnam stocks
- **Task 2.2 (5%)**: k-day forecast for Vietnam market
- **Task 2.3 (5%)**: Multi-day consecutive forecast

### Task 3: Trading Signal Identification (20%)
- **Task 3.1 (10%)**: Buy signal identification using CNN with class weighting
- **Task 3.2 (10%)**: Sell signal identification with RSI and MACD indicators

### Task 4: Portfolio Optimization (30%)
- **Task 4.1 (10%)**: Profitable stock selection (liquidity filter + trend following)
- **Task 4.2 (10%)**: Risk management (volatility + liquidity risk scoring)
- **Task 4.3 (10%)**: Portfolio composition (Prudent vs Risk-Taking strategies)

### Task 5: Deployment & Automation (30% - Extra Credit)
- **Task 5.1 (5%)**: REST API deployment with Flask
- **Task 5.2 (10%)**: SaaS web interface with Streamlit
- **Task 5.3 (15%)**: Automated workflow orchestration with Airflow

## Installation

### Prerequisites
- Python 3.9+
- pip or conda

### Setup

1. **Clone/Extract the project**
   ```bash
   cd DL4AI-240205-project
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare data**
   Ensure data files are in:
   - `data/nasdaq/csv/` - NASDAQ stock data
   - `data/vietnam/` - Vietnam stock data

## Usage

### Running Individual Notebooks
```bash
jupyter notebook notebooks/Final_project_DL4AI.ipynb
```

### Training Models
```bash
# Train NASDAQ model
python scripts/train_nasdaq.py

# Train Vietnam model
python scripts/train_vietnam.py

# Train signal models
python scripts/train_signals.py

# Train portfolio model
python scripts/train_portfolio.py
```

### REST API Server
```bash
# Start Flask server
python src/deployment/api/flask_server.py

# API will be available at http://localhost:5000
# Example: curl http://localhost:5000/predict?ticker=AAPL&days=7
```

### Streamlit SaaS Interface
```bash
# Start Streamlit app
streamlit run src/deployment/streamlit_app/app.py

# Open browser to http://localhost:8501
```

### Airflow Workflow
```bash
# Initialize Airflow database
airflow db init

# Start Airflow scheduler
airflow scheduler

# In another terminal, start webserver
airflow webserver --port 8080

# Access at http://localhost:8080
```

## Key Technologies

- **Deep Learning**: TensorFlow, Keras, PyTorch
- **Time-Series**: Scikit-learn, Statsmodels
- **Visualization**: Matplotlib, Plotly
- **Deployment**: Flask, Streamlit, Docker
- **Orchestration**: Apache Airflow
- **Data Processing**: Pandas, NumPy

## Model Architectures

### CNN for Time-Series Prediction
- Conv1D layers for temporal pattern extraction
- MaxPooling1D for dimensionality reduction
- Dense layers for feature transformation
- Output: Price predictions or probability scores

### Key Features
- Per-window MinMax normalization
- Time-series train/validation/test split (no shuffling)
- Early stopping to prevent overfitting
- Custom class weights for imbalanced signal classification

## Performance Metrics

- **Regression**: Mean Squared Error (MSE), Mean Absolute Error (MAE)
- **Classification**: Precision, Recall, F1-Score, ROC-AUC
- **Backtesting**: Sharpe Ratio, Max Drawdown, Total Return

## API Endpoints

### REST API
- `GET /predict` - Predict stock price
- `POST /train` - Train model
- `GET /signals` - Get trading signals
- `GET /portfolio` - Get portfolio recommendations
- `GET /health` - Health check

## Deployment

### Docker
```bash
# Build image
docker build -t dl4ai-stock-prediction .

# Run container
docker run -p 5000:5000 -p 8501:8501 dl4ai-stock-prediction
```

### Cloud Deployment
Supports deployment to:
- AWS (SageMaker, Lambda)
- Google Cloud (Vertex AI, Cloud Functions)
- Azure (Azure ML, Functions)

## Data Sources

- **NASDAQ**: data/nasdaq/csv/ (250+ stocks)
- **Vietnam**: data/vietnam/data-vn-20230228/ (local market data)

## Project Report

See `reports/report_draft.md` for detailed documentation including:
- Methodology explanations
- Model justifications
- Results analysis
- Future improvements

## Contact & Support

For issues or questions, refer to the project documentation or create an issue in the repository.

## License

See LICENSE file for details.
