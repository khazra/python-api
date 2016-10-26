import unittest
import json

from tests.base import BaseTestCase


class CreateTodoTestCase(BaseTestCase):

    def test_cannot_create_todo_if_unlogged(self):
        response = self.client.post('/todo')
        self.assertEqual(response.status, '401 UNAUTHORIZED')

    def test_cannot_create_if_no_data_is_provided(self):
        self.login('admin', 'admin')
        response = self.auth_post('/todo')
        self.assertEqual(response.status, '400 BAD REQUEST')

    def test_cannot_create_if_no_title_is_provided(self):
        self.login('admin', 'admin')
        response = self.auth_post('/todo', data={
            'text': 'some text'
        })
        self.assertEqual(response.status, '400 BAD REQUEST')

    def test_cannot_create_if_no_text_is_provided(self):
        self.login('admin', 'admin')
        response = self.auth_post('/todo', data={
            'title': 'some title'
        })
        self.assertEqual(response.status, '400 BAD REQUEST')

    def test_create_todo(self):
        todo_title = 'some title'
        todo_text = 'some text'

        self.login('admin', 'admin')
        response = self.auth_post('/todo', data={
            'title': todo_title,
            'text': todo_text
        })
        response_data = json.loads(response.data).get('data')

        self.assertEqual(response.status, '201 CREATED')
        self.assertEqual(response_data.get('title'), todo_title)
        self.assertEqual(response_data.get('text'), todo_text)


if __name__ == '__main__':
    unittest.main()
