from flask_restful import Resource, reqparse
from utils.database import Database


class CreateUser(Resource):
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str,
                                help='Email address to create user')
            parser.add_argument('password', type=str,
                                help='Password to create user')
            args = parser.parse_args()

            _userEmail = args['email']
            _userPassword = args['password']

            cursor = Database.connection.cursor()
            cursor.callproc('spCreateUser', (_userEmail, _userPassword))
            data = cursor.fetchall()

            if len(data) is 0:
                Database.connection.commit()
                return {
                    'StatusCode': '200',
                    'Message': 'User creation success'
                }

            else:
                return {'StatusCode': '1000', 'Message': str(data[0])}

        except Exception as e:
            return {
                'error': str(e)
            }
