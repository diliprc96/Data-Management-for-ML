# validation_functions.py (This will contain the validation logic)

import pandas as pd
import logging

def validate_data_types(df, rules):
    errors = []
    for col, rule in rules.items():
        if col in df.columns:
            expected_type = rule.get("dtype")
            if expected_type == "numeric":
                # Check if the column can be converted to numeric
                try:
                    df[col] = pd.to_numeric(df[col], errors="coerce")
                except Exception as e:
                    errors.append(f"Error converting column {col} to numeric: {e}")
            elif expected_type == "string":
                # Check if the column is of string type
                if not pd.api.types.is_string_dtype(df[col]):
                    errors.append(f"Column {col} is not of type string.")
    return errors

def validate_ranges(df, rules):
    errors = []
    for col, rule in rules.items():
        if col in df.columns and "range" in rule:
            min_val, max_val = rule["range"]
            invalid_rows = df[(df[col] < min_val) | (df[col] > max_val)]
            if not invalid_rows.empty:
                errors.append(f"Out-of-range values in column {col}: Expected {min_val}-{max_val}, Found {invalid_rows[col].tolist()}")
    return errors

def validate_formats(df, rules):
    errors = []
    for col, rule in rules.items():
        if col in df.columns and "format" in rule:
            pattern = rule["format"]
            invalid_rows = df[~df[col].astype(str).str.match(pattern, na=False)]
            if not invalid_rows.empty:
                errors.append(f"Invalid format in column {col}: {invalid_rows[col].tolist()}")
    return errors

def validate_data(df, rules, logging):
    errors = []

    # Validate data types
    errors.extend(validate_data_types(df, rules))
    
    # Validate ranges for numeric columns
    errors.extend(validate_ranges(df, rules))
    
    # Validate format rules for categorical columns
    errors.extend(validate_formats(df, rules))

    if errors:
        for error in errors:
            logging.error(error)
        print("Data validation failed. Check the log file for details.")
    else:
        logging.info("Data validation successful. No issues found.")
        print("Data validation passed!")
