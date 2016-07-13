from src import app, api

from src.api.user import User, Users
from src.api.auth import Login


# API endpoints
api.add_resource(Login, '/login')
api.add_resource(Users, '/user')
api.add_resource(User, '/user/<int:id>')

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
