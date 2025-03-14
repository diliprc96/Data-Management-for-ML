import random

import requests
from faker import Faker
import pandas as pd
import schedule
import time
import logging
from sqlalchemy import create_engine
from sklearn.preprocessing import StandardScaler, LabelEncoder
import seaborn as sns
import matplotlib.pyplot as plt
# Setup Logging
logging.basicConfig(filename="data_ingestion.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Database Connection (PostgreSQL Example)
DB_CONNECTION = "postgresql://postgres:0000@localhost:5432/churn_db"
engine = create_engine(DB_CONNECTION)
faker = Faker()
plans = ["Free", "Basic", "Premium", "Enterprise"]

# API Source: Fetch Customer Orders from Fake Store API
API_URL = "https://fakestoreapi.com/carts"
def save_data_to_csv():
    num_customers = 2  # Adjust dataset size
    data = []
    for _ in range(num_customers):
        signup_date = faker.date_between(start_date='-5y', end_date='-1y')
        last_purchase_date = faker.date_between(start_date=signup_date, end_date='today')
        data.append({
            "customer_id": faker.uuid4(),
            "name": faker.random_element([None,faker.name()]),
            "age": faker.random_element(["thirty",random.randint(18, 50)]),
            "email": faker.email(),
            "signup_date": signup_date,
            "last_purchase_date": last_purchase_date,
            "total_spent": round(random.uniform(50, 10000), 2),
            "purchase_frequency": faker.random_element([random.randint(1, 50),"25"]),
            "monthly_spending": faker.random_element([random.randint(1, 50)]),
            "subscription_plan": faker.random_element(plans+[None]),
            "churned": random.choice([0, 1,None])  # 1 = Churned, 0 = Retained
        })

    df = pd.DataFrame(data)
    df.to_csv("synthetic_customer_data.csv", index=False)
    logging.info("✅ Synthetic dataset saved as 'synthetic_customer_data.csv'!")
    return df

def validate_data_types(df, rules):
    errors = []
    for col, rule in rules.items():
        if col in df.columns:
            expected_type = rule["dtype"]
            if expected_type == "datetime":
                try:
                    df[col] = pd.to_datetime(df[col], format=rule["format"], errors="coerce")
                    if df[col].isna().sum() > 0:
                        errors.append(f"Invalid datetime format in column {col}")
                except Exception as e:
                    errors.append(f"Error parsing datetime in column {col}: {e}")
    return errors

def validate_ranges(df, rules):
    errors = []
    for col, rule in rules.items():
        if col in df.columns and "range" in rule:
            min_val, max_val = rule["range"]
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(18)
            invalid_rows = df[(df[col] < min_val) | (df[col] > max_val)]
            if not invalid_rows.empty:
                errors.append(f"Out-of-range values in column {col}: Expected {min_val}-{max_val}, Found {invalid_rows[col].tolist()}")
    return errors

def validate_formats(df, rules):
    errors = []
    for col, rule in rules.items():
        if col in df.columns and "format" in rule and col=='email':
            pattern = rule["format"]
            invalid_rows = df[~df[col].astype(str).str.match(pattern, na=False)]
            if not invalid_rows.empty:
                errors.append(f"Invalid format in column {col}: {invalid_rows[col].tolist()}")
    return errors

# Function to detect outliers using IQR
def detect_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] < lower_bound) | (df[column] > upper_bound)]

def validation():

    df = pd.read_csv("synthetic_customer_data.csv")
    # df["name"] = df["name"].fillna(faker.name())
    logging.info("Missing Values:\n", df.isnull().sum())

    # Check data types
    logging.info(f'data types: {df.dtypes}')
    # Python Code for Data Cleaning
    missing_before = df.isnull().sum()
    logging.info(f"Missing values BEFORE filling:\n{missing_before}")
    # Log missing values AFTER filling
    missing_after = df.isnull().sum()
    print(f"Missing values AFTER filling:\n{missing_after}")
    # Define validation rules
    validation_rules = {
        "customer_id": {"dtype": int, "unique": True},
        "age": {"dtype": int, "range": (18, 100)},  # Age must be between 18-100
        "email": {"dtype": str, "format": r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"},
        "signup_date": {"dtype": "datetime", "format": "%Y-%m-%d"},
    }

    def validate_data(df, rules):
        errors = []

        errors.extend(validate_data_types(df, rules))
        errors.extend(validate_ranges(df, rules))
        errors.extend(validate_formats(df, rules))

        if errors:
            for error in errors:
                logging.error(error)
            print("Data validation failed. Check the log file for details.")
        else:
            logging.info("Data validation successful. No issues found.")
            print("Data validation passed!")

    # Run validation
    validate_data(df, validation_rules)
    df["name"] = df["name"].fillna(faker.name())
    df["churned"] = df["churned"].fillna(random.choice([0, 1]))
    df["subscription_plan"] = df["subscription_plan"].fillna(faker.random_element(plans))
    # Fill missing values in float64 columns using Forward + Backward Fill
    for column in df.select_dtypes(include="float64").columns:
        df[column] = df[column].ffill().bfill()
    for column in df.select_dtypes(include="object").columns:
        df[column] = df[column].ffill().bfill()
    encoder = LabelEncoder()
    df["subscription_plan"] = encoder.fit_transform(df["subscription_plan"])

    scaler = StandardScaler()
    df["total_spent"] = scaler.fit_transform(df[["total_spent"]])
    # Count churn by subscription plan
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="subscription_plan", hue="churned", palette="coolwarm")
    plt.title("Churn Rate by Subscription Plan")
    plt.xlabel("Subscription Plan")
    plt.ylabel("Count")
    plt.legend(["Not Churned", "Churned"])
    plt.show()
    # Age
    # Distribution
    plt.figure(figsize=(8, 5))
    sns.histplot(df["age"], bins=10, kde=True, color="blue")
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.show()

    # Spending
    # Distribution

    plt.figure(figsize=(8, 5))
    sns.boxplot(x=df["monthly_spending"], color="green")
    plt.title("Monthly Spending Distribution")
    plt.show()

    # Detect outliers in age and spending
    outliers_age = detect_outliers(df,"age")
    outliers_spending = detect_outliers(df, "monthly_spending")
    print("\nOutliers in Age:\n", outliers_age)
    print("\nOutliers in Monthly Spending:\n", outliers_spending)

    df.to_sql("customer_orders_data", engine, if_exists="append", index=False)





schedule.every(2).seconds.do(save_data_to_csv)
schedule.every(4).seconds.do(validation)
# Schedule Jobs: Fetch Data Every Hour
# schedule.every().hour.do(fetch_api_data)


logging.info("🚀 Data Ingestion Service Running...")
while True:
    schedule.run_pending()
    time.sleep(1)
# while True:
#     logging.info(111)
#     schedule.run_pending()
#     logging.info(44)
#     time.sleep(1)  # Check every minute
