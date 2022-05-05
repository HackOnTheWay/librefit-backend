from json import load
from dotenv import load_dotenv

import os

load_dotenv()

class Config(object):
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI= os.environ.get('DB_URL')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    