from flask import Blueprint, jsonify, request
from database.models.Sala import Sala, TipoSala, Butaca
from resources.home import get_db
rooms = Blueprint('rooms', __name__)
table = ['Sala', 'tipoSala']


@rooms.route('/rooms', methods=['GET'])
def get_rooms():
    aux = get_db().innerJoin(table[0],table[1])
    print(aux)
    return jsonify(aux)


@rooms.route('/rooms/type', methods=['GET'])
def get_type_rooms():
    return jsonify(get_db().select(table[1]))

@rooms.route('/rooms/seats', methods=['GET'])
def get_seats():
    id = request.args.get('id')
    return jsonify(get_db().innerJoin('Butaca',table[0],'*',f'where Butaca.idSala={id}'))


@rooms.route('/rooms/<int:id>', methods=['GET'])
def get_room(id):
    return jsonify([])


@rooms.route('/rooms', methods=['POST'])
def add_rooms():
    data = dict(request.get_json())
    # get_db().select(table[0],'')
    newRoom = Sala(data['nombre'], data['cantidadButacas'],
                   data['tipoSala']['valor'])
    tupleNewRoom = newRoom.__iter__(data['tipoSala']['idTipoSala'], newRoom.nombre,
                                    newRoom.fechaRegistro, newRoom.cantidadButacas, newRoom.precio)
    get_db().insert(newRoom, [tupleNewRoom])
    idSala = get_db().getLastId(table[0])
    newSeats = []
    for seat in data['butacas']:
        newSeat = Butaca(idSala, seat['fila'], seat['columna'], seat['nombre'])
        tupleNewSeat = newSeat.__iter__(
            newSeat.idSala, newSeat.fila, newSeat.columna, newSeat.nombre)
        newSeats.append(tupleNewSeat)
    get_db().insert(newSeat, newSeats)
    get_db().commit()
    return {'status':'Room registered succesfully'},200


@rooms.route('/rooms', methods=['PUT'])
def update_rooms():
    return jsonify([])


@rooms.route('/rooms', methods=['DELETE'])
def delete_rooms():
    return jsonify([])
# sala3D = TipoSala('3-D').__dict__
# sala2D = TipoSala('2-D').__dict__

# salas = [
#     Sala(1,'Sala 1',20,sala3D).__dict__,
#     Sala(2,'Sala 2',30,sala2D).__dict__,
#     Sala(3,'Sala 3',60,sala2D).__dict__,
#     Sala(4,'Sala 4',10,sala3D).__dict__,
#     ]
# butacas = [
#     [
#         Butaca(1,1,1,1,'Butaca 1-1',True).__dict__,
#         Butaca(2,1,1,2,'Butaca 1-2',True).__dict__,
#         Butaca(3,1,1,3,'Butaca 1-3',True).__dict__,
#         Butaca(4,1,1,4,'Butaca 1-4',True).__dict__,
#     ],[
#         Butaca(5,1,3,1,'Butaca 2-1',True).__dict__,
#         Butaca(6,1,3,2,'Butaca 2-2',True).__dict__,
#     ],[
#         Butaca(7,1,3,1,'Butaca 3-1',True).__dict__,
#         Butaca(8,1,3,2,'Butaca 3-2',False).__dict__,
#         Butaca(9,1,3,3,'Butaca 3-3',False).__dict__,
#     ]
# ]
