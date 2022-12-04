
import datetime
import sqlite3 as sql
# from models.Usuario import Usuario,TipoUsuario
# from models.Sala import TipoSala
class db():
    def __init__(self, db):
        self.connection = sql.connect(db)
        self.cursor = self.connection.cursor()

    def query(self, query):
        """
            execute the query in sqlite database
        """
        self.cursor.execute(query)

    def commit(self):
        """
            confirm the query operation
        """
        self.connection.commit()

    def close(self):
        self.connection.close()

    def Multiquery(self, query, values):
        self.cursor.executemany(query, values)


class dbQuery(db):
    def select(self, table,condition=''):
        self.query(f"select * from {table} {condition};")
        return self.cursor.fetchall()
    def getLastId(self,table):
        self.query(f"select id{table} from {table} order by id{table} DESC limit 1;")
        return self.cursor.fetchall()[0][0]
    def insert(self, table, values):
        self.Multiquery(f"insert into {table}", values)
        self.commit()



# # create the sqlite database 
# bdd = dbQuery('database\database.db')
# # create tables 
# bdd.query("CREATE TABLE IF NOT EXISTS Usuario(idUsuario INTEGER PRIMARY KEY AUTOINCREMENT,idTipoUsuario INTEGER,nombre VARCHAR(40),apellido VARCHAR(40),nombreUsuario VARCHAR(60),DNI VARCHAR(10),contrasena VARCHAR(20),correo VARCHAR(40),telefono VARCHAR(40),fechaRegistro DATE,fechaNacimiento DATE)")
# bdd.query("CREATE TABLE IF NOT EXISTS Reserva(idReserva INTEGER PRIMARY KEY AUTOINCREMENT, idUsuario INTEGER,idFuncion INTEGER,idDescuento INTEGER,fechaRegistro DATE,total REAL,FOREIGN KEY(idUsuario) REFERENCES Usuario(idUsuario),FOREIGN KEY(idFuncion) REFERENCES Funcion(idFuncion),FOREIGN KEY(idDescuento) REFERENCES Descuento(idDescuento))")
# bdd.query("CREATE TABLE IF NOT EXISTS Descuento(idDescuento INTEGER PRIMARY KEY AUTOINCREMENT, dia TEXT,porcentaje REAL)")
# bdd.query("CREATE TABLE IF NOT EXISTS Funcion(idFuncion INTEGER PRIMARY KEY AUTOINCREMENT,idSala INTEGER, idPelicula INTEGER,fechaFuncion DATE,fechaRegistro DATE,cantidadButacasDisponible INTEGER,FOREIGN KEY(idPelicula) REFERENCES Pelicula(idPelicula),FOREIGN KEY(idSala) REFERENCES Sala(idSala))")
# bdd.query("CREATE TABLE IF NOT EXISTS Sala(idSala INTEGER PRIMARY KEY AUTOINCREMENT,idTipoSala INTEGER,nombre TEXT ,fechaRegistro DATE,cantidadButacas INTEGER,precio REAL,FOREIGN KEY(idTipoSala) REFERENCES TipoSala(idTipoSala))")
# bdd.query("CREATE TABLE IF NOT EXISTS TipoSala(idTipoSala INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT ,valor REAL)")
# bdd.query("CREATE TABLE IF NOT EXISTS TipoUsuario(idTipoUsuario INTEGER PRIMARY KEY AUTOINCREMENT,nombre TEXT)")
# bdd.query("CREATE TABLE IF NOT EXISTS Butaca(idButaca INTEGER PRIMARY KEY AUTOINCREMENT,idSala INTEGER,fila INTEGER,columna INTEGER,nombre TEXT,FOREIGN KEY(idSala) REFERENCES Sala(idSala))")
# bdd.query("CREATE TABLE IF NOT EXISTS DetalleReserva(idDetalleReserva INTEGER PRIMARY KEY AUTOINCREMENT,idButaca INTEGER,FOREIGN KEY(idButaca) REFERENCES Butaca(idButaca))")
# ts =TipoSala()
# bdd.insert(ts,[(1,'Sala-3D',300),(2,'Sala-2D',200)])
# u1 = Usuario()
# u = TipoUsuario()
# bdd.insert(u,[(1,'Administrador')])
# print(datetime.datetime.now())
# bdd.insert(u1,[(1,1,'pablo', 'sandoval','admin', '43168585','123','ejemplo@gmail.com', '4210132',datetime.datetime.now(),datetime.datetime.now())])
# bdd.commit()
# bdd.close()
