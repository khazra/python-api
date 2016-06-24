from flask import request, Response
from functools import wraps


class Auth():
    @classmethod
    def _check_auth(self, authorization_token):
        return authorization_token == 'token'

    @classmethod
    def _authenticate(self):
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
