from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

#app config
app = Flask(__name__)

app.config.from_object(Config)

#database config
db = SQLAlchemy(app)

#jwt object

    
from app.auth import routes
from app.workout import routes