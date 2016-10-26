import unittest
import json

from tests.base import BaseTestCase


class AuthApiTestCase(BaseTestCase):

    def test_valid_credentials(self):
        response = self.login('admin', 'admin')
        self.assertEqual(response.status, self.response_status(200))

    def test_bad_credentials(self):
        response = self.login('user', 'bad_password')
        self.assertEqual(response.status, self.response_status(403))

    def test_bad_content_type(self):
        response = self.login('user', 'bad_password', 'application/bad')
        self.assertEqual(response.status, self.response_status(400))

    def test_no_credentials(self):
        response = self.client.post(
            '/login',
            data=json.dumps({}),
            follow_redirects=True,
            content_type='application/json'
        )
        self.assertEqual(response.status, self.response_status(400))

    def test_auth_token_present(self):
        response = self.login('admin', 'admin')
        response_data = json.loads(response.data).get('data')
        self.assertTrue(
            response_data.get('authenticationToken') is not None
        )


if __name__ == '__main__':
    unittest.main()
