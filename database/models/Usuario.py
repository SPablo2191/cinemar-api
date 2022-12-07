import datetime
from .BaseModel import BaseModel

class Usuario(BaseModel):
    def __init__(self,nombre,apellido,nombreUsuario,contrasena,DNI,correo,telefono,fechaNacimiento,fechaRegistro=datetime.datetime.now(),idTipoUsuario=2,estado=True):
        self.idTipoUsuario = idTipoUsuario
        self.nombre = nombre
        self.apellido = apellido
        self.nombreUsuario = nombreUsuario
        self.DNI = DNI
        self.contrasena = contrasena
        self.correo = correo
        self.telefono = telefono
        self.fechaNacimiento = fechaNacimiento
        self.fechaRegistro = fechaRegistro
        self.estado = estado
    
    def __str__(self):
        return "Usuario(idTipoUsuario,nombre,apellido,nombreUsuario,DNI,contrasena,correo,telefono,fechaRegistro,fechaNacimiento,estado) values(?,?,?,?,?,?,?,?,?,?,?)"

class TipoUsuario:
    def __str__(self) -> str:
        return "TipoUsuario(idTipoUsuario,nombre) values(?,?)"