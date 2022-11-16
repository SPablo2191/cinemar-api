import datetime
class Funcion:
    def __init__(self,sala,pelicula,horaFuncion,fechaRegistro=datetime.datetime.now()):
        self._sala = sala
        self._pelicula = pelicula
        self._horaFuncion = horaFuncion
        self._fechaRegistro = fechaRegistro

    def __str__(self):
        return {
            "sala" : self._sala,
            "pelicula" : self._pelicula,
            "horaFuncion" : self._horaFuncion,
            "fechaRegistro" : self._fechaRegistro
        }