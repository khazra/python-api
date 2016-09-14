import datetime
from src import db, auth


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    role = db.Column(db.String(16), nullable=False, default='USER')
    created = db.Column(db.DateTime, nullable=False,
                        default=datetime.datetime.now())
    modified = db.Column(db.DateTime,
                         nullable=False,
                         default=datetime.datetime.now(),
                         onupdate=datetime.datetime.now()
                         )
    active = db.Column(db.Boolean, nullable=False, default=0)

    def __init__(self, username, password, active=False, role='USER'):
        self.username = username
        self.password = auth.hash_password(password)
        self.active = active
        self.role = role

    def __repr__(self):
        return '<User %r>' % self.username
