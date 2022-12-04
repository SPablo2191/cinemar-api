from flask import Blueprint, jsonify, request, Response
from flask_jwt_extended import create_access_token
from resources.home import get_db
import datetime
table = 'Usuario'
users = Blueprint('users', __name__)


@users.route('/users', methods=['GET'])
def get_users():
    return jsonify(get_db().select(table))


@users.route('/users', methods=['POST'])
def auth():
    data = dict(request.get_json())
    condition = f"where nombreUsuario LIKE'{data['nombreUsuario']}' AND contrasena LIKE '{data['contrasena']}'"
    rows = get_db().select(table, condition)
    if rows == []:
        return {'error': 'username or password invalid'}, 401
    expires = datetime.timedelta(minutes=2)
    access_token = create_access_token(
        identity=data['nombreUsuario'], expires_delta=expires)
    return {'token': access_token}, 200


# @users.route('/users', methods=['PUT'])
# def update_users():
#     return jsonify([])


# @users.route('/users', methods=['DELETE'])
# def delete_users():
#     return jsonify([])
