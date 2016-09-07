import unittest

from base import BaseTestCase


class UserApiTestCase(BaseTestCase):

    def test_create_user(self):
        response = self.login('admin', 'admin')
        self.assertEqual(response.status, '200 OK')

if __name__ == '__main__':
    unittest.main()
