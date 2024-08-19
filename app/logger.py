import logging
import sys


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    format = logging.Formatter("%(levelname)s:     %(message)s")
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setFormatter(format)
    logger.addHandler(stream_handler)
    return logger
