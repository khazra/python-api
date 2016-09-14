import unittest

from base import BaseTestCase
from flask import current_app as app
from src.utils.auth import Auth


class TestAuthUtils(BaseTestCase):

    auth = Auth(app)

    def test_auth_init(self):
        self.assertTrue(self.auth.signer is not None)
        self.assertEqual(self.app, app)


if __name__ == '__main__':
    unittest.main()
