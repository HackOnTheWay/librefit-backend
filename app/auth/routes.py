from crypt import methods
from app import app

from flask import jsonify

@app.route('/api/auth/login', methods = ['POST'])
def login():
    return jsonify({'msg': 'Login Route'})

@app.route('/api/auth/register', methods = ['POST'])
def register():
    return jsonify({'msg': 'Register route'})

@app.route('/api/auth/forgot_pass', methods = ['POST'])
def forgot_password():
    return jsonify({'msg': 'forgot pass'})