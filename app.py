from flask import Flask
from flask_restful import Api
from api.user import CreateUser
from api.auth import Login, Logout

app = Flask(__name__)
api = Api(app)


api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(CreateUser, '/createUser')

if __name__ == '__main__':
    app.run(debug=True)
