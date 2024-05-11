import requests

from utils.logger import get_logger


log = get_logger()


def get_universities() -> list[dict]:
    UNIVERSITIES_URL = "http://universities/search"
    response = requests.get(UNIVERSITIES_URL)
    universities_data = response.json()
    log.info(f"Universities quantity {len(universities_data)}")
    return universities_data
