import datetime
class Funcion:
    def __init__(self,sala,pelicula,cantidadButacasDisponibles,fechaFuncion=datetime.datetime.now(),fechaRegistro=datetime.datetime.now()):
        self.sala = sala
        self.pelicula = pelicula
        self.fechaFuncion = fechaFuncion
        self.fechaRegistro = fechaRegistro
        self.cantidadButacasDisponibles = cantidadButacasDisponibles

    def __str__(self):
        return {
            "sala" : self._sala,
            "pelicula" : self._pelicula,
            "horaFuncion" : self._horaFuncion,
            "fechaRegistro" : self._fechaRegistro
        }