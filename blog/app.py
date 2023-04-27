from flask import Flask

# Фабрика по созданию приложений
from blog import commands
from blog.extensions import db, login_manager, migrate
from blog.models import User


# Точка входа в приложение. Создание экземпляра приложения
def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('blog.config')

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)
    # Который возвращает экземпляр приложения
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # @login_manager.user_loader
    # def unauthorized():
    #     return redirect(url_for('auth.login'))


# Регистрация блюпринта в приложении
def register_blueprints(app: Flask):
    from blog.auth.views import auth
    from blog.user.views import user
    from blog.articles.views import article
    from blog.home.views import home

    app.register_blueprint(user)
    app.register_blueprint(auth)
    app.register_blueprint(article)
    app.register_blueprint(home)


def register_commands(app: Flask):
#     app.cli.add_command(commands.init_db)
    app.cli.add_command(commands.create_init_user)