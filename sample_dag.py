# Import required libraries
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta 
# Default arguments for the DAG
default_args = {
    'owner': 'airflow',  # Update this to the desired start date
    'retries': 5,
}

# Define the DAG
dag = DAG(
    'sample_dag',  # This is the DAG ID
    default_args=default_args,
    description='A simple sample DAG for testing',
    schedule_interval=None,  # Set to `None` for manual triggering
)

# Dummy start task
start_task = DummyOperator(
    task_id='start',
    dag=dag,
)

# Python function to be executed by the PythonOperator
def print_hello():
    print("Hello from Airflow!")

# Python task to print a message
python_task = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

# Dummy end task
end_task = DummyOperator(
    task_id='end',
    dag=dag,
)

# Set task dependencies
start_task >> python_task >> end_task
