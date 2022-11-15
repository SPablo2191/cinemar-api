from flask import Blueprint,jsonify
import datetime
rooms = Blueprint('rooms',__name__)
@rooms.route('/rooms',methods=['GET'])
def get_rooms():
    return jsonify([])
    # return jsonify([
    #     {'idSala': 1,'nombre':'sala1','cantidadButacas': '10','fechaRegistro':datetime.datetime.now()},
    #     {'idSala': 2,'nombre':'sala2','cantidadButacas': '20','fechaRegistro':datetime.datetime.now()},
    #     {'idSala': 3,'nombre':'sala3','cantidadButacas': '30','fechaRegistro':datetime.datetime.now()},
    #     {'idSala': 4,'nombre':'sala4','cantidadButacas': '40','fechaRegistro':datetime.datetime.now()}])
@rooms.route('/rooms',methods=['POST'])
def add_rooms():
    return jsonify([])
@rooms.route('/rooms',methods=['PUT'])
def update_rooms():
    return jsonify([])
@rooms.route('/rooms',methods=['DELETE'])
def delete_rooms():
    return jsonify([])