from wtforms import StringField, validators, PasswordField, SubmitField
from flask_wtf import FlaskForm


class UserForm(FlaskForm):
    name = StringField('Имя')
    surname = StringField('Фамилия')
    email = StringField('Эл почта', [validators.DataRequired(), validators.Email()])
    password = PasswordField('Пароль', [validators.DataRequired(), validators.EqualTo('confirm_password', message='Значение должно соответствовать значению пароля')])
    confirm_password = PasswordField('Подтверждение пароля', [validators.DataRequired()])
    submit = SubmitField('Регистрация')