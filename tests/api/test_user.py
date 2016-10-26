import unittest
import json

from tests.base import BaseTestCase


class GetUserTestCase(BaseTestCase):

    def test_cannot_get_user_if_unlogged(self):
        response = self.client.get('/user/1')
        self.assertEqual(response.status, self.response_status(401))

    def test_404_when_wrong_id(self):
        self.login('admin', 'admin')
        response = self.auth_get('/user/wrong_id')
        self.assertEqual(response.status, self.response_status(404))

    def test_get_user(self):
        self.login('admin', 'admin')
        response = self.auth_get('/user/1')
        response_data = json.loads(response.data).get('data')
        self.assertEqual(response.status, self.response_status(200))
        self.assertTrue(response_data.get('username') is not None)


class CreateUserTestCase(BaseTestCase):

    def test_cannot_create_if_unlogged(self):
        response = self.client.post('/user')
        self.assertEqual(response.status, self.response_status(401))

    def test_cannot_create_if_no_data_is_provided(self):
        self.login('admin', 'admin')
        response = self.auth_post('/user')
        self.assertEqual(response.status, self.response_status(400))

    def test_cannot_create_if_only_password(self):
        self.login('admin', 'admin')
        response = self.auth_post('/user', data={
            'password': 'paass'
        })
        self.assertEqual(response.status, self.response_status(400))

    def test_cannot_create_if_only_username(self):
        self.login('admin', 'admin')
        response = self.auth_post('/user', data={
            'email': 'user'
        })
        self.assertEqual(response.status, self.response_status(400))

    def test_cannot_create_if_user_exists(self):
        self.login('admin', 'admin')
        response = self.auth_post('/user', data={
            'email': 'admin',
            'password': 'admin'
        })
        self.assertEqual(response.status, self.response_status(423))

    def test_create_user(self):
        self.login('admin', 'admin')
        response = self.auth_post('/user', data={
            'email': 'new_user@ex.pl',
            'password': 'pass'
        })
        self.assertEqual(response.status, self.response_status(201))


if __name__ == '__main__':
    unittest.main()
