import logging
import logging.config
import os

from Application.Core.settings import LOGGERS


if not os.path.exists(LOGGERS.APP_STATE.PATH):
    os.makedirs(LOGGERS.APP_STATE.PATH)

if not os.path.exists(LOGGERS.REQUEST.PATH):
    os.makedirs(LOGGERS.REQUEST.PATH)


LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'app_state': {
            'format': LOGGERS.APP_STATE.FORMAT
        },
        'request': {
            'format': LOGGERS.REQUEST.FORMAT,
        },
    },
    'handlers': {
        'app_state': {
            'level': 'INFO',
            'formatter': 'app_state',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f"{LOGGERS.APP_STATE.PATH}/{LOGGERS.APP_STATE.FILE_NAME}",
            'when': 'midnight',
        },
        'request': {
            'level': 'INFO',
            'formatter': 'request',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': f"{LOGGERS.REQUEST.PATH}/{LOGGERS.REQUEST.FILE_NAME}",
            'when': 'midnight',
        },
    },
    'loggers': {
        'uvicorn.error': {
            'handlers': ['app_state'],
            'level': 'DEBUG',
        },
        'Utils.Logger.middleware': {
            'handlers': ['request'],
            'level': 'DEBUG',
        },
        'Utils.Core.router': {
            'handlers': ['request'],
            'level': 'DEBUG',
        },
    }
}

logging.config.dictConfig(LOGGING_CONFIG)


def get_logger(name: str):
    return logging.getLogger(name)
