import logging
from flask import Flask
from flask_restful import Api
from api.user import User
from api.auth import Login
from utils.database import Database
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
api = Api(app)

app.config.update(
    MYSQL_DATABASE_USER='root',
    MYSQL_DATABASE_PASSWORD='',
    MYSQL_DATABASE_DB='python_api',
    MYSQL_DATABASE_HOST='127.0.0.1',

    SECRET_KEY='very scary secret key',
    TOKEN_RANDOM_STRING_LENGTH=16,
    TOKEN_VALIDITY_DURATION=3600,

    DEBUG=True,
    LOG_LEVEL=logging.INFO
)

Database.connect(app)

api.add_resource(Login, '/login')
api.add_resource(User, '/user/<int:id>')

if __name__ == '__main__':
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
    handler.setLevel(app.config['LOG_LEVEL'])
    app.logger.addHandler(handler)
    app.run(debug=app.config['DEBUG'])
