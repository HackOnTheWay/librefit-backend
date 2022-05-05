from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    user_pass = db.Column(db.String(20), unique=True, nullable=False)
    email_id = db.Column(db.String(20), unique=True, nullable=False)
  