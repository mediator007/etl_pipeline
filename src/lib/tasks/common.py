from utils.logger import get_logger


log = get_logger()


def start():
    log.info("ETL STARTED")


def stop():
    log.info("ETL STOPPED")
