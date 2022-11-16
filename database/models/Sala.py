import datetime

class Sala:
    def __init__(self,idSala,nombre,cantidadButacas,tipoSala,fechaRegistro=datetime.datetime.now()):
        self.idSala = idSala
        self.nombre = nombre
        self.tipoSala = tipoSala
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