from app import db

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    user_pass = db.Column(db.String(20), unique=True, nullable=False)
    email_id = db.Column(db.String(20), unique=True, nullable=False)

class Awards(db.Model):
    award_id = db.Column(db.Integer, primary_key=True) 
    award_name = db.Column(db.String(20), unique=True) 

class Userawards(db.Model):
    user_id = db.Column(db.Integer, foreign_key=True, primary_key=True)
    award_id = db.Column(db.Integer, foreign_key=True)
        