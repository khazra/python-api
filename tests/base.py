import json

from flask_testing import TestCase

from src.app import app
from src import db
from src.model.user import User


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('src.config.Test')
        return app

    def setUp(self):
        db.create_all()
        admin = User('admin', 'admin', True, 'ADMIN')
        db.session.add(admin)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def login(self, username, password, content_type='application/json'):
        response = self.client.post('/login', data=json.dumps(dict(
            email=username,
            password=password
        )), follow_redirects=True, content_type=content_type)

        self.auth_token = response.headers.get('Authentication-Token')
        return response

    def auth_get(self, uri, headers={}):
        headers.update({
            'Authentication-Token': self.auth_token
        })
        return self.client.get(uri, headers=headers)

    def auth_post(self, uri, headers={}, data={}):
        headers.update({
            'Authentication-Token': self.auth_token
        })
        return self.client.post(
            uri,
            headers=headers,
            data=json.dumps(data),
            content_type='application/json'
        )
