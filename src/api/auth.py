from flask import Response, request
from flask_restful import Resource
from flask import current_app as app

from src.utils.database import Database
from src.utils.auth import Auth


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
                return Auth.generate_auth_token()
            else:
                return Response('Wrong authentication data', 403)

        except Exception as e:
            app.logger.error('ERROR: Exception raised: %s', str(e))
            return Response('Unknown error', 520)

    @staticmethod
    def __credentials_valid(username, password):
        hashed_password = Auth.hash_password(password)
        cursor = Database.connection.cursor()
        query = ("SELECT id from users where "
                 "username='{0}' and "
                 "password='{1}'").format(username, hashed_password)
        cursor.execute(query)
        data = cursor.fetchone()

        if data:
            return True

        return False
