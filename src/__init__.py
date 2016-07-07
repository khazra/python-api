import os

from flask import Flask
from flask_restful import Api

from logging.handlers import RotatingFileHandler
from itsdangerous import TimestampSigner

from src.api.user import User
from src.api.auth import Login
from src.utils.database import Database


app = Flask(__name__)
api = Api(app)

# load settings from proper config file
# for prod, set APP_SETTINGS env variable to src.config.Production
# export APP_SETTINGS='src.config.Production'
app_settings = os.getenv(
    'APP_SETTINGS', 'src.config.Development')
app.config.from_object(app_settings)

Database.connect(app)

# init signer for creating signed authentication tokens
app.signer = TimestampSigner(app.config['SECRET_KEY'])

# init log handler
log_handler = RotatingFileHandler(
    app.config['LOGFILE_PATH'],
    maxBytes=app.config['LOGFILE_MAX_BYTES'],
    backupCount=app.config['LOGFILE_BACKUP_COUNT']
)
log_handler.setLevel(app.config['LOG_LEVEL'])
app.logger.addHandler(log_handler)

# API endpoints
api.add_resource(Login, '/login')
api.add_resource(User, '/user/<int:id>')

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
