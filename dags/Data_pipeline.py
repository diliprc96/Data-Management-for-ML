import os
import logging
import pandas as pd
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# File paths
RAW_DATA_PATH = "data/raw_data.csv"
INGESTED_DATA_PATH = "data/ingested_data.csv"
TRANSFORMED_DATA_PATH = "data/transformed_data.csv"

def ingest_data():
    try:
        if not os.path.exists("data"):
            os.makedirs("data")  # Ensure directory exists
        df = pd.read_csv(RAW_DATA_PATH)
        df.to_csv(INGESTED_DATA_PATH, index=False)
        logger.info("Data ingestion complete.")
    except Exception as e:
        logger.error(f"Data ingestion failed: {e}")
        raise

def validate_data():
    try:
        df = pd.read_csv(INGESTED_DATA_PATH)
        missing = df.isnull().sum()
        if missing.any():
            raise ValueError(f"Missing values found:\n{missing}")
        logger.info("Data validation passed.")
    except Exception as e:
        logger.error(f"Data validation failed: {e}")
        raise

def prepare_data():
    try:
        df = pd.read_csv(INGESTED_DATA_PATH)
        df["customer_tenure_years"] = df["tenure"] / 12  # Example feature engineering
        df.to_csv(TRANSFORMED_DATA_PATH, index=False)
        logger.info("Data transformation complete.")
    except Exception as e:
        logger.error(f"Data preparation failed: {e}")
        raise

def store_data():
    try:
        os.system(f"dvc add {TRANSFORMED_DATA_PATH} && git commit -m 'Updated transformed dataset'")
        logger.info("Data stored in version control.")
    except Exception as e:
        logger.error(f"Data storage failed: {e}")
        raise

# Define DAG
with DAG(
    "Data_pipeline",
    default_args={"start_date": datetime(2023, 3, 18), "retries": 5},
    schedule_interval="@daily",  # Use `schedule_interval` instead of `schedule`
    catchup=False,
) as dag:

    task_ingest = PythonOperator(task_id="ingest_data", python_callable=ingest_data)
    task_validate = PythonOperator(task_id="validate_data", python_callable=validate_data)
    task_prepare = PythonOperator(task_id="prepare_data", python_callable=prepare_data)
    task_store = PythonOperator(task_id="store_data", python_callable=store_data)

    # Define dependencies
    task_ingest >> task_validate >> task_prepare >> task_store
