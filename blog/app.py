from flask import Flask

# Фабрика по созданию приложений
from blog.user.views import user
from blog.articles.views import article
from blog.home.views import home


# Точка входа в приложение. Создание экземпляра приложения
def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    # Который возвращает экземпляр приложения
    return app


# Регистрация блюпринта в приложении
def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
    app.register_blueprint(home)
