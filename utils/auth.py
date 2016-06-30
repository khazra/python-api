from flask import request, Response
from functools import wraps


class Auth():
    @staticmethod
    def _check_auth(authorization_token):
        return authorization_token == 'token'

    @staticmethod
    def _authenticate():
        return Response('Not authorized', 401)

    @classmethod
    def requires_auth(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            authorization_token = request.headers.get('Token')
            if not self._check_auth(authorization_token):
                return self._authenticate()
            return f(*args, **kwargs)
        return decorated
