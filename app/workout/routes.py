from app import db
from app import app


from flask import jsonify, request

from flask_jwt_extended import get_current_user, jwt_required, JWTManager
from flask_jwt_extended import current_user

from app.models import Users, Workoutuser,Workouts


jwt = JWTManager(app)

@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return Users.query.filter_by(user_id=identity).one_or_none()


@app.route('/api/workout/get_workouts', methods=['GET'], endpoint='get_workouts')
@jwt_required()
def get_workouts():
    workouts = Workouts.query.all()

    workouts_dict = {str(workout_id): str(workout_name)
                     for workout_id, workout_name in enumerate(workouts, 1)}

    return jsonify(workouts_dict)


@app.route('/api/workout/end_workout', methods=['POST'])
@jwt_required()
def end_workouts():
    data = request.get_json()

    user = current_user.user_id

    print(user)

    c_user = Users.query.filter_by(user_id=user).first()

    if c_user is None:
        return jsonify({'message': 'User does not exist'}), 401

    workout_id = data['workout_id']
    duration = data['duration']

    workout_user = Workoutuser(
        user_id=user, w_id=workout_id, duration=duration)

    db.session.add(workout_user)
    db.session.commit()

    return jsonify({'message': 'Workout completed'})
