import datetime
from .BaseModel import BaseModel
class Funcion(BaseModel):
    def __init__(self,idSala,idPelicula,cantidadButacasDisponibles,fechaFuncion,nombrePelicula,estado=True,fechaRegistro=datetime.datetime.now()):
        self.sala = idSala
        self.pelicula = idPelicula
        self.cantidadButacasDisponibles = cantidadButacasDisponibles
        self.fechaFuncion = fechaFuncion
        self.estado = estado
        self.nombrePelicula = nombrePelicula
        self.fechaRegistro = fechaRegistro

    def __str__(self):
        return 'Funcion(idSala, idPelicula,fechaFuncion,fechaRegistro,cantidadButacasDisponible,estado,nombrePelicula) values (?,?,?,?,?,?,?)'