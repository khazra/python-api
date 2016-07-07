from flask import request, Response
from flask import current_app as app

from functools import wraps
from itsdangerous import BadSignature, SignatureExpired
from random import choice
from string import ascii_letters
import hashlib


class Auth:
    @classmethod
    def requires_login(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            authentication_token = request.headers.get('Authentication-Token')

            if not authentication_token or not self.__is_token_valid(
                    authentication_token):
                return Response('Not authorized', 401)

            return f(*args, **kwargs)

        return decorated

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password).hexdigest()

    @classmethod
    def generate_auth_token(self):
        token_random_string = ''.join(
            choice(ascii_letters) for i in range(
                app.config['TOKEN_RANDOM_STRING_LENGTH']))

        signed = app.signer.sign(token_random_string)

        app.logger.info('INFO: Authorized with token %s', signed)

        return signed

    @classmethod
    def __is_token_valid(self, authentication_token):
        try:
            app.signer.unsign(
                authentication_token,
                max_age=app.config['TOKEN_VALIDITY_DURATION']
            )

        except SignatureExpired as e:
            app.logger.info('INFO: SignatureExpired, %s', str(e))
            return False    # valid token, but expired
        except BadSignature as e:
            app.logger.info('INFO: BadSignature, %s', str(e))
            return False    # invalid token

        return True
