import logging

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    named_logger = logging.getLogger(name)
    named_logger.setLevel(level)
    return named_logger
