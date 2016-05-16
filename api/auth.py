from flask import Blueprint, request, Response
from functools import wraps
auth = Blueprint('auth', __name__)


def check_auth(authorization_token):
    return authorization_token == 'token'


def authenticate():
    return Response('Not authorized', 401)


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        authorization_token = request.headers.get('Token')
        if not check_auth(authorization_token):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


@auth.route('/login', methods=['POST'])
@requires_auth
def login():
    return Response('OK', 200)


@auth.route('/logout', methods=['POST'])
def logout():
    return 'OK'
