from flask_restful import Resource
from utils.database import Database


class User(Resource):
    @staticmethod
    def get(id):
        try:
            cursor = Database.connection.cursor()
            query = ("SELECT UserName from users "
                     "where UserId='{0}'").format(id)
            cursor.execute(query)
            return cursor.fetchone()

        except Exception as e:
            return {
                'error': str(e)
            }