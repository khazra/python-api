import unittest
import hashlib

from base import BaseTestCase
from src.model.user import User


class UserModelTestCase(BaseTestCase):

    def test_add_user_to_db(self):
        new_user = User('test_user', 'pass')
        self.assertEqual(new_user.username, 'test_user')
        self.assertEqual(
            new_user.password,
            hashlib.sha256('pass').hexdigest()
        )
        self.assertFalse(new_user.active)
        self.assertEqual(new_user.role, 'USER')

    def test_add_admin_user_to_db(self):
        new_admin_user = User('admin_user', 'pass', True, 'ADMIN')
        self.assertEqual(new_admin_user.username, 'admin_user')
        self.assertEqual(
            new_admin_user.password,
            hashlib.sha256('pass').hexdigest()
        )
        self.assertTrue(new_admin_user.active)
        self.assertEqual(new_admin_user.role, 'ADMIN')


if __name__ == '__main__':
    unittest.main()
