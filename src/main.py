from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


from settings import Settings
from lib.tasks.get_universities import get_universities
from lib.tasks.transform_universities import transform_universities
from lib.tasks import common

settings = Settings()


default_args = {
    'start_date': datetime.now(),
    'depends_on_past': False,
    'wait_for_downstream': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10),
}

with DAG(
    settings.universities_etl_pipeline_name,
    default_args=default_args,
    schedule_interval=timedelta(seconds=10),
    catchup=False,
    dagrun_timeout=timedelta(seconds=10)
) as dag:

    start_task = PythonOperator(
        task_id='start_task',
        python_callable=common.start,
        show_return_value_in_logs=True
    )

    stop_task = PythonOperator(
        task_id='stop_task',
        python_callable=common.stop,
        show_return_value_in_logs=True
    )

    get_data = PythonOperator(
        task_id='get_data',
        python_callable=get_universities,
        show_return_value_in_logs=False
    )

    transform_data = PythonOperator(
        task_id='transform_data',
        python_callable=transform_universities,
        show_return_value_in_logs=False
    )

    start_task >> get_data >> transform_data >> stop_task
