from airflow import DAG
from airflow.operators import BashOperator
from datetime import datetime, timedelta

# Following are defaults which can be overridden later on
default_args = {
    'owner': 'stivenramireza',
    'depends_on_past': False,
    'start_date': datetime(2018, 9, 28),
    'email': ['stivenramireza@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'schedule_interval': '1 * * * *',
}

dag = DAG('airflow-poc', default_args=default_args)

# run_script run a bash script

run_script = BashOperator(
    task_id='run_scrapy_script',
    bash_command='scrapy crawl finca-raiz',
    dag=dag)s