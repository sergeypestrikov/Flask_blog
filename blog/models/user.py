from sqlalchemy import Column, Integer, String, Boolean
from flask_login import UserMixin
from blog.models.database import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))