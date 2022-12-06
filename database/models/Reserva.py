from .BaseModel import BaseModel
import datetime


class Reserva(BaseModel):
    def __init__(self, idUsuario, idFuncion, idDescuento, total, estado=True, fechaRegistro=datetime.datetime.now()):
        self.idUsuario = idUsuario
        self.idFuncion = idFuncion
        self.idDescuento = idDescuento
        self.total = total
        self.estado = estado
        self.fechaRegistro = fechaRegistro
    def __str__(self) -> str:
        return 'Reserva (idUsuario,idFuncion,idDescuento,fechaRegistro,total,estado) values (?,?,?,?,?,?)'

class DetalleReserva(BaseModel):
    def __init__(self,idButaca,estado = True):
        self.idButaca = idButaca
        self.estado = estado
    def __str__(self) -> str:
        return 'DetalleReserva (idButaca,estado) values (?,?)'