from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from utils.logger import get_logger


log = get_logger()


def my_print():
    log.critical("-----------------Q-----------------")
    return "-----------------Q-----------------"


default_args = {
    'owner': 'romank',
    'start_date': datetime.now(),
    'depends_on_past': False,
    'wait_for_downstream': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10),  # Retry every 10 seconds if failed
}

with DAG(
    'mydag',
    default_args=default_args,
    schedule_interval=timedelta(seconds=10),
    catchup=False,
    dagrun_timeout=timedelta(seconds=10)
) as dag:

    t1 = BashOperator(
        task_id='echo_hi',
        bash_command='echo "Hello"',
    )

    t2 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )
    t3 = PythonOperator(
        task_id='print_task',
        python_callable=my_print,
        show_return_value_in_logs=True
    )

    t3 >> t2 >> t1
