from flask_testing import TestCase

from src import app
from src.utils.database import Database


class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_object('src.config.Test')
        return app

    def SetUp(self):
        Database.connect(app)
        # create db and populate it with data
