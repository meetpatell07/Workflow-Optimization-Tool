import pandas as pd
import os

# File paths
RAW_DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'raw_jira_data.csv')
PROCESSED_DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'processed_data.csv')