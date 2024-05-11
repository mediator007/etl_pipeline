from utils.logger import get_logger


log = get_logger()


def start() -> None:
    log.info("ETL STARTED")


def stop() -> None:
    log.info("ETL STOPPED")
