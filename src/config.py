import logging


class Base(object):
    SECRET_KEY = 'replace this to something more appriopriate :)'
    TOKEN_RANDOM_STRING_LENGTH = 16
    TOKEN_VALIDITY_DURATION = 3600

    LOGFILE_PATH = 'app.log'
    LOGFILE_MAX_BYTES = 10000
    LOGFILE_BACKUP_COUNT = 1

    ADMIN_DEFAULT_PASSWD = ('8c6976e5b5410415bde908bd4dee15df'
                            'b167a9c873fc4bb8a81f6f2ab448a918')
    ADMIN_DEFAULT_NAME = 'admin'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    USER_ROLES = {
        'admin': 'ADMIN',
        'user': 'USER'
    }


class Development(Base):
    SQLALCHEMY_DATABASE_URI = 'mysql://dev:dev@localhost/python_api'
    DEBUG = True
    LOG_LEVEL = logging.INFO


class Production(Base):
    SQLALCHEMY_DATABASE_URI = ''
    DEBUG = False
    LOG_LEVEL = logging.ERROR


class Test(Base):
    SQLALCHEMY_DATABASE_URI = 'mysql://test:test@localhost/python_api_test'
    DEBUG = True
    LOG_LEVEL = logging.INFO
    TESTING = True
    LIVESERVER_PORT = 7001
    LIVESERVER_TIMEOUT = 10
