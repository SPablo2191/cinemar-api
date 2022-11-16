import datetime


class Usuario:
    def __init__(self,nombre,apellido,edad,DNI,correo="",telefono="",fechaRegistro=datetime.datetime.now()):
        self._nombre = nombre
        self._edad = edad
        self._DNI = DNI
        self._apellido = apellido
        self._correo = correo
        self._telefono = telefono
        self._fechaRegistro = fechaRegistro
    
    def __str__(self):
        return {
            "nombre" : self._nombre,
            "edad" : self._edad,
            "DNI" : self._DNI,
            "apellido" : self._apellido,
            "correo" : self._correo,
            "telefono" : self._telefono,
            "fechaRegistro" : self._fechaRegistro
        }