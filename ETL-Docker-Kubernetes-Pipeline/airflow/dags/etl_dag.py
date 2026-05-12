from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.append('/opt/airflow')

from scripts.run_pipeline import run_pipeline

default_args = {
    'owner': 'Pranay',
    'start_date': datetime(2025, 1, 1)
}

with DAG(
    dag_id='etl_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False
) as dag:

    run_etl = PythonOperator(
        task_id='run_pipeline',
        python_callable=run_pipeline
    )

    run_etl