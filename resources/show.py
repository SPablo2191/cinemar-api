from flask import Blueprint,jsonify
from database.models.Funcion import Funcion
from database.models.Sala import Sala, TipoSala
sala3D = TipoSala('3-D').__dict__
funciones = [
    Funcion(Sala(1,'Sala 1',20,sala3D).__dict__,'Wakanda Forever').__dict__
    ]


shows = Blueprint('shows',__name__)
@shows.route('/shows',methods=['GET'])
def get_shows():
    print(funciones)
    return jsonify(funciones)
@shows.route('/shows',methods=['POST'])
def add_rooms():
    return jsonify([])
@shows.route('/shows',methods=['PUT'])
def update_rooms():
    return jsonify([])
@shows.route('/shows',methods=['DELETE'])
def delete_rooms():
    return jsonify([])