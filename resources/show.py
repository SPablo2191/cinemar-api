from flask import Blueprint,jsonify
shows = Blueprint('shows',__name__)
@shows.route('/shows',methods=['GET'])
def get_shows():
    return jsonify([])
@shows.route('/shows',methods=['POST'])
def add_rooms():
    return jsonify([])
@shows.route('/shows',methods=['PUT'])
def update_rooms():
    return jsonify([])
@shows.route('/shows',methods=['DELETE'])
def delete_rooms():
    return jsonify([])