from distutils.command.config import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

#app config
app = Flask(__name__)

app.config.from_object(config)

#database config
db = SQLAlchemy(app)


    