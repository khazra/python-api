from flask_restful import Resource
from flask import Response, request

from src import app, auth, db


class User(Resource):

    @staticmethod
    @auth.requires_login
    def get(id):
        if not id:
            return Response('Specify user id', 400)

        with db.connection as cursor:
            try:
                query = ("SELECT username from users "
                         "where id='{0}'").format(id)
                cursor.execute(query)
                return cursor.fetchone()

            except Exception as e:
                app.logger.error('ERROR: Exception raised: %s', str(e))
                return Response('Unknown error', 520)


class Users(Resource):

    @staticmethod
    @auth.requires_login
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
            db.create_user(username, auth.hash_password(password))
            return Response('User created', 201)

        except Exception as e:
            app.logger.error('ERROR: Exception raised: %s', str(e))
            return Response('Unknown error', 520)
