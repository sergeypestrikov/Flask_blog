from flask import Flask, redirect, url_for

import os

# Фабрика по созданию приложений
from blog.auth.views import auth
from blog.user.views import user
from blog.articles.views import article
from blog.home.views import home
from blog.models.database import db
from flask_login import LoginManager

login_manager = LoginManager()


# Точка входа в приложение. Создание экземпляра приложения
def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config['SECRET_KEY'] = '^ihiq&vwj2o)4$+qc=gkl5q4&0jnus)(=o&@2h-$)*kr6k6aj&'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        User.query.get(int(user_id))

    # @login_manager.user_loader
    # def unauthorized():
    #     return redirect(url_for('auth.login'))

    register_blueprints(app)
    # Который возвращает экземпляр приложения
    return app


# Регистрация блюпринта в приложении
def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(auth)
    app.register_blueprint(article)
    app.register_blueprint(home)