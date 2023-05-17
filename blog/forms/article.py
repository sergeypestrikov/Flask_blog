from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, TextAreaField, SelectMultipleField


# Форма создания статьи
class CreateArticleForm(FlaskForm):
    title = StringField('Заголовок', [validators.DataRequired()])
    text = TextAreaField('Текст статьи', [validators.DataRequired()])
    tags = SelectMultipleField('Теги', coerce=int)
    submit = SubmitField('Создать')
