from json import load
from dotenv import load_dotenv

import os

load_dotenv()

class Config(object):
    SECRET_KEY = os.environ.get('JWT_SECRET_KEY')