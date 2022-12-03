from flask import Blueprint,jsonify
from resources.home import get_db

users = Blueprint('users',__name__)
@users.route('/users',methods=['GET'])
def get_users():
    return jsonify(get_db().select('Usuario'))
@users.route('/users',methods=['POST'])
def add_rooms():
    return jsonify([])
@users.route('/users',methods=['PUT'])
def update_rooms():
    return jsonify([])
@users.route('/users',methods=['DELETE'])
def delete_rooms():
    return jsonify([])