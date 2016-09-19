from flask_restful import Resource, reqparse

from src import app, auth, db
from src.model.user import User as user_model
from src.utils.api import response


class User(Resource):

    @staticmethod
    @auth.requires_login
    def get(id):
        user = user_model.query.filter_by(id=id).first()

        if user is not None:
            return response(
                message='User found',
                status=200,
                data={'username': user.username}
            )

        else:
            return response(
                status=404,
                message='User not found'
            )


class Users(Resource):

    @staticmethod
    @auth.requires_login
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument(
            'email',
            type=str,
            help='no email provided',
            required=True,
            location='json'
        )
        parser.add_argument(
            'password',
            type=str,
            help='no email provided',
            required=True,
            location='json'
        )

        args = parser.parse_args()

        username = args['email']
        password = args['password']

        user_exists = user_model.query.filter_by(
            username=username
        ).first() is not None

        if user_exists:
            return response(
                status=423,
                message='User already exists'
            )

        new_user = user_model(username, password)
        db.session.add(new_user)
        db.session.commit()

        return response(
            status=201,
            message='User created',
            data={
                'userId': new_user.id
            }
        )
