from flask import Response
from flask_restful import Resource
from utils.auth import Auth


class Login(Resource):
    @Auth.requires_auth
    def post(self):
        return Response('OK', 200)


class Logout(Resource):
    @Auth.requires_auth
    def post(self):
        return 'OK'
