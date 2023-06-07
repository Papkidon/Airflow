from datetime import datetime

from airflow.decorators import dag
from airflow.operators.python import PythonOperator
from scripts.save import save_to_db
from scripts.scrape import scrape_from_olx

from airflow import DAG

default_args = {"start_date": datetime(2023, 6, 8)}


@dag(schedule="@daily", default_args=default_args, catchup=False)
def scrape_dag():
    # scrape_items_task = PythonOperator(
    #     task_id="scrape",
    #     python_callable=scrape_from_olx,
    #     op_kwargs={"item": "iphone"},
    # )

    # save_items_task: PythonOperator = PythonOperator(
    #     task_id="save",
    #     python_callable=save_to_db,
    # )

    scrape_from_olx(save_to_db())


scrape_dag()
