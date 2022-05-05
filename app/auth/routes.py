from app import app
from app.models import Users
from app import db

#date time
from datetime import timedelta
from datetime import timezone
from datetime import datetime



from flask_jwt_extended import JWTManager,create_access_token, get_jwt_identity,jwt_required
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies
from flask_jwt_extended import get_jwt

from flask import jsonify,request
from werkzeug.security import generate_password_hash,check_password_hash

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)
jwt = JWTManager(app)


#refreshing token implementation
@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(seconds=10))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        return response


@app.route('/api/auth/login', methods = ['POST'])
def login():
    user_name='amar'
    user_pass='38y2y'
    user = Users.query.filter_by(user_name=user_name,user_pass=user_pass).first()
    access_token = create_access_token(identity=user.user_id)
    response = jsonify({"msg": "login successful"})
    set_access_cookies(response, access_token)
    return jsonify({ "token": access_token, "user_name": user.user_name , "msg": "login successful"})

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


@app.route("/api/auth/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "logout successful"})
    unset_jwt_cookies(response)
    return response


@app.route("/api/auth/protected", methods = ["GET"])
@jwt_required()
def protected():
    return jsonify({"msg": "token expired"})

