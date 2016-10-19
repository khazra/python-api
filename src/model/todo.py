import datetime
from src import db


class Todo(db.Model):

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(128), nullable=False)
    text = db.Column(db.String(264), nullable=False)
    created = db.Column(db.DateTime, nullable=False,
                        default=datetime.datetime.now())
    modified = db.Column(db.DateTime,
                         nullable=False,
                         default=datetime.datetime.now(),
                         onupdate=datetime.datetime.now()
                         )
    completed = db.Column(db.Boolean, nullable=False, default=0)

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return '<Todo %r>' % self.title
