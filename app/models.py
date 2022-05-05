from enum import unique
from app import db

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    user_name = db.Column(db.String(20), unique=True, nullable=False)
    user_pass = db.Column(db.String(20), unique=True, nullable=False)
    email_id = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return self.user_name

class Awards(db.Model):
    award_id = db.Column(db.Integer, primary_key=True) 
    award_name = db.Column(db.String(20), unique=True) 

class Userawards(db.Model):
    user_id = db.Column(db.Integer, foreign_key=True, primary_key=True)
    award_id = db.Column(db.Integer, foreign_key=True)
        
class Workouts(db.Model):
    w_id = db.Column(db.Integer, primary_key=True)
    w_name = db.Column(db.String(20), unique=True)

    def __repr__(self):
        return self.w_name

class Workoutuser(db.Model):
    user_id = db.Column(db.Integer, foreign_key=True, primary_key=True)
    w_id = db.Column(db.Integer, foreign_key=True)
    duration = db.Column(db.Integer)
    