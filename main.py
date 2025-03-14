# main.py
import pandas as pd
import logging
from Data_validation import validate_data

# Set up logging
logging.basicConfig(filename='data_validation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Load the data
    df = pd.read_csv('/workspaces/Data-Management-for-ML/sample_dataset.csv')  # Adjust this path as needed

    # Define validation rules
    rules = {
        "customerID": {
            "dtype": "string"
        },
        "gender": {
            "format": r"^(Male|Female)$"
        },
        "SeniorCitizen": {
            "dtype": "numeric",
            "range": [0, 1]
        },
        "Partner": {
            "format": r"^(Yes|No)$"
        },
        "Dependents": {
            "format": r"^(Yes|No)$"
        },
        "tenure": {
            "dtype": "numeric",
            "range": [0, 100]
        },
        "PhoneService": {
            "format": r"^(Yes|No)$"
        },
        "MultipleLines": {
            "format": r"^(Yes|No|No phone service)$"
        },
        "InternetService": {
            "format": r"^(DSL|Fiber optic|No)$"
        },
        "OnlineSecurity": {
            "format": r"^(Yes|No|No internet service)$"
        },
        "DeviceProtection": {
            "format": r"^(Yes|No|No internet service)$"
        },
        "TechSupport": {
            "format": r"^(Yes|No|No internet service)$"
        },
        "StreamingTV": {
            "format": r"^(Yes|No|No internet service)$"
        },
        "StreamingMovies": {
            "format": r"^(Yes|No|No internet service)$"
        },
        "Contract": {
            "format": r"^(Month-to-month|One year|Two year)$"
        },
        "PaperlessBilling": {
            "format": r"^(Yes|No)$"
        },
        "PaymentMethod": {
            "format": r"^(Electronic check|Mailed check|Bank transfer \(automatic\)|Credit card \(automatic\))$"
        },
        "MonthlyCharges": {
            "dtype": "numeric",
            "range": [0, 1000]
        },
        "TotalCharges": {
            "dtype": "numeric"
        },
        "Churn": {
            "format": r"^(Yes|No)$"
        }
    }

    # Call the validation function
    validate_data(df, rules, logging)
    
if __name__ == "__main__":
    main()
