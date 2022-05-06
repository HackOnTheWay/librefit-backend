from app import app, awards

from app import db
from app.models import Users,Userawards
from flask import jsonify, request

from flask_jwt_extended import get_current_user, jwt_required, JWTManager
from flask_jwt_extended import current_user

jwt = JWTManager(app)
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return Users.query.filter_by(user_id=identity).one_or_none()


@app.route('/api/awards/send_award')
@jwt_required()
def send_award():

    if current_user.streaks == 7:
        award_name = 'consistent'
        award_id = awards.query.filter_by(award_name=award_name).first()
        award_user = Userawards(user_id=current_user.user_id, award_id=award_id)
        db.session.add(award_user)
        db.session.commit()
    return jsonify({ "message" : 'user badge awarded' })