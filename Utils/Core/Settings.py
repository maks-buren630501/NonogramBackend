import datetime

APP_NAME = 'Nonogram'
APP_VERSION = '1.0'
DEBUG = True

LOGGING = {
    'LEVEL': 'DEBUG',
    'LEVEL_FILE': 'DEBUG',
    'DIRECTORY': f'LOGS {APP_VERSION}',
    'FILE_NAME': f'{datetime.date.today()}',
    'CONTENT_FORMAT': '%(asctime)s [%(levelname)s] | %(message)s',
    'DATE_FORMAT': '%d-%b-%y %H:%M:%S'
}
