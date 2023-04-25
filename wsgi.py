from werkzeug.security import generate_password_hash

from blog.extensions import db
from blog.app import create_app

app = create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(
        host='0.0.0.0',
        port=5050,
        debug=True
    )


# Команда init_db нужная для инициализации базы при первом запуске
@app.cli.command('init-db')
def init_db():

    db.create_all()
    print('База Данных инициализирована!')


# Команда create_users, которая поможет создавать пользователей
@app.cli.command('create-users')
def create_users():
    from blog.models import User

    db.session.add(
        User(email='name@email.com', password=generate_password_hash('test123'))
    )
    db.session.commit()
    print('Прекрасно! Создан пользователь')
