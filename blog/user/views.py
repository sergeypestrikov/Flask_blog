from werkzeug.exceptions import NotFound
from flask import Blueprint, render_template, redirect

# Объект блюпринта (эксиз) пользователя
user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


USERS = {
    1: {'name': 'Сергей'},
    2: {'name': 'Жанна'},
    3: {'name': 'Лев'},
}


# Регистрация роута внутри блюпринта
@user.route('/')
def user_list():
    return render_template('users/list.html', users=USERS)


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user_id = USERS[pk]
    except KeyError:
        raise NotFound(f'Пользователь с id {pk} не найден')
        # return redirect('/users')
    return render_template(
        'users/details.html',
        user_name=user_id['name']
    )


def get_user_name(pk: int):
    if pk in USERS:
        user_name = USERS[pk]['name']
    else:
        raise NotFound(f'Пользователь с id:{pk} не найден')
    return user_name