from flask import Flask
from api.auth import auth
app = Flask(__name__)


app.register_blueprint(auth)
app.run(debug=True)
