from logger.logger import get_logger
from lib_one.main import main as lib_one_main


def main():
    logger = get_logger(__name__)
    logger.info("hello project one!")
    lib_one_main()


if __name__ == '__main__':
    main()
