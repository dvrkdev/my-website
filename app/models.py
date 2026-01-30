from flask_login import UserMixin

from app.extensions import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False, unique=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"{self.id}: {self.username}"
