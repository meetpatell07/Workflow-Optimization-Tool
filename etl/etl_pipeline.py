import pandas as pd
import os

# File paths
RAW_DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'raw_jira_data.csv')
PROCESSED_DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'processed_data.csv')

# Extract function: Read raw data from CSV
def extract():
    try:
        raw_data = pd.read_csv(RAW_DATA_PATH)
        print("Data extracted successfully")
        return raw_data
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

# Transform function: Analyze and clean data
def transform(raw_data):
    try:
        # Convert relevant columns to datetime
        raw_data['due_date'] = pd.to_datetime(raw_data['due_date'], errors='coerce')
        raw_data['created_at'] = pd.to_datetime(raw_data['created_at'], errors='coerce')
        raw_data['completed_at'] = pd.to_datetime(raw_data['completed_at'], errors='coerce')

        # Filter tasks that are overdue or not completed
        overdue_tasks = raw_data[raw_data['due_date'] < pd.to_datetime('today')]
        overdue_tasks = overdue_tasks[overdue_tasks['status'].str.lower() != 'done']
        
        # Process workflow performance (e.g., completion time)
        raw_data['completion_time'] = raw_data['completed_at'] - raw_data['created_at']
        raw_data['completion_time'] = raw_data['completion_time'].dt.days

        print("Data transformed successfully")
        return raw_data, overdue_tasks
    except Exception as e:
        print(f"Error transforming data: {e}")
        return None, None

# Load function: Save transformed data
def load(processed_data):
    try:
        processed_data.to_csv(PROCESSED_DATA_PATH, index=False)
        print(f"Data loaded successfully to {PROCESSED_DATA_PATH}")
    except Exception as e:
        print(f"Error loading data: {e}")

# ETL pipeline execution
def run_etl():
    print("Starting ETL pipeline...")
    raw_data = extract()  # Step 1: Extract
    if raw_data is not None:
        transformed_data, overdue_tasks = transform(raw_data)  # Step 2: Transform
        if transformed_data is not None:
            load(transformed_data)  # Step 3: Load
    print("ETL pipeline completed.")
    
if __name__ == "__main__":
    run_etl()
