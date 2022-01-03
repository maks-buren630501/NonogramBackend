from dataclasses import dataclass


@dataclass
class APP:
    APP_NAME: str = 'Nonogram'
    APP_VERSION: str = '0.1'
    DEBUG: bool = True


@dataclass
class LOGGER:
    PATH: str
    FILE_NAME: str
    FORMAT: str


@dataclass
class LOGGERS:
    APP_STATE = LOGGER(
        PATH=f"Logs {APP.APP_NAME} {APP.APP_VERSION}/Server_status",
        FILE_NAME='app.log',
        FORMAT='%(levelname)s %(message)s %(asctime)s'
    )
    REQUEST = LOGGER(
        PATH=f"Logs {APP.APP_NAME} {APP.APP_VERSION}/Requests",
        FILE_NAME='requests.log',
        FORMAT='%(levelname)s %(asctime)s %(message)s'
    )

