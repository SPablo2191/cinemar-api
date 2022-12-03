from flask import Blueprint,jsonify
from resources.home import get_db
reservations = Blueprint('reservations',__name__)
@reservations.route('/reservations',methods=['GET'])
def get_reservations():
    aux = get_db().select('Reserva')
    print(type(aux))
    print({}.fromkeys(aux, "set"))
    return jsonify(get_db().select('Reserva'))

@reservations.route('/reservations',methods=['POST'])
def add_reservations():
    return jsonify([])

@reservations.route('/reservations',methods=['PUT'])
def update_reservations():
    return jsonify([])

@reservations.route('/reservations',methods=['DELETE'])
def delete_reservations():
    return jsonify([])