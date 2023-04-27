import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


# Команда init_db нужная для инициализации базы при первом запуске
# @app.cli.command('init-db')
# def init_db():
#
#     db.create_all()
#     print('База Данных инициализирована!')


# Команда create_init_user, которая поможет создавать пользователей
@click.command('create-init-user')
def create_init_user():
    from blog.models import User
    from wsgi import app

    db.session.add(
        User(email='name@email.com', password=generate_password_hash('test123'))
    )
    db.session.commit()
    print('Прекрасно! Создан пользователь')