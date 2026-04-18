from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.append('/app')

from pipelines.main_pipeline import run_pipeline

default_args = {
    'owner': 'pranay',
    'start_date': datetime(2024, 1, 1)
}

with DAG(
    dag_id='sales_pipeline',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    run_etl = PythonOperator(
        task_id='run_pipeline',
        python_callable=run_pipeline
    )