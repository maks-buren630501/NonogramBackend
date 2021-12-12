import os
import logging
from Utils.Core.settings import LOGGING


if not os.path.exists(LOGGING['DIRECTORY']):
    os.mkdir(LOGGING['DIRECTORY'])


def get_request_handler():
    file_handler = logging.FileHandler(filename=f"{LOGGING['DIRECTORY']}/{LOGGING['FILE_NAME']}.log", mode='a+')
    file_handler.setLevel(LOGGING["LEVEL_FILE"])
    file_handler.setFormatter(logging.Formatter(LOGGING['CONTENT_FORMAT'], datefmt=LOGGING['DATE_FORMAT']))
    return file_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(LOGGING["LEVEL"])
    logger.addHandler(get_request_handler())
    return logger
