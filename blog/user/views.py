from urllib import request

from werkzeug.exceptions import NotFound
from werkzeug.security import generate_password_hash
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user, login_user


from blog.extensions import db
from blog.forms.user import UserForm
from blog.models import User

# Объект блюпринта (эксиз) пользователя
user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@user.route('register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    form = UserForm(request.form)
    errors = []
    if request.method == 'POST' and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('Такая почта уже зарегистрирована')
            return render_template('users/register.html', form=form)

        _user = User(
            email=form.email.data,
            name=form.name.data,
            surname=form.surname.data,
            password=generate_password_hash(form.password.data),
        )

        db.session.add(_user)
        db.session.commit()

        login_user(_user)

    return render_template('users/register.html', form=form, errors=errors,)



# Регистрация роута внутри блюпринта
@user.route('/')
def user_list():
    from blog.models import User
    users = User.query.all()
    return render_template('users/list.html', users=users)


@user.route('/<int:pk>')
def get_user(pk: int):
    from blog.models import User

    _user = User.query.filter_by(id=pk).one_or_none()
    if not _user:
        raise NotFound(f'Пользователь с id{pk} не существует')
    return render_template('users/details.html', user=_user)


@user.route('/<int:pk>')
@login_required
def profile(pk: int):
    from blog.models import User

    _user = User.query.filter_by(id=pk).one_or_none()
    if not _user:
        raise NotFound(f'Пользователь с id{pk} не существует')
    return render_template('users/profile.html', user=_user)


