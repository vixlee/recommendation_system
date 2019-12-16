from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String)
    fullname = db.Column(db.String(120))

    def __init__(self, username, email, password, fullname):
        self.username = username
        self.email = email
        self.password = password
        self.fullname = fullname