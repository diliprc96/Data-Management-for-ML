import os
import pandas as pd
import time
import logging
from datetime import datetime

# Setup Logging
log_file = "ingestion_log.csv"
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s,%(message)s')

# Paths
SOURCE_DIR = "data_source"
DEST_DIR = "raw_data"

os.makedirs(DEST_DIR, exist_ok=True)

def ingest_csv():
    """Moves CSV files from the source directory to the raw data directory."""
    for file in os.listdir(SOURCE_DIR):
        if file.endswith(".csv"):
            src_path = os.path.join(SOURCE_DIR, file)
            dest_path = os.path.join(DEST_DIR, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{file}")

            try:
                df = pd.read_csv(src_path)
                df.to_csv(dest_path, index=False)  # Save in raw format
                os.remove(src_path)
                logging.info(f"SUCCESS,CSV,{file},{dest_path}")
                print(f"Ingested {file} successfully.")
            except Exception as e:
                logging.error(f"FAILURE,CSV,{file},{e}")

# Automate Ingestion (Runs every hour)
while True:
    ingest_csv()
    time.sleep(3600)  # Sleep for 1 hour
