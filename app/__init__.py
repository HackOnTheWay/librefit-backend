from flask_jwt_extended import JWTManager,create_access_token, get_jwt_identity
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

#app config
app = Flask(__name__)

app.config.from_object(Config)

#database config
db = SQLAlchemy(app)

#jwt object
jwt = JWTManager(app)
    
from app.auth import routes
