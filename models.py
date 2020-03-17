#encoding: utf-8
from exts import db


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    username = db.Column(db.String(50),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    # email = db.Column(db.String(50),nullable=False)