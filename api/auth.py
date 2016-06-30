from flask import Response, request, json
from flask_restful import Resource
from utils.database import Database
from api.user import User


class Login(Resource):
    def post(self):
        try:
            json_body = request.get_json()
            username = json_body.get('email')
            password = json_body.get('password')

            userId = self.__get_user_id(username, password)

            if userId is None:
                return Response('Username or Password is wrong', 403)
            else:
                return Response(response=json.dumps(User.get(userId)),
                                status=200,
                                mimetype='application/json')

        except Exception as e:
            return e

    @staticmethod
    def __get_user_id(username, password):
        cursor = Database.connection.cursor()
        query = ("SELECT UserId from users where "
                 "Username='{0}' and "
                 "Password='{1}'").format(username, password)
        cursor.execute(query)
        return cursor.fetchone()[0]


class Logout(Resource):
    def post(self):
        return 'OK'
