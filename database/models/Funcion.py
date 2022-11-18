import datetime
class Funcion:
    def __init__(self,sala,pelicula,horaFuncion=str(datetime.datetime.now().time()),fechaRegistro=datetime.datetime.now()):
        self.sala = sala
        self.pelicula = pelicula
        self.horaFuncion = horaFuncion
        self.fechaRegistro = fechaRegistro

    def __str__(self):
        return {
            "sala" : self._sala,
            "pelicula" : self._pelicula,
            "horaFuncion" : self._horaFuncion,
            "fechaRegistro" : self._fechaRegistro
        }