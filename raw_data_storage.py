import os
import shutil
from datetime import datetime

# Base Directory
BASE_DIR = "data_lake"

# Define Data Sources and Types
DATA_SOURCES = {
    "transactions": ["csv"],
    "customer_support": ["json"],
    "web_activity": ["logs"],
    "market_sentiment": ["txt"]
}

# Function to generate folder path dynamically
def get_storage_path(source, data_type):
    date_partition = datetime.today().strftime('%Y-%m-%d')
    return os.path.join(BASE_DIR, source, data_type, date_partition, "raw")

# Ensure directories exist
for source, types in DATA_SOURCES.items():
    for data_type in types:
        path = get_storage_path(source, data_type)
        os.makedirs(path, exist_ok=True)

# Function to move files to the respective raw storage folder
def store_raw_data(source, data_type, source_folder):
    dest_folder = get_storage_path(source, data_type)
    
    for file in os.listdir(source_folder):
        src_path = os.path.join(source_folder, file)
        dest_path = os.path.join(dest_folder, file)
        
        if os.path.isfile(src_path):
            shutil.move(src_path, dest_path)
            print(f"Moved {file} → {dest_path}")

# Example Usage: Moving CSV transaction files to their correct location
source_data_folder = "source_files/transactions"
store_raw_data("transactions", "csv", source_data_folder)
