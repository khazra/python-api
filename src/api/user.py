from flask_restful import Resource
from flask import Response, request

from src import app, auth, db
from src.model.user import User as user_model


class User(Resource):

    @staticmethod
    @auth.requires_login
    def get(id):
        user = user_model.query.filter_by(id=id).first()

        try:
            if user is not None:
                return Response('User found', 200, {'username': user.username})
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
            user_exists = user_model.query.filter_by(
                username=username
            ).first() is not None

            if user_exists:
                app.logger.info('INFO: User already exists: %s', username)
                return Response('User already exists', 423)

            new_user = user_model(username, password)
            db.session.add(new_user)
            db.session.commit()

            return Response('User created', 201, {
                'User-Id': new_user.id
            })

        except Exception as e:
            app.logger.error('ERROR: Exception raised: %s', str(e))
            return Response('Unknown error', 520)
