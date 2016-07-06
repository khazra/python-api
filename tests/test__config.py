import unittest
import logging

from app import app

from flask import current_app
from flask_testing import TestCase


class TestDevelopmentConfig(TestCase):

    def create_app(self):
        app.config.from_object('config.Development')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['LOG_LEVEL'] is logging.INFO)
        self.assertFalse(current_app is None)


if __name__ == '__main__':
    unittest.main()
