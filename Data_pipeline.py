from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import os

def ingest_data():
    df = pd.read_csv("data/raw_data.csv")
    df.to_csv("data/ingested_data.csv", index=False)
    print("Data ingestion complete.")

def validate_data():
    df = pd.read_csv("data/ingested_data.csv")
    missing = df.isnull().sum()
    if missing.any():
        raise ValueError(f"Missing values found:\n{missing}")
    print("Data validation passed.")

def prepare_data():
    df = pd.read_csv("data/ingested_data.csv")
    df["customer_tenure_years"] = df["tenure"] / 12  # Example feature engineering
    df.to_csv("data/transformed_data.csv", index=False)
    print("Data transformation complete.")

def store_data():
    os.system("dvc add data/transformed_data.csv && git commit -m 'Updated transformed dataset'")
    print("Data stored in version control.")

# Define DAG
with DAG(
    "data_pipeline",
    default_args={"start_date": datetime(2024, 3, 14), "retries": 1},
    schedule_interval="@daily",
    catchup=False,
) as dag:

    task_ingest = PythonOperator(task_id="ingest_data", python_callable=ingest_data)
    task_validate = PythonOperator(task_id="validate_data", python_callable=validate_data)
    task_prepare = PythonOperator(task_id="prepare_data", python_callable=prepare_data)
    task_store = PythonOperator(task_id="store_data", python_callable=store_data)

    # Define dependencies
    task_ingest >> task_validate >> task_prepare >> task_store
