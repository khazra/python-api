from flask_restful import Resource, reqparse

from src import auth
from src.model.user import User as user_model
from src.utils.api import response


class Login(Resource):

    def post(self):
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
            help='no password provided',
            required=True,
            location='json'
        )
        args = parser.parse_args()

        username = args['email']
        password = args['password']

        if self.__credentials_valid(username, password):
                return response(
                    status=200,
                    message='Credentials valid',
                    data={
                        'authenticationToken': auth.generate_auth_token()
                    }
                )

        else:
            return response(
                status=403,
                message='Wrong authentication data'
            )

    @staticmethod
    def __credentials_valid(username, password):
        hashed_password = auth.hash_password(password)

        valid = user_model.query.filter_by(username=username,
                                           password=hashed_password).first()

        if valid is not None:
            return True

        return False
