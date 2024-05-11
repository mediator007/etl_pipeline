import logging
import inspect


def init_logging(log: logging.Logger):
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '[%(asctime)s] - [%(name)s(%(lineno)d)] - [%(levelname)s] - [%(message)s]',
        datefmt="%Y-%m-%d %H:%M:%S"
        )
    handler.setFormatter(formatter)
    log.addHandler(handler)


def get_logger(name: str | None = None) -> logging.Logger:
    frame = inspect.currentframe().f_back
    module_name = frame.f_globals['__name__']
    if name:
        module_name = name
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)
    init_logging(logger)
    return logger
