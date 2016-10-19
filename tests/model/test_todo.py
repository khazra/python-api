import unittest

from tests.base import BaseTestCase
from src.model.todo import Todo


class TodoModelTestCase(BaseTestCase):

    def test_add_todo_to_db(self):
        new_todo = Todo('an example todo', 'text')
        self.assertEqual(new_todo.title, 'an example todo')
        self.assertEqual(new_todo.text, 'text')


if __name__ == '__main__':
    unittest.main()
