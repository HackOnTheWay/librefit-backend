from app import app
from app.models import Users
from app import db

from flask_jwt_extended import JWTManager,create_access_token, get_jwt_identity,jwt_required

from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash


jwt = JWTManager(app)

@app.route('/api/auth/login', methods = ['POST'])
def login():
    user_name='amar'
    user_pass='38y2y'
    user = Users.query.filter_by(user_name=user_name,user_pass=user_pass).first()
    access_token = create_access_token(identity=user.user_id)
    return jsonify({ "token": access_token, "user_name": user.user_name})

@app.route('/api/auth/register', methods = ['POST'])
def register():
    data = request.get_json()
    user_name = data['user_name']
    user_pass = generate_password_hash(data['user_pass'])
    email_id = data['email_id']
    user = Users(user_name=user_name,user_pass=user_pass,email_id=email_id)
    db.session.add(user)
    db.session.commit()
    return jsonify({'msg': 'Register route'})

@app.route('/api/auth/forgot_pass', methods = ['POST'])
def forgot_password():
    return jsonify({'msg': 'forgot pass'})