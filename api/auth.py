from flask import Blueprint
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST'])
def login():
    return 'OK'


@auth.route('/logout', methods=['POST'])
def logout():
    return 'OK'
