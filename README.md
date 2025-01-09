# Workflow Optimization and Reporting Tool

## Overview
This project automates the **ETL** process for analyzing project management data, optimizes workflows, and visualizes insights using **Power BI**.

## Features:
- **ETL Pipeline**: Extracts, transforms, and loads project data (e.g., Jira).
- **Overdue Tasks**: Identify overdue tasks in the workflow.
- **Task Completion Times**: Analyze how long tasks take to complete.
- **Power BI Reports**: Visualize insights with Power BI for decision-making.

## Setup

1. **Install Dependencies**:
    ```bash
    pip install -r etl/requirements.txt
    ```

2. **Run the ETL Pipeline**:
    ```bash
    python etl/etl_pipeline.py
    ```

3. **Open Power BI** and load the `processed_data.csv` to create visualizations.

## Screenshots

### ETL Pipeline in Action
![ETL Pipeline](./images/Screenshot%202025-01-08%20220836.png)

### Power BI Reports
![Power BI Report](./images/Screenshot%20(181).png)

## License
This project is licensed under the MIT License.
