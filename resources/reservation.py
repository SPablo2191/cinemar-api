from flask import Blueprint,jsonify
import datetime
reservations = Blueprint('reservations',__name__)
@reservations.route('/reservations',methods=['GET'])
def get_reservations():
    # return jsonify([])
    return jsonify([
        {'idSala': 1,'nombre':'sala1','cantidadButacas': '10','fechaRegistro':datetime.datetime.now()},
        {'idSala': 2,'nombre':'sala2','cantidadButacas': '20','fechaRegistro':datetime.datetime.now()},
        {'idSala': 3,'nombre':'sala3','cantidadButacas': '30','fechaRegistro':datetime.datetime.now()},
        {'idSala': 4,'nombre':'sala4','cantidadButacas': '40','fechaRegistro':datetime.datetime.now()}])
@reservations.route('/reservations',methods=['POST'])
def add_reservations():
    return jsonify([])
@reservations.route('/reservations',methods=['PUT'])
def update_reservations():
    return jsonify([])
@reservations.route('/reservations',methods=['DELETE'])
def delete_reservations():
    return jsonify([])