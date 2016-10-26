from flask_restful import Resource, reqparse

from src import auth, db
from src.utils.api import response
from src.model.todo import Todo


class Todos(Resource):

    @staticmethod
    @auth.requires_login
    def post():
        parser = reqparse.RequestParser()
        parser.add_argument(
            'title',
            type=str,
            help='no title provided',
            required=True,
            location='json'
        )
        parser.add_argument(
            'text',
            type=str,
            help='no text provided',
            required=True,
            location='json'
        )

        args = parser.parse_args()

        title = args['title']
        text = args['text']

        new_todo = Todo(title, text)
        db.session.add(new_todo)
        db.session.commit()

        return response(
            message='Todo created',
            status=201,
            data={
                'title': new_todo.title,
                'text': new_todo.text
            }
        )
