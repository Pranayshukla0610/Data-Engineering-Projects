from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

sys.path.append('/opt/airflow/scripts')

from data_cleaning import clean_inventory_data
from load_to_postgres import load_inventory_data



def start_pipeline():
    print('Inventory pipeline started')


with DAG(
    dag_id='inventory_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    start_task = PythonOperator(
        task_id='start_pipeline',
        python_callable=start_pipeline
    )

    clean_task = PythonOperator(
        task_id='clean_inventory_data',
        python_callable=clean_inventory_data
    )

    load_task = PythonOperator(
        task_id='load_to_postgres',
        python_callable=load_inventory_data
    )

    start_task >> clean_task >> load_task