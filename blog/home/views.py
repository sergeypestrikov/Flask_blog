from flask import Blueprint, render_template

# Объект блюпринта (эксиз) пользователя
home = Blueprint('home', __name__, url_prefix='/', static_folder='../static')


# Регистрация роута внутри блюпринта
@home.route('/')
def home_page():
    return render_template('home.html')