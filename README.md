# Data-Management-for-ML

API'based customer churn data was not available. so I have used only the CSV  data.
But,if the API is available, the corresponding code is given 
[Team name and contribution.md](<Team name and contribution.md>) - Team name and contribution.
* [api_data_ingestion.py](api_data_ingestion.py) - A sample code that fetches the data from API sources at a preiodic interval
* [csv_data_ingestion.py](csv_data_ingestion.py) - A sample code that monitors a given directory. As soon as a csv file is generated the ingestion is triggered.
* [data_generation.py](data_generation.py) - This code simulates the data collected in realtime, it generates defined data points at regular intervals to mimic the real world where data is received periodically. The data is collected and put into a postgre sql database.

* [synthetic_customer_data.csv](synthetic_customer_data.csv) is the sample file that is generated in defintie intervals.

* [data_ingestion](data_ingestion.log) is generated.

* [sample_data.csv](sample_dataset.csv) - Due to resource constraint the csv file is not fully generated. Therefore, a open source data is used to demonstrate the further process of the pipeline. [Kind request to accept this]

