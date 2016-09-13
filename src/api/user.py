from flask_restful import Resource
from flask import Response, request

from src import app, auth
from src.model.user import UserModel as user


class User(Resource):

    @staticmethod
    @auth.requires_login
    def get(id):
        username = user.get_username_by_id(id)

        try:
            if username is not None:
                return Response('User found', 200, {'username': username})
            else:
                return Response('User not found', 404)

        except Exception as e:
            app.logger.error('ERROR: Exception raised: %s', str(e))
            return Response('Unknown error', 520)


class Users(Resource):

    @staticmethod
    @auth.requires_login
    def post():
        json_body = request.get_json()

        if not json_body:
            return Response('Bad content type', 400)

        username = json_body.get('email')
        password = json_body.get('password')

        if not username or not password:
            return Response(
                'Please provide username and password for user', 400)

        try:
            if user.get_user_id_by_name(username) is not None:
                app.logger.info('INFO: User already exists: %s', username)
                return Response('User already exists', 423)

            new_user = user.create(username, auth.hash_password(password))
            return Response('User created', 201, {
                'User-Id': new_user
            })

        except Exception as e:
            app.logger.error('ERROR: Exception raised: %s', str(e))
            return Response('Unknown error', 520)
