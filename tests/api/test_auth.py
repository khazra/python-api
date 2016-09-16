import unittest

from tests.base import BaseTestCase


class AuthApiTestCase(BaseTestCase):

    def test_valid_credentials(self):
        response = self.login('admin', 'admin')
        self.assertEqual(response.status, '200 OK')

    def test_bad_credentials(self):
        response = self.login('user', 'bad_password')
        self.assertEqual(response.status, '403 FORBIDDEN')

    def test_bad_content_type(self):
        response = self.login('user', 'bad_password', 'application/bad')
        self.assertEqual(response.status, '400 BAD REQUEST')

    def test_no_credentials(self):
        response = self.login(None, None)
        self.assertEqual(response.status, '400 BAD REQUEST')

    def test_auth_token_present(self):
        response = self.login('admin', 'admin')
        self.assertTrue(
            response.headers.get('Authentication-Token') is not None
        )


if __name__ == '__main__':
    unittest.main()
