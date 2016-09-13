import unittest
import logging

from src.app import app

from flask import current_app
from flask_testing import TestCase


class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('src.config.Development')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['LOG_LEVEL'] is logging.INFO)
        self.assertFalse(current_app is None)


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('src.config.Production')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)
        self.assertTrue(app.config['LOG_LEVEL'] is logging.ERROR)
        self.assertFalse(current_app is None)


class TestTestConfig(TestCase):
    def create_app(self):
        app.config.from_object('src.config.Test')
        return app

    def test_app_is_test(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['LOG_LEVEL'] is logging.INFO)
        self.assertTrue(app.config['MYSQL_DATABASE_DB'] is 'python_api_test')
        self.assertFalse(current_app is None)


if __name__ == '__main__':
    unittest.main()
