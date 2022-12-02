# cinemar-api🎦
Proyecto Cinemar API - Mil Programadores Python 2022
# Drive🐱‍🏍:
- Link: https://drive.google.com/drive/folders/1RniGTnwd7dSyqFlN-fCgnRz-NIwaH31Z?usp=sharing

# FrontEnd🐱‍🚀:
- Link: https://github.com/SPablo2191/CinemarWeb

## Routes👣:
- /movies 
    - GET => obtiene las ultimas peliculas tomando datos de The movieDatabaseAPI
- /movies/id
    - GET => obtiene una descripción completo de una pelicula especificada por su ID

## SQLITE
### Usuario
CREATE TABLE IF NOT EXISTS Usuario(idUsuario INTEGER PRIMARY KEY,idTipoUsuario INTEGER,nombre VARCHAR(40),apellido VARCHAR(40),nombreUsuario VARCHAR(60),DNI VARCHAR(10),contrasena VARCHAR(20),correo VARCHAR(40),telefono VARCHAR(40),fechaRegistro DATE,FOREIGN KEY(idTipoUsuario) REFERENCES TipoUsuario(idTipoUsuario))

### Reserva
CREATE TABLE IF NOT EXISTS Reserva(idReserva INTEGER PRIMARY KEY, idUsuario INTEGER,idFuncion INTEGER,idDescuento INTEGER,fechaRegistro DATE,total REAL,FOREIGN KEY(idUsuario) REFERENCES Usuario(idUsuario),FOREIGN KEY(idFuncion) REFERENCES Funcion(idFuncion),FOREIGN KEY(idDescuento) REFERENCES Descuento(idDescuento))

### Descuento
CREATE TABLE IF NOT EXISTS Descuento(idDescuento INTEGER PRIMARY KEY, dia TEXT,porcentaje REAL)

### Funcion
CREATE TABLE IF NOT EXISTS Funcion(idFuncion INTEGER PRIMARY KEY,idSala INTEGER, idPelicula INTEGER,fechaFuncion DATE,fechaRegistro DATE,cantidadButacasDisponible INTEGER,FOREIGN KEY(idPelicula) REFERENCES Pelicula(idPelicula),FOREIGN KEY(idSala) REFERENCES Sala(idSala))

### Sala
CREATE TABLE IF NOT EXISTS Sala(idSala INTEGER PRIMARY KEY,idTipoSala INTEGER,nombre TEXT ,fechaRegistro DATE,cantidadButacas INTEGER,precio REAL,FOREIGN KEY(idTipoSala) REFERENCES TipoSala(idTipoSala))

### TipoSala
CREATE TABLE IF NOT EXISTS TipoSala(idTipoSala INTEGER PRIMARY KEY,nombre TEXT ,valor REAL)
### TipoUsuario
CREATE TABLE IF NOT EXISTS TipoUsuario(idTipoUsuario INTEGER PRIMARY KEY,nombre TEXT)

### Butaca
CREATE TABLE IF NOT EXISTS Butaca(idButaca INTEGER PRIMARY KEY,idSala INTEGER,fila INTEGER,columna INTEGER,nombre TEXT,FOREIGN KEY(idSala) REFERENCES Sala(idSala))

### DetalleReserva
CREATE TABLE IF NOT EXISTS DetalleReserva(idDetalleReserva INTEGER PRIMARY KEY,idButaca INTEGER,FOREIGN KEY(idButaca) REFERENCES Butaca(idButaca))
