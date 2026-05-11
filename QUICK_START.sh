#!/bin/bash

# Quick Start Guide for DL4AI Stock Prediction Project
# This script helps you get started with the project

echo "🚀 DL4AI Stock Prediction - Quick Start Guide"
echo "=============================================="
echo ""

# Check Python version
echo "✓ Checking Python version..."
python --version
echo ""

# Install requirements
echo "✓ Installing dependencies..."
echo "  Run: pip install -r requirements.txt"
echo ""

# Show how to run each component
echo "📊 COMPONENT SETUP INSTRUCTIONS"
echo "================================"
echo ""

echo "1️⃣  JUPYTER NOTEBOOKS"
echo "   Run your analysis notebooks:"
echo "   $ jupyter notebook notebooks/Final_project_DL4AI.ipynb"
echo ""

echo "2️⃣  REST API SERVER (Task 5.1)"
echo "   Start the Flask API:"
echo "   $ python src/deployment/api/flask_server.py"
echo ""
echo "   Test the API:"
echo "   $ curl http://localhost:5000/health"
echo "   $ curl 'http://localhost:5000/predict?ticker=AAPL&days=7'"
echo ""

echo "3️⃣  STREAMLIT DASHBOARD (Task 5.2)"
echo "   Launch the web interface:"
echo "   $ streamlit run src/deployment/streamlit_app/app.py"
echo ""
echo "   Browser: http://localhost:8501"
echo ""

echo "4️⃣  AIRFLOW WORKFLOW (Task 5.3)"
echo "   Setup Airflow automation:"
echo "   $ airflow db init"
echo "   $ airflow scheduler &"
echo "   $ airflow webserver --port 8080"
echo ""
echo "   Browser: http://localhost:8080"
echo ""

echo "📁 PROJECT STRUCTURE"
echo "==================="
echo "data/                           # Stock data (NASDAQ + Vietnam)"
echo "src/"
echo "  ├── deployment/"
echo "  │   ├── api/flask_server.py         # REST API"
echo "  │   ├── streamlit_app/app.py        # Web Dashboard"
echo "  │   └── airflow/dags/...            # Workflow DAG"
echo "  ├── models/                         # Model architectures"
echo "  ├── data/                           # Data processing"
echo "  ├── signals/                        # Trading signals"
echo "  ├── portfolio/                      # Portfolio optimization"
echo "  └── evaluation/                     # Backtesting & metrics"
echo ""

echo "📋 FILES TO CHECK"
echo "================"
echo "✓ README.md - Full documentation"
echo "✓ PROJECT_COMPLETION_SUMMARY.md - Task summary"
echo "✓ requirements.txt - All dependencies"
echo ""

echo "🎯 TASKS IMPLEMENTED"
echo "==================="
echo "✓ Task 1: NASDAQ Price Prediction (15%)"
echo "✓ Task 2: Vietnam Price Prediction (15%)"
echo "✓ Task 3: Trading Signals (20%)"  
echo "✓ Task 4: Portfolio Optimization (30%)"
echo "✓ Task 5: Deployment & Automation (30% - Extra Credit)"
echo ""

echo "🌐 API ENDPOINTS"
echo "================"
echo "GET  /health                    # Health check"
echo "GET  /predict                   # Get price prediction"
echo "GET  /signals                   # Get trading signals"
echo "GET  /portfolio                 # Get portfolio recommendation"
echo "POST /backtest                  # Run strategy backtest"
echo ""

echo "📊 EXAMPLE COMMANDS"
echo "==================="
echo "# Get AAPL prediction for 7 days"
echo "curl 'http://localhost:5000/predict?ticker=AAPL&days=7&market=nasdaq'"
echo ""
echo "# Get buy signals for stock"
echo "curl 'http://localhost:5000/signals?ticker=AAPL&signal_type=buy'"
echo ""
echo "# Get portfolio recommendation"
echo "curl 'http://localhost:5000/portfolio?profile=prudent&market=vietnam'"
echo ""

echo "✅ SETUP COMPLETE!"
echo "==================="
echo "You're ready to go! Choose a component above to get started."
