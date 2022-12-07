from flask import Blueprint, jsonify, request
from database.models.Funcion import Funcion
from resources.home import get_db
shows = Blueprint('shows', __name__)
table = 'Funcion'


@shows.route('/shows', methods=['GET'])
def get_shows():
    aux = get_db().innerJoin(table, 'Sala')
    return jsonify(aux)


@shows.route('/shows/seats', methods=['GET'])
def get_seats_of_show():
    id = request.args.get('id')
    seatsOfRoom = get_db().select('Butaca inner join Sala  on Sala.idSala = Butaca.idSala inner join Funcion on Funcion.idSala = Sala.idSala ','idButaca,fila,columna,Butaca.nombre',f'where idFuncion={id}')
    seatsAvailable = get_db().select('Butaca inner join DetalleReserva  on Butaca.idButaca = DetalleReserva.idButaca inner join Reserva on Reserva.idReserva = DetalleReserva.idReserva inner join Funcion on Reserva.idFuncion = Funcion.idFuncion','Butaca.idButaca',f'where Funcion.idFuncion={id}')
    print(seatsAvailable)
    seatsOfShow  = []
    for item in seatsOfRoom:
        seat = list(item)
        seat.append(True)
        seatsOfShow.append(seat)
    for i in range(len(seatsAvailable)):
        for j in range(len(seatsOfRoom)):
            if(seatsAvailable[i][0] == seatsOfRoom[j][0]):
                seatsOfShow[j][len(seatsOfShow[0])-1]= False
    return {'seats':seatsOfShow,'length':len(seatsOfShow)}
    # return jsonify(get_db().innerJoinDynamic(['Butaca','Sala','Funcion'],'fila,columna,Butaca.nombre',f'where idFuncion={id}'))


@shows.route('/shows', methods=['POST'])
def add_shows():
    data = dict(request.get_json())
    newShow = Funcion(data['sala']['idSala'], data['pelicula']['id'], data['sala']
                      ['cantidadButacas'], data['fechaFuncion'], data['pelicula']['title'])
    tupleNewShow = newShow.__iter__(newShow.sala, newShow.pelicula, newShow.fechaFuncion, newShow.fechaRegistro,
                                    newShow.cantidadButacasDisponibles, newShow.estado, newShow.nombrePelicula)
    get_db().insert(newShow, [tupleNewShow])
    return {'status': 'Show registered succesfully'}, 200


@shows.route('/shows', methods=['PUT'])
def update_shows():
    return jsonify([])


@shows.route('/shows', methods=['DELETE'])
def delete_shows():
    return jsonify([])


def matrix_find(matrix, value):
    if not matrix or not matrix[0]:
        return False

    j = len(matrix) - 1
    for row in matrix:
        while (row[j] > value):
            j = j - 1
            if j == -1:
                return False
        if (row[j] == value):
            return True
    return False