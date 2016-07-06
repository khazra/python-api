import os

from flask import Flask
from flask_restful import Api
from api.user import User
from api.auth import Login
from utils.database import Database
from logging.handlers import RotatingFileHandler
from itsdangerous import TimestampSigner

app = Flask(__name__)
api = Api(app)

app_settings = os.getenv(
    'APP_SETTINGS', 'config.Development')
app.config.from_object(app_settings)

Database.connect(app)
app.signer = TimestampSigner(app.config['SECRET_KEY'])

api.add_resource(Login, '/login')
api.add_resource(User, '/user/<int:id>')

if __name__ == '__main__':
    log_handler = RotatingFileHandler(
        app.config['LOGFILE_NAME'],
        maxBytes=app.config['LOGFILE_MAX_BYTES'],
        backupCount=app.config['LOGFILE_BACKUP_COUNT']
    )
    log_handler.setLevel(app.config['LOG_LEVEL'])
    app.logger.addHandler(log_handler)

    app.run(debug=app.config['DEBUG'])
