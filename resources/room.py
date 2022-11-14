from flask import Blueprint,jsonify
rooms = Blueprint('rooms',__name__)
@rooms.route('/rooms',methods=['GET'])
def get_rooms():
    return jsonify([])
@rooms.route('/rooms',methods=['POST'])
def add_rooms():
    return jsonify([])
@rooms.route('/rooms',methods=['PUT'])
def update_rooms():
    return jsonify([])
@rooms.route('/rooms',methods=['DELETE'])
def delete_rooms():
    return jsonify([])