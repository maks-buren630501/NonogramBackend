import os
import logging
from Utils.Core.Settings import LOGGING


if not os.path.exists(LOGGING['DIRECTORY']):
    os.mkdir(LOGGING['DIRECTORY'])

logger = logging.getLogger()
logger.setLevel(LOGGING["LEVEL"])

handler = logging.FileHandler(filename=f"{LOGGING['DIRECTORY']}/{LOGGING['FILE_NAME']}.log", mode='a+')
handler.setLevel(LOGGING["LEVEL_FILE"])
formatter = logging.Formatter(LOGGING['CONTENT_FORMAT'], datefmt=LOGGING['DATE_FORMAT'])
handler.setFormatter(formatter)

logger.addHandler(handler)
