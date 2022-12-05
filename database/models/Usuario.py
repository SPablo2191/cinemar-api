import datetime


class Usuario:
    # def __init__(self,nombre,apellido,edad,DNI,correo="",telefono="",fechaRegistro=datetime.datetime.now()):
    #     self._nombre = nombre
    #     self._edad = edad
    #     self._DNI = DNI
    #     self._apellido = apellido
    #     self._correo = correo
    #     self._telefono = telefono
    #     self._fechaRegistro = fechaRegistro
    
    def __str__(self):
        return "Usuario(idTipoUsuario,nombre,apellido,nombreUsuario,DNI,contrasena,correo,telefono,fechaRegistro,fechaNacimiento,estado) values(?,?,?,?,?,?,?,?,?,?,?)"

class TipoUsuario:
    def __str__(self) -> str:
        return "TipoUsuario(idTipoUsuario,nombre) values(?,?)"