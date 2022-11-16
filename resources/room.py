from flask import Blueprint,jsonify
from database.models.Sala import Sala,TipoSala
import json
import datetime
rooms = Blueprint('rooms',__name__)
sala3D = TipoSala('3-D')

@rooms.route('/rooms',methods=['GET'])
def get_rooms():
    ejemplo = Sala(1,'Sala 1',20,sala3D.__dict__)
    print(ejemplo)
    return jsonify([ejemplo.__dict__])
    
@rooms.route('/rooms',methods=['POST'])
def add_rooms():
    return jsonify([])
@rooms.route('/rooms',methods=['PUT'])
def update_rooms():
    return jsonify([])
@rooms.route('/rooms',methods=['DELETE'])
def delete_rooms():
    return jsonify([])