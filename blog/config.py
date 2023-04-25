import os

from dotenv import load_dotenv

from blog.enums import Envtype

load_dotenv()

ENV = os.getenv('FLASK_ENV', default=Envtype.production)
DEBUG = ENV == Envtype.development

SECRET_KEY = os.getenv('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False


# class BaseConfig(object):
#     DEBUG = False
#     TESTING = False
#     SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SECRET_KEY = "^ihiq&vwj2o)4$+qc=gkl5q4&0jnus)(=o&@2h-$)*kr6k6aj&"
#
#
# class DevConfig(BaseConfig):
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
#
#
# class TestingConfig(BaseConfig):
#     TESTING = True