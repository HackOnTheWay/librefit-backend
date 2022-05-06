from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

from flask_jwt_extended import JWTManager

#app config
app = Flask(__name__)

app.config.from_object(Config)

#database config
db = SQLAlchemy(app)

#jwt object
# jwt = JWTManager(app)
    
from app.auth import routes
from app.workout import routes
from app.awards import routes