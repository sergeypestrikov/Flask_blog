import os

from dotenv import load_dotenv

from blog.enums import Envtype

load_dotenv()

ENV = os.getenv('FLASK_ENV', default=Envtype.production)
DEBUG = ENV == Envtype.development

SECRET_KEY = os.getenv('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WTF_CSRF_ENABLED = True