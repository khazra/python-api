import logging


class Base(object):
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_DB = 'python_api'
    MYSQL_DATABASE_HOST = '127.0.0.1'

    SECRET_KEY = 'very scary secret key'
    TOKEN_RANDOM_STRING_LENGTH = 16
    TOKEN_VALIDITY_DURATION = 3600

    LOGFILE_NAME = 'app.log'
    LOGFILE_MAX_BYTES = 10000
    LOGFILE_BACKUP_COUNT = 1


class Development(Base):
    DEBUG = True
    LOG_LEVEL = logging.INFO


class Production(Base):
    DEBUG = False
    LOG_LEVEL = logging.ERROR