from sqlalchemy import Column, Integer, String, Boolean
from blog.models.database import db
from sqlalchemy.orm import relationship


class Article(db.Model):
    __tablename__ = 'articles'

    title = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    bloger = relationship('User')
