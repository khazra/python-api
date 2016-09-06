from flask_testing import TestCase

from src.app import app
from src.utils.database import Database
from src.model.user import UserModel as user


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('src.config.Test')
        return app

    def setup(self):
        Database(app)
        user.create('test_user1', 'test_pass')
