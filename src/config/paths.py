from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / 'data'
NASDAQ_DIR = DATA_DIR / 'nasdaq' / 'csv'
VIETNAM_DIR = DATA_DIR / 'vietnam' / 'data-vn-20230228'

MODEL_DIR = BASE_DIR / 'saved_models'
REPORT_DIR = BASE_DIR / 'reports'