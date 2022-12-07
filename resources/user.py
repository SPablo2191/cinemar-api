from flask import Blueprint, jsonify, request, Response
from flask_jwt_extended import create_access_token
from resources.home import get_db
from database.models.Usuario import Usuario
import datetime
table = 'Usuario'
users = Blueprint('users', __name__)


@users.route('/users', methods=['GET'])
def get_users():
    return jsonify(get_db().select(table))


@users.route('/users', methods=['POST'])
def auth():
    data = dict(request.get_json())
    condition = f"where nombreUsuario LIKE '{data['nombreUsuario']}' AND contrasena LIKE '{data['contrasena']}'"
    rows = get_db().select(table, '*', condition)
    
    if rows == []:
        return {'error': 'username or password invalid'}, 401
    expires = datetime.timedelta(minutes=2)
    access_token = create_access_token(
        identity=data['nombreUsuario'], expires_delta=expires)
    return {'token': access_token, 'user': data['nombreUsuario'], 'idUser': rows[0][0], 'idTipoUsuario': rows[0][1]}, 200


@users.route('/users/register', methods=['POST'])
def register():
    data = dict(request.get_json())
    newUser = Usuario(
        nombre=data['nombre'], apellido=data['apellido'], nombreUsuario=data['nombreUsuario'], contrasena=data['contrasena'], correo=data['correo'], DNI=data['DNI'], fechaNacimiento=data['fechaNacimiento'], telefono=data['telefono'])
    newTuple = newUser.__iter__(newUser.idTipoUsuario, newUser.nombre, newUser.apellido, newUser.nombreUsuario, newUser.DNI,
                                newUser.contrasena, newUser.correo, newUser.telefono, newUser.fechaRegistro, newUser.fechaNacimiento, newUser.estado)
    get_db().insert(newUser, [newTuple])
    return {'status': 'User registered succesfully'}, 200
# @users.route('/users', methods=['PUT'])
# def update_users():
#     return jsonify([])


# @users.route('/users', methods=['DELETE'])
# def delete_users():
#     return jsonify([])
