from flask import Blueprint,jsonify
from database.models.Sala import Sala,TipoSala,Butaca

rooms = Blueprint('rooms',__name__)
sala3D = TipoSala('3-D').__dict__
sala2D = TipoSala('2-D').__dict__

salas = [
    Sala(1,'Sala 1',20,sala3D).__dict__,
    Sala(2,'Sala 2',30,sala2D).__dict__,
    Sala(3,'Sala 3',60,sala2D).__dict__,
    Sala(4,'Sala 4',10,sala3D).__dict__,
    ]
butacas = [
    [
        Butaca(1,1,1,1,'Butaca 1-1',True).__dict__,
        Butaca(2,1,1,2,'Butaca 1-2',True).__dict__,
        Butaca(3,1,1,3,'Butaca 1-3',True).__dict__,
        Butaca(4,1,1,4,'Butaca 1-4',True).__dict__,
    ],[
        Butaca(5,1,3,1,'Butaca 2-1',True).__dict__,
        Butaca(6,1,3,2,'Butaca 2-2',True).__dict__,
    ],[
        Butaca(7,1,3,1,'Butaca 3-1',True).__dict__,
        Butaca(8,1,3,2,'Butaca 3-2',False).__dict__,
        Butaca(9,1,3,3,'Butaca 3-3',False).__dict__,
    ]
]

@rooms.route('/rooms',methods=['GET'])
def get_rooms():
    return jsonify(salas)
@rooms.route('/rooms/<int:id>',methods=['GET'])
def get_room(id):
    return jsonify(butacas)
@rooms.route('/rooms',methods=['POST'])
def add_rooms():
    
    return jsonify([])
@rooms.route('/rooms',methods=['PUT'])
def update_rooms():
    return jsonify([])
@rooms.route('/rooms',methods=['DELETE'])
def delete_rooms():
    return jsonify([])