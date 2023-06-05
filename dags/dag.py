from datetime import datetime

from airflow.operators.python import PythonOperator
from scripts.scrape import scrape_from_olx

from airflow import DAG

with DAG(
    "scrape_items",
    start_date=datetime(2023, 6, 5),
    schedule_interval="@hourly",
    catchup=False,
) as dag:
    training_model_tasks = [
        PythonOperator(
            task_id=f"olx",
            python_callable=scrape_from_olx,
            op_kwargs={"item": "iphone"},
        )
    ]
    training_model_tasks
