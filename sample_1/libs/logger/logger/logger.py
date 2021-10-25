import logging


formatter = "%(asctime)s %(levelname)s : %(pathname)s %(lineno)d : %(message)s"
logging.basicConfig(level=logging.INFO, format=formatter)


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger
