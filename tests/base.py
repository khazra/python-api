import json

from flask_testing import TestCase

from src.app import app
from src import db


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('src.config.Test')
        return app

    def setUp(self):
        self.db = db

    def tearDown(self):
        self.db.drop_all_tables()

    def login(self, username, password):
        return self.client.post('/login', data=json.dumps(dict(
            email=username,
            password=password
        )), follow_redirects=True, content_type='application/json')
