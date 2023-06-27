from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

api = Blueprint('api_auth', __name__)

@api.route('/login', methods=['POST'])
def login():
    
    username = request.json.get('username')
    password = request.json.get('password')
    
    if not username: return jsonify({ "username": "Username is required!"}), 400
    if not password: return jsonify({ "password": "Password is required!"}), 400
    
    userFound = User.query.filter_by(username=username).first()
    
    if not userFound: return jsonify({ "message": "username/password is incorrect"}), 401
    
    if not check_password_hash(userFound.password, password):
        return jsonify({ "message": "username/password is incorrect"}), 401
    
    acces_token = create_access_token(identity=userFound["id"])
    
    data = {
        "access_token": acces_token,
        "user": userFound.serialize()
    }
    
    return jsonify(data), 200
    
    
@api.route('/register', methods=['POST'])
def register():
    # code to register users
    pass