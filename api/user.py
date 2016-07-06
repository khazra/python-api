from flask_restful import Resource
from flask import current_app as app

from utils.database import Database
from utils.auth import Auth


class User(Resource):
    @staticmethod
    @Auth.requires_login
    def get(id):
        try:
            cursor = Database.connection.cursor()
            query = ("SELECT username from users "
                     "where id='{0}'").format(id)
            cursor.execute(query)
            return cursor.fetchone()

        except Exception as e:
            app.logger.error('ERROR: Exception raised: %s', str(e))
