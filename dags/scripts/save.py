from airflow.decorators import task
from pandas import DataFrame


@task
def save_to_db(df: DataFrame):
    # scraped_data = ti.xcom_pull(
    #     task_ids=[
    #         "scrape_from_olx",
    #     ]
    # )
    if not df:
        raise Exception("Data could not been scraped")
    # Save into the db
    print("Scraped data ", df)
    print("Saving to db....")
    return ...
