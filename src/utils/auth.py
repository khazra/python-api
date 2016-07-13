from flask import request, Response

from functools import wraps
from itsdangerous import BadSignature, SignatureExpired, TimestampSigner
from random import choice
from string import ascii_letters
import hashlib


class Auth:

    @classmethod
    def __init__(self, app):
        self.signer = TimestampSigner(app.config['SECRET_KEY'])
        self.app = app

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
                self.app.config['TOKEN_RANDOM_STRING_LENGTH']))

        signed = self.signer.sign(token_random_string)

        self.app.logger.info('INFO: Authorized with token %s', signed)

        return signed

    @classmethod
    def __is_token_valid(self, authentication_token):
        try:
            self.signer.unsign(
                authentication_token,
                max_age=self.app.config['TOKEN_VALIDITY_DURATION']
            )

        except SignatureExpired as e:
            self.app.logger.info('INFO: SignatureExpired, %s', str(e))
            return False    # valid token, but expired
        except BadSignature as e:
            self.app.logger.info('INFO: BadSignature, %s', str(e))
            return False    # invalid token

        return True
