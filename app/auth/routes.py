from app import app
from app.models import Users
from app import db

from app import jwt

from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash

@app.route('/api/auth/login', methods = ['POST'])
def login():
    # user_id=1
    # user_name = 'amar'
    # user_pass='hello'
    # email_id ='test@gmail.com'
    # user = Users(user_id=user_id,user_name=user_name,user_pass=user_pass,email_id=email_id)
    # db.session.add(user)
    # db.session.commit()
    if Users is None:
        # the user was not found on the database
        return jsonify({"msg": "Bad username or password"}), 401
    
    # create a new token with the user id inside
    access_token = jwt.create_access_token(identity=Users.id)
    return jsonify({ "token": access_token, "user_id": Users.id })

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