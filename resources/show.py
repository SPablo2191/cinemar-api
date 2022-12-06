from flask import Blueprint, jsonify, request
from database.models.Funcion import Funcion
from resources.home import get_db
shows = Blueprint('shows', __name__)
table = 'Funcion'


@shows.route('/shows', methods=['GET'])
def get_shows():
    aux = get_db().innerJoin(table, 'Sala')
    return jsonify(aux)


@shows.route('/shows/seats/<int:id>', methods=['GET','POST'])
def get_seats_of_show(id):
    # idFuncion = request.args.get('id')
    seatsOfShow = get_db().select('Butaca inner join Sala  on Sala.idSala = Butaca.idSala inner join Funcion on Funcion.idSala = Sala.idSala ','fila,columna,Butaca.nombre',f'where idFuncion={id}')
    seatsAvailable = get_db().select('Butaca inner join DetalleReserva  on Sala.idSala = Butaca.idSala inner join Funcion on Funcion.idSala = Sala.idSala ','fila,columna,Butaca.nombre',f'where idFuncion={id}')
    return jsonify([])
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
