from flask import Blueprint, jsonify, request
from resources.home import get_db
from database.models.Reserva import Reserva,DetalleReserva
reservations = Blueprint('reservations', __name__)
table = ['Reserva', 'DetalleReserva']


@reservations.route('/reservations', methods=['GET'])
def get_reservations():
    id = request.args.get('id')
    rows = get_db().select(table[0],'*',f'where idUsuario={id}')
    return jsonify(get_array_json(rows))


@reservations.route('/reservations', methods=['POST'])
def add_reservations():
    data = dict(request.get_json())
    newReservation = Reserva(idUsuario=data['idUsuario'], idFuncion=data['funcion']
                             ['idFuncion'], idDescuento=data['descuento']['idDescuento'], total=data['total'])
    newTupleReservation = newReservation.__iter__(newReservation.idUsuario,newReservation.idFuncion,newReservation.idDescuento,newReservation.fechaRegistro,newReservation.total,newReservation.estado)
    print(newTupleReservation)
    get_db().insert(newReservation, [newTupleReservation])
    idReservation = get_db().getLastId(table[0])
    newReservedSeats = []
    for seat in data['seats']:
        print(seat['idButaca'])
        newDetail = DetalleReserva(seat['idButaca'])
        newTuple = newDetail.__iter__(idReservation,newDetail.idButaca,newDetail.estado)
        print(newTuple)
        newReservedSeats.append(newTuple)
    get_db().insert(newDetail, newReservedSeats)
    print(get_db().select(table[1]))
    get_db().commit()
    return {'status':'Reservation registered succesfully'},200


@reservations.route('/reservations', methods=['PUT'])
def update_reservations():
    return jsonify([])


@reservations.route('/reservations', methods=['DELETE'])
def delete_reservations():
    return jsonify([])

def get_array_json(rows):
    array = []
    print(rows)
    for row in rows:
        item = Reserva(row[1],row[2],row[3],row[5],bool(row[6]),row[4],row[0]).__dict__
        array.append(item)
    return array