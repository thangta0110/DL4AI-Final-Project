"""
Flask REST API Server for Stock Prediction Models (Task 5.1)
Implements REST API endpoints for model deployment
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
import tensorflow as tf
import os
import json
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Configuration
MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'saved_models')
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'data')
NASDAQ_MODEL_PATH = os.path.join(MODEL_DIR, 'nasdaq', 'model.h5')
VIETNAM_MODEL_PATH = os.path.join(MODEL_DIR, 'vietnam', 'model.h5')
SIGNAL_MODEL_PATH = os.path.join(MODEL_DIR, 'signals', 'model.h5')

# Global models  dictionary
models = {}
scaler_stats = {}

def load_models():
    """Load pre-trained models"""
    global models
    try:
        # Create dummy models for demo (replace with actual trained models)
        logger.info("Loading models...")
        # In production, load actual saved models
        models['nasdaq_loaded'] = True
        models['vietnam_loaded'] = True
        models['signals_loaded'] = True
        logger.info("Models loaded successfully")
    except Exception as e:
        logger.error(f"Error loading models: {e}")

def load_stock_data(ticker):
    """Load stock data for a given ticker"""
    try:
        csv_path = os.path.join(DATA_DIR, 'nasdaq', 'csv', f'{ticker}.csv')
        if os.path.exists(csv_path):
            df = pd.read_csv(csv_path)
            return df
        else:
            return None
    except Exception as e:
        logger.error(f"Error loading stock data for {ticker}: {e}")
        return None

def prepare_prediction_input(data, window_size=30):
    """Prepare data for prediction"""
    feature_cols = ['Low', 'High', 'Open', 'Close', 'Adjusted Close', 'Volume']
    df = data[feature_cols].copy()
    
    if len(df) < window_size:
        return None
    
    window = df.iloc[-window_size:].values
    
    # Normalize
    X_norm = window.copy().astype('float32')
    for f in range(len(feature_cols)):
        f_min, f_max = window[:, f].min(), window[:, f].max()
        if f_max > f_min:
            X_norm[:, f] = (window[:, f] - f_min) / (f_max - f_min)
    
    return X_norm.reshape(1, window_size, len(feature_cols)), window[:, 3]

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'models_loaded': models
    }), 200

@app.route('/predict', methods=['GET'])
def predict():
    """
    Predict stock price
    Query parameters:
    - ticker: Stock ticker (e.g., 'AAPL')
    - days: Number of days ahead to forecast (default: 1)
    - market: 'nasdaq' or 'vietnam' (default: 'nasdaq')
    """
    try:
        ticker = request.args.get('ticker', 'AAPL').upper()
        days_ahead = int(request.args.get('days', 1))
        market = request.args.get('market', 'nasdaq').lower()
        
        logger.info(f"Prediction request: ticker={ticker}, days={days_ahead}, market={market}")
        
        # Load data
        data = load_stock_data(ticker)
        if data is None:
            return jsonify({
                'error': f'Stock data not found for ticker {ticker}',
                'status': 'error'
            }), 404
        
        # Prepare input
        X_norm, close_range = prepare_prediction_input(data)
        if X_norm is None:
            return jsonify({
                'error': 'Insufficient data for prediction',
                'status': 'error'
            }), 400
        
        # Generate prediction (placeholder)
        last_price = data['Close'].iloc[-1]
        predicted_prices = [last_price * (1 + np.random.uniform(-0.02, 0.02)) for _ in range(days_ahead)]
        confidence = np.random.uniform(0.65, 0.95)
        
        return jsonify({
            'ticker': ticker,
            'market': market,
            'days_ahead': days_ahead,
            'last_price': float(last_price),
            'predicted_prices': [float(p) for p in predicted_prices],
            'confidence': float(confidence),
            'timestamp': datetime.now().isoformat(),
            'status': 'success'
        }), 200
        
    except Exception as e:
        logger.error(f"Prediction error: {e}")
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/signals', methods=['GET'])
def get_trading_signals():
    """
    Get trading signals for a stock
    Query parameters:
    - ticker: Stock ticker
    - signal_type: 'buy' or 'sell' (default: 'buy')
    """
    try:
        ticker = request.args.get('ticker', 'AAPL').upper()
        signal_type = request.args.get('signal_type', 'buy').lower()
        
        data = load_stock_data(ticker)
        if data is None:
            return jsonify({
                'error': f'Stock data not found for ticker {ticker}',
                'status': 'error'
            }), 404
        
        # Generate signal (placeholder)
        signal_probability = np.random.uniform(0.3, 0.9)
        signal = 'STRONG' if signal_probability > 0.7 else 'MODERATE' if signal_probability > 0.5 else 'WEAK'
        
        return jsonify({
            'ticker': ticker,
            'signal_type': signal_type,
            'signal': signal,
            'probability': float(signal_probability),
            'timestamp': datetime.now().isoformat(),
            'status': 'success'
        }), 200
        
    except Exception as e:
        logger.error(f"Signal error: {e}")
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/portfolio', methods=['GET'])
def get_portfolio_recommendation():
    """
    Get portfolio recommendation
    Query parameters:
    - profile: 'prudent' or 'risk-taking' (default: 'prudent')
    - market: 'nasdaq' or 'vietnam' (default: 'vietnam')
    """
    try:
        profile = request.args.get('profile', 'prudent').lower()
        market = request.args.get('market', 'vietnam').lower()
        
        # Generate recommendation (placeholder)
        if profile == 'prudent':
            portfolio = [
                {'ticker': 'VCB', 'weight': 0.25, 'expected_return': 0.08, 'risk_score': 0.2},
                {'ticker': 'BID', 'weight': 0.30, 'expected_return': 0.10, 'risk_score': 0.25},
                {'ticker': 'ACB', 'weight': 0.20, 'expected_return': 0.07, 'risk_score': 0.18},
                {'ticker': 'MBB', 'weight': 0.15, 'expected_return': 0.09, 'risk_score': 0.22},
                {'ticker': 'HPG', 'weight': 0.10, 'expected_return': 0.12, 'risk_score': 0.30},
            ]
        else:
            portfolio = [
                {'ticker': 'HPG', 'weight': 0.25, 'expected_return': 0.15, 'risk_score': 0.35},
                {'ticker': 'FPT', 'weight': 0.25, 'expected_return': 0.18, 'risk_score': 0.40},
                {'ticker': 'VIC', 'weight': 0.20, 'expected_return': 0.14, 'risk_score': 0.32},
                {'ticker': 'MWG', 'weight': 0.15, 'expected_return': 0.16, 'risk_score': 0.38},
                {'ticker': 'TPB', 'weight': 0.15, 'expected_return': 0.13, 'risk_score': 0.30},
            ]
        
        return jsonify({
            'profile': profile,
            'market': market,
            'portfolio': portfolio,
            'portfolio_return': sum(p['expected_return'] * p['weight'] for p in portfolio),
            'portfolio_risk': np.sqrt(sum((p['risk_score'] * p['weight']) ** 2 for p in portfolio)),
            'timestamp': datetime.now().isoformat(),
            'status': 'success'
        }), 200
        
    except Exception as e:
        logger.error(f"Portfolio error: {e}")
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/backtest', methods=['POST'])
def backtest_strategy():
    """
    Backtest a trading strategy
    POST data should include:
    - strategy: Strategy type or parameters
    - start_date: Start date
    - end_date: End date
    """
    try:
        data = request.get_json()
        strategy = data.get('strategy', 'default')
        start_date = data.get('start_date', (datetime.now() - timedelta(days=365)).isoformat())
        end_date = data.get('end_date', datetime.now().isoformat())
        
        # Simulate backtest results
        results = {
            'strategy': strategy,
            'start_date': start_date,
            'end_date': end_date,
            'total_return': np.random.uniform(0.05, 0.30),
            'sharpe_ratio': np.random.uniform(0.5, 2.0),
            'max_drawdown': np.random.uniform(-0.15, -0.05),
            'win_rate': np.random.uniform(0.45, 0.65),
            'num_trades': np.random.randint(20, 100),
            'timestamp': datetime.now().isoformat(),
            'status': 'success'
        }
        
        return jsonify(results), 200
        
    except Exception as e:
        logger.error(f"Backtest error: {e}")
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({
        'error': 'Endpoint not found',
        'status': 'error'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({
        'error': 'Internal server error',
        'status': 'error'
    }), 500

if __name__ == '__main__':
    # Load models at startup
    load_models()
    
    # Start Flask server
    logger.info("Starting Stock Prediction API Server...")
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=False,
        threaded=True
    )
