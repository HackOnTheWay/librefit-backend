from app import app
from app.models import Users
from app import db


# date time
from datetime import timedelta
from datetime import timezone
from datetime import datetime


from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required, create_refresh_token
from flask_jwt_extended import set_access_cookies
from flask_jwt_extended import unset_jwt_cookies
from flask_jwt_extended import get_jwt
from flask_jwt_extended import get_current_user
from flask_jwt_extended import current_user


from flask import jsonify, request

from werkzeug.security import generate_password_hash, check_password_hash

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)
jwt = JWTManager(app)


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return Users.query.filter_by(user_id=identity).one_or_none()

# refreshing token implementation


@app.after_request
def refresh_expiring_jwts(response):
    try:
        exp_timestamp = get_jwt()["exp"]
        now = datetime.now(timezone.utc)
        target_timestamp = datetime.timestamp(now + timedelta(minutes=3))
        if target_timestamp > exp_timestamp:
            access_token = create_access_token(identity=get_jwt_identity())
            set_access_cookies(response, access_token)
        return response
    except (RuntimeError, KeyError):
        return response


@app.route('/api/auth/login', methods=['POST'])
def login():

    data = request.get_json()

    user_name = data['user_name']
    if user_name:
        if '@' in user_name:
            user = Users.query.filter_by(email_id=user_name).first()
        else:
            user = Users.query.filter_by(user_name=user_name).first()

        if user is None:
            return jsonify({'message': 'User not found'}), 401

        user_pass = data['user_pass']

        if check_password_hash(user.user_pass, user_pass):
            access_token = create_access_token(identity=user.user_id)
            refresh_token = create_refresh_token(identity=user.user_id)
            response = jsonify({"msg": "login successful"})
            set_access_cookies(response, access_token)
            return jsonify({"access-token": access_token, "refresh-token": refresh_token})
        else:
            return jsonify({'message': 'Incorrect Password'}), 401
    else:
        return jsonify({'message': 'Username not provided'}), 401


@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    user_name = data['user_name']

    user_name_exists = Users.query.filter_by(user_name=user_name).first()

    if user_name_exists is not None:
        return jsonify({'message': 'Username already exists'}), 401

    email_id = data['email_id']

    email_id_exists = Users.query.filter_by(email_id=email_id).first()

    if email_id_exists is not None:
        return jsonify({'message': 'Email already exists'}), 401

    user_pass = data['user_pass']

    if user_name is None or user_pass is None or email_id is None:
        return jsonify({'message': 'fields cannot be empty'}), 401
    user_pass = generate_password_hash(data['user_pass'])
    user = Users(user_name=user_name, user_pass=user_pass, email_id=email_id)
    db.session.add(user)
    db.session.commit()
    return jsonify({'msg': 'Register route'})


@app.route('/api/auth/forgot_pass', methods=['POST'])
def forgot_password():
    return jsonify({'msg': 'forgot pass'})


@app.route("/api/auth/logout", methods=["POST"])
@jwt_required()
def logout():
    response = jsonify({"msg": "logout successful"})
    user = Users.query.filter_by(user_id=current_user.user_id).first()
    if current_user.last_seen is None:
        user.last_seen = datetime.now()
        db.session.commit()
    else:
        frequency = datetime.now - user.last_seen
        if frequency == 1:
            streak += 1
            user = Users(streak=streak)
            db.session.add(user)
            db.session.commit()
    unset_jwt_cookies(response)
    return response


@app.route("/api/auth/protected", methods=["GET"])
@jwt_required()
def protected():
    return jsonify({"msg": "token expired"})


@app.route("/api/auth/get_username", methods=['GET'])
def get_username():
    username = Users.query.all()

    user_dict = {str(index): str(usern)
                 for index, usern in enumerate(username, 1)}

    return jsonify(user_dict)


@app.route('/api/get_user', methods=['GET'])
@jwt_required()
def get_user():
    user = Users.query.filter_by(user_id=current_user.user_id).first()

    user_dict = {'user_id': user.user_id,
                 'last_seen': user.last_seen,
                 'profile_pic': user.profile_pic,
                 'email_id': user.email_id,
                 'user_name': user.user_name,
                 'streaks': user.streaks
                 }

    if user is None:
        return jsonify({'message': 'User does not exist'}), 401
    return jsonify(user_dict)
