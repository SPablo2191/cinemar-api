from flask import Blueprint,jsonify
from database.models.Sala import Sala,TipoSala
rooms = Blueprint('rooms',__name__)
sala3D = TipoSala('3-D').__dict__
sala2D = TipoSala('2-D').__dict__

salas = [
    Sala(1,'Sala 1',20,sala3D).__dict__,
    Sala(2,'Sala 2',30,sala2D).__dict__,
    Sala(3,'Sala 3',60,sala2D).__dict__,
    Sala(4,'Sala 4',10,sala3D).__dict__,
    ]

@rooms.route('/rooms',methods=['GET'])
def get_rooms():
    return jsonify(salas)

@rooms.route('/rooms',methods=['POST'])
def add_rooms():
    
    return jsonify([])
@rooms.route('/rooms',methods=['PUT'])
def update_rooms():
    return jsonify([])
@rooms.route('/rooms',methods=['DELETE'])
def delete_rooms():
    return jsonify([])