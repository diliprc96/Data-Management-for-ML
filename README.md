# Data-Management-for-ML

API-based customer churn data was not available, so I have used only the CSV data.
However, if the API is available, the corresponding code is given below:

## Team Contributions
[Team name and contribution.md](<Team name and contribution.md>) - Team name and contribution.

## Data Ingestion
* [api_data_ingestion.py](api_data_ingestion.py) - A sample code that fetches the data from API sources at a periodic interval.
* [csv_data_ingestion.py](csv_data_ingestion.py) - A sample code that monitors a given directory. As soon as a CSV file is generated, the ingestion is triggered.
* [data_generation.py](data_generation.py) - This code simulates the data collected in real-time, generating defined data points at regular intervals to mimic real-world periodic data reception. The data is collected and stored in a PostgreSQL database.

## Data Files
* [synthetic_customer_data.csv](synthetic_customer_data.csv) - A sample file that is generated at defined intervals.
* [data_ingestion.log](data_ingestion.log) - Log file for data ingestion process.
* [sample_dataset.csv](sample_dataset.csv) - Due to resource constraints, the CSV file is not fully generated. Therefore, an open-source dataset is used to demonstrate further pipeline processing. **[Kind request to accept this]**

## Data Processing & Feature Engineering
* [data_preparation.ipynb](data_preparation.ipynb) - Data transformation and feature engineering steps.
* [data_validation.py](data_validation.py) - Code for validating the dataset to ensure quality.
* [data_validation.log](data_validation.log) - Log file for data validation steps.
* [Data_transformation_sql](Data_transformation_sql) - SQL-based transformation logic.

## Feature Store & Versioning
* [feature_store.py](feature_store.py) - Implements a feature store to manage engineered features.
* [Data_versioning.sh](Data_versioning.sh) - Script to version raw and transformed datasets using DVC/Git.

## Orchestration
* [Data_pipeline.py](Data_pipeline.py) - Apache Airflow DAG to automate data pipeline execution.
* [airflow_terminal_output.txt](airflow_terminal_output.txt) - Logs of pipeline runs in Airflow.

## Metadata & Documentation
* [meta_data_schema.json](meta_data_schema.json) - Schema definition for the dataset.
* [Problem Formulation.md](Problem Formulation.md) - Document explaining the problem statement.
* [Folder_structure.md](Folder_structure.md) - Structure of the project directory.
* [LICENSE](LICENSE) - License for the project.

## Visualizations & Insights
* [data_vis_plot2.png](data_vis_plot2.png), [data_vis_plot3.png](data_vis_plot3.png), [data_visualization_plot.png](data_visualization_plot.png) - Plots generated from data analysis.
* Additional plots: [newplot (3).png](newplot (3).png) to [newplot (9).png](newplot (9).png)

## Raw Data & Storage
* [raw_data/](raw_data) - Directory containing raw data files.
* [raw_data_storage.py](raw_data_storage.py) - Script for storing raw data.
* [customer_data.parquet](customer_data.parquet) - Parquet format dataset for efficient storage and retrieval.

## Execution
The model building is integrated within the data preparation process in [data_preparation.ipynb](data_preparation.ipynb).
