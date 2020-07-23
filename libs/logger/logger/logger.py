import logging

logging.basicConfig(level=logging.INFO)


def get_logger(name: str, level: int = logging.INFO):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger
