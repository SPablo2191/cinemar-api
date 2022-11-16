from flask import Blueprint,jsonify

reservations = Blueprint('reservations',__name__)
@reservations.route('/reservations',methods=['GET'])
def get_reservations():
    return jsonify([])

@reservations.route('/reservations',methods=['POST'])
def add_reservations():
    return jsonify([])

@reservations.route('/reservations',methods=['PUT'])
def update_reservations():
    return jsonify([])

@reservations.route('/reservations',methods=['DELETE'])
def delete_reservations():
    return jsonify([])