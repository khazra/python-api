from flask_restful import Resource
from flask import current_app as app, Response, request

from src.utils.auth import Auth


class User(Resource):
    @staticmethod
    @Auth.requires_login
    def get(id=None, name=None):
        if not id and not name:
            return Response('Specify username or user id', 400)

        with app.db.connection:
            try:
                cursor = app.db.connection.cursor()
                query = ("SELECT username from users "
                         "where id='{0}'").format(id)
                cursor.execute(query)
                return cursor.fetchone()

            except Exception as e:
                app.logger.error('ERROR: Exception raised: %s', str(e))
                return Response('Unknown error', 520)


class Users(Resource):
    @staticmethod
    @Auth.requires_login
    def post():
        json_body = request.get_json()

        if not json_body:
            return Response('Content type must be application/json', 400)

        username = json_body.get('email')
        password = json_body.get('password')

        if not username or not password:
            return Response(
                'Please provide username and password for user', 400)

        try:
            app.db.create_user(username, Auth.hash_password(password))
            return Response('User created', 201)

        except Exception as e:
            app.logger.error('ERROR: Exception raised: %s', str(e))
            return Response('Unknown error', 520)
