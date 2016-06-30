from flask import Flask
from flask_restful import Api
from api.user import User
from api.auth import Login, Logout
from utils.database import Database

app = Flask(__name__)
api = Api(app)

app.config['MYSQL_DATABASE_USER'] = 'admin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'python-api'
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'

Database.connect(app)

api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(debug=True)
