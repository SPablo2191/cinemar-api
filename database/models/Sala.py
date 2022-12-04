import datetime

from .BaseModel import BaseModel

class Sala(BaseModel):
    def __init__(self,nombre,cantidadButacas,precio=0,fechaRegistro=datetime.datetime.now()):
        self.nombre = nombre
        self.precio = precio
        self.cantidadButacas = cantidadButacas
        self.fechaRegistro = fechaRegistro
    
    def __str__(self):
        return 'Sala(idTipoSala,nombre,fechaRegistro,cantidadButacas,precio) values (?,?,?,?,?)'
class TipoSala:
    # def __init__(self,nombre):
    #     self.nombre = nombre
    def __str__(self) -> str:
        return 'TipoSala(idTipoSala,nombre,valor) values (?,?,?)'

class Butaca(BaseModel):
    def __init__(self,idSala :int,fila :int,columna : int,nombre: str):
        self.idSala = idSala
        self.fila = fila
        self.columna = columna
        self.nombre = nombre

    def __str__(self) -> str:
        return 'Butaca(idSala,fila,columna,nombre) values (?,?,?,?)'