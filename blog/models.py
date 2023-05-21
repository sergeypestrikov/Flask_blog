from datetime import datetime


from flask_login import UserMixin
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship

from blog.extensions import db


# Таблица тагов/статей
article_tag_association_table = Table(
    'article_tag_association',
    db.metadata,
    db.Column('article_id', db.Integer, ForeignKey('articles.id'), nullable=False),
    db.Column('tag_id', db.Integer, ForeignKey('tags.id'), nullable=False),
)


# Модель пользователя
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    surname = db.Column(db.String(40))
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))

    author = relationship('Author', uselist=False, back_populates='user')

    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password


# Модель автора
class Author(db.Model):
    __tablename__ = 'authors'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='author')
    articles = relationship('Article', back_populates='author')


# Модель статьи
class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, ForeignKey('authors.id'), nullable=False)
    title = db.Column(db.String(255))
    text = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    author = relationship('Author', back_populates='articles')
    tags = relationship('Tag', secondary=article_tag_association_table, back_populates='articles')


# Модель тега
class Tag(db.Model):
    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)

    articles = relationship('Article', secondary=article_tag_association_table, back_populates='tags')