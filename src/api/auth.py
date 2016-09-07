from flask import Response, request
from flask_restful import Resource

from src import app, auth
from src.model.user import UserModel as user


class Login(Resource):

    def post(self):
        try:
            json_body = request.get_json()

            if not json_body:
                return Response('Content type must be application/json', 400)

            username = json_body.get('email')
            password = json_body.get('password')

            if not username or not password:
                return Response('Please provide username and password', 400)

            if self.__credentials_valid(username, password):
                return auth.generate_auth_token()
            else:
                return Response('Wrong authentication data', 403)

        except Exception as e:
            app.logger.error('ERROR: Exception raised: %s', str(e))
            return Response('Unknown error', 520)

    @staticmethod
    def __credentials_valid(username, password):
        hashed_password = auth.hash_password(password)

        data = user.get_user_id_by_name_and_password(username, hashed_password)

        if data is not None:
            return True

        return False
