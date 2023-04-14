from flask import Flask

# Создание экземпляра приложения
app = Flask(__name__)


@app.route('/')
def index():
    return 'The main page!'