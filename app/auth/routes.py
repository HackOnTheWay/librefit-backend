from app import app
from app.models import Users
from app import db

from flask import jsonify

@app.route('/api/auth/login', methods = ['POST'])
def login():
    user_id=1
    user_name = 'amar'
    user_pass='hello'
    email_id ='test@gmail.com'
    user = Users(user_id=user_id,user_name=user_name,user_pass=user_pass,email_id=email_id)
    db.session.add(user)
    db.session.commit()
    return jsonify({'msg': 'Login Route'})   
@app.route('/api/auth/register', methods = ['POST'])
def register():
    return jsonify({'msg': 'Register route'})

@app.route('/api/auth/forgot_pass', methods = ['POST'])
def forgot_password():
    return jsonify({'msg': 'forgot pass'})