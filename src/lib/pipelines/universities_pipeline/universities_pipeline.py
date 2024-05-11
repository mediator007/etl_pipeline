from datetime import datetime, timedelta

from airflow import DAG

from settings import Settings


settings = Settings()


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.now(),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 10,
    'retry_delay': timedelta(seconds=5),
}

dag = DAG(
    settings.universities_etl_pipeline_name,
    default_args=default_args,
    schedule_interval=settings.etl_pipeline_schedule,
)
