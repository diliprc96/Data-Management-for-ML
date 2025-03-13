import requests
import json
import os
import logging
from datetime import datetime
import time

# Setup Logging
log_file = "ingestion_log.csv"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s,%(message)s')

# API Configuration
API_URL = "https://api.example.com/customer_churn"
HEADERS = {"Authorization": "Bearer YOUR_API_KEY"}

# Destination Directory
RAW_DIR = "raw_api_data"
os.makedirs(RAW_DIR, exist_ok=True)

def fetch_api_data():
    """Fetches customer churn data from an API and stores it in raw JSON format."""
    try:
        response = requests.get(API_URL, headers=HEADERS)
        response.raise_for_status()  # Raise an error for failed requests
        
        data = response.json()
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_path = os.path.join(RAW_DIR, f"api_data_{timestamp}.json")
        
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        
        logging.info(f"SUCCESS,API,{file_path}")
        print(f"API data fetched successfully: {file_path}")
    except Exception as e:
        logging.error(f"FAILURE,API,{e}")
        print(f"API fetch failed: {e}")

# Automate API Ingestion (Runs every hour)
while True:
    fetch_api_data()
    time.sleep(3600)  # Sleep for 1 hour
