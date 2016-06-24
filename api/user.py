from flask_restful import Resource


class CreateUser(Resource):
    def post(self):
        return {
            'status': 'success'
        }
