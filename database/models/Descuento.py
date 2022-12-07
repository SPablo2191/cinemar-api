import datetime
from .BaseModel import BaseModel

class Descuento(BaseModel):
    def __init__(self,dia,porcentaje,descripcion,estado=True,idDescuento=0):
        self.idDescuento = idDescuento
        self.dia = dia
        self.porcentaje = porcentaje
        self.descripcion = descripcion
        self.estado = estado
    
    def __str__(self):
        return "Descuento(dia,porcentaje,descripcion,estado) values(?,?,?,?)"
