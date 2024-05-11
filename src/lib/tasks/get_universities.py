import requests as r
from airflow.decorators import task

from utils.logger import get_logger


log = get_logger()


UNIVERSITIES_URL = "http://universities/search"


@task
def get_universities():
    response = r.get(UNIVERSITIES_URL)
    log.info(f"Universities Quantity: {len(response.json())}")
    return response.json()
