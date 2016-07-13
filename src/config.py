import logging


class Base(object):
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = ''
    MYSQL_DATABASE_DB = 'python_api'
    MYSQL_DATABASE_HOST = '127.0.0.1'

    SECRET_KEY = 'very scary secret key'
    TOKEN_RANDOM_STRING_LENGTH = 16
    TOKEN_VALIDITY_DURATION = 3600

    LOGFILE_PATH = 'src/logs/app.log'
    LOGFILE_MAX_BYTES = 10000
    LOGFILE_BACKUP_COUNT = 1

    ADMIN_DEFAULT_PASSWD = ('8c6976e5b5410415bde908bd4dee15df'
                            'b167a9c873fc4bb8a81f6f2ab448a918')


class Development(Base):
    DEBUG = True
    LOG_LEVEL = logging.INFO


class Production(Base):
    DEBUG = False
    LOG_LEVEL = logging.ERROR


class Test(Base):
    MYSQL_DATABASE_DB = 'python_api_test'
    DEBUG = True
    LOG_LEVEL = logging.INFO
    TESTING = True
