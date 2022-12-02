import datetime

class Sala:
    def __init__(self,idSala,nombre,cantidadButacas,tipoSala,precio=0,fechaRegistro=datetime.datetime.now()):
        self.idSala = idSala
        self.nombre = nombre
        self.tipoSala = tipoSala
        self.precio = precio
        self.cantidadButacas = cantidadButacas
        self.fechaRegistro = fechaRegistro
    
    def __str__(self):
        return str({
            'idSala': self.idSala,
            'nombre':self.nombre,
            'cantidadButacas': self.cantidadButacas,
            'fechaRegistro': self.fechaRegistro})
class TipoSala:
    def __init__(self,nombre):
        self.nombre = nombre

class Butaca:
    def __init__(self,idButaca : int,idSala :int,fila :int,columna : int,nombre: str,ocupado : bool):
        self.idButaca = idButaca
        self.idSala = idSala
        self.fila = fila
        self.columna = columna
        self.nombre = nombre
        self.ocupado = ocupado