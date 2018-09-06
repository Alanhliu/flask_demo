from sqlalchemy import Column

from app import db
from sqlalchemy.orm import class_mapper


class User(db.Model):
    __tablename__ = 'user'
    uid: int = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __init__(self, username: object, password: object) -> object:
        self.username = username
        self.password = password

    def as_dict(obj):
        return dict((col.name, getattr(obj, col.name)) \
                    for col in class_mapper(obj.__class__).mapped_table.c)

    def __repr__(self):
        return '<User %r>' % self.username

# class Admin(db.Model):
#     __tablename__ = 'admins'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(320), unique=True)
#     password = db.Column(db.String(32), nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username
