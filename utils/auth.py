from flask import request, Response
from flask import current_app as app

from functools import wraps
from itsdangerous import TimestampSigner, BadSignature, SignatureExpired
from random import choice
from string import ascii_letters
import hashlib


class Auth:
    @classmethod
    def requires_login(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            authorization_token = request.headers.get('Token')
            if not self._is_token_valid(authorization_token):
                return self._authenticate()
            return f(*args, **kwargs)
        return decorated

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password).hexdigest()

    @classmethod
    def generate_auth_token(self):
        signer = TimestampSigner(app.config['SECRET_KEY'])

        token_random_string = ''.join(
            choice(ascii_letters) for i in range(
                app.config['TOKEN_RANDOM_STRING_LENGTH']))

        signed = signer.sign(token_random_string)

        app.logger.info('INFO: Authorized with token %s', signed)

        return signed

    @classmethod
    def _is_token_valid(self, authorization_token):
        signer = TimestampSigner(app.config['SECRET_KEY'])

        app.logger.info('INFO: %s', str(signer))

        try:
            signer.unsign(
                authorization_token,
                max_age=app.config['TOKEN_VALIDITY_DURATION']
            )

        except SignatureExpired as e:
            app.logger.info('INFO: %s', str(e))
            return False    # valid token, but expired
        except BadSignature as e:
            app.logger.info('INFO: %s', str(e))
            return False    # invalid token

        return True

    @staticmethod
    def _authenticate():
        return Response('Not authorized', 401)
