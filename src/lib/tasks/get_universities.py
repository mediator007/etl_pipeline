import requests

from utils.logger import get_logger


log = get_logger()


def get_universities():
    UNIVERSITIES_URL = "http://universities/search"
    response = requests.get(UNIVERSITIES_URL)
    log.info(f"Universities quantity {len(response.json())}")
