import os

from flask import Flask
from flask_restful import Api

from logging.handlers import RotatingFileHandler

from src.utils.database import Database
from src.utils.auth import Auth


app = Flask(__name__)
api = Api(app)

# load settings from proper config file
# for prod, set APP_SETTINGS env variable to src.config.Production
# export APP_SETTINGS='src.config.Production'
app_settings = os.getenv(
    'APP_SETTINGS', 'src.config.Development')
app.config.from_object(app_settings)

# connect to db
db = Database(app)

# init auth utils for generating api tokens etc.
auth = Auth(app)

# init log handler
log_handler = RotatingFileHandler(
    app.config['LOGFILE_PATH'],
    maxBytes=app.config['LOGFILE_MAX_BYTES'],
    backupCount=app.config['LOGFILE_BACKUP_COUNT']
)
log_handler.setLevel(app.config['LOG_LEVEL'])
app.logger.addHandler(log_handler)
