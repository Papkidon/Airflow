from datetime import datetime

from airflow.operators.python import PythonOperator
from scripts.save import save_to_db
from scripts.scrape import scrape_from_olx

from airflow import DAG

with DAG(
    "scrape_items",
    start_date=datetime(2023, 6, 5),
    schedule_interval="@hourly",
    catchup=False,
) as dag:
    scrape_items_task = PythonOperator(
        task_id="scrape",
        python_callable=scrape_from_olx,
        op_kwargs={"item": "iphone"},
    )

    save_items_task: PythonOperator = PythonOperator(
        task_id="save",
        python_callable=save_to_db,
    )

    scrape_items_task >> save_items_task
