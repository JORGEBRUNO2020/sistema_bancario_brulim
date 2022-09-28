import sqlite3


#------------CREAR LA BBDD---------------
# conexion = sqlite3.connect('sistema_brulim.db')
# conexion.close()
#-----------------------------------------

#------------CARGAR TABLAS---------------

# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()

# cursor.execute('CREATE TABLE moneda ( id SERIAL NOT NULL ,    nombre varchar(25) NOT NULL,    pais varchar(15) NOT NULL,    precio_compra decimal(10,2) NOT NULL,    precio_venta decimal(10,2) NOT NULL,    CONSTRAINT moneda_pk PRIMARY KEY (id))')

# conexion.commit()
# conexion.close()
#-----------------------------------------
# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()

# cursor.execute('CREATE TABLE sucursal (id SERIAL NOT NULL, ciudad varchar(30) NOT NULL,    direccion varchar(45) NOT NULL, CONSTRAINT sucursal_pk PRIMARY KEY (id))')

# conexion.commit()
# conexion.close()
#-----------------------------------------

# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()

# cursor.execute('CREATE TABLE tipo_cuenta (    id SERIAL NOT NULL ,    nombre varchar(30) NOT NULL,    CONSTRAINT tipo_cuenta_pk PRIMARY KEY (id))')

# conexion.commit()
# conexion.close()

#-----------------------------------
# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()

# cursor.execute('CREATE TABLE tipo_usuario (    id SERIAL NOT NULL ,    usuario_tipo varchar(30) NOT NULL,    CONSTRAINT tipo_usuario_pk PRIMARY KEY (id))')

# conexion.commit()
# conexion.close()

#-----------------------------------
# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()

# cursor.execute('CREATE TABLE usuario (    id SERIAL NOT NULL ,    estado boolean NOT NULL,    tipo_usuario_id int NOT NULL,    CONSTRAINT usuario_pk PRIMARY KEY (id))')

# conexion.commit()
# conexion.close()

#-----------------------------------
# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()

# cursor.execute('CREATE TABLE cuenta (    numero_cuenta SERIAL NOT NULL ,    cbu varchar(10) NOT NULL,    saldo decimal(14,2) NOT NULL,    sucursal_id int NOT NULL,    tipo_cuenta_id int NOT NULL,    usuario_id int NOT NULL,    CONSTRAINT cuenta_pk PRIMARY KEY (numero_cuenta))')

# conexion.commit()
# conexion.close()

#-----------------------------------
# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()

# cursor.execute('CREATE TABLE datos_cuenta (    cuenta_numero_cuenta int NOT NULL,    fecha_apertura date NOT NULL,    estado boolean NOT NULL,    CONSTRAINT datos_cuenta_pk PRIMARY KEY (cuenta_numero_cuenta))')

# conexion.commit()
# conexion.close()

#-----------------------------------
# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()

# cursor.execute('CREATE TABLE datos_usuario (    cuil_cuit int NOT NULL,    dni varchar(8) NULL,    nombre varchar(45) NULL,    apellido varchar(40) NULL,    razon_social varchar(45) NULL,    telefono varchar(20) NOT NULL,    email varchar(60) NOT NULL,    usuario_id int NOT NULL,    CONSTRAINT datos_usuario_pk PRIMARY KEY (cuil_cuit))')

# conexion.commit()
# conexion.close()

#-----------------------------------
# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()

# cursor.execute('CREATE TABLE login (    nombre_usuario varchar(40) NOT NULL,    password varchar(25) NOT NULL,    usuario_id int NOT NULL,    CONSTRAINT login_pk PRIMARY KEY (nombre_usuario))')

# conexion.commit()
# conexion.close()

#-----------------------------------
# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()

# cursor.execute('CREATE TABLE movimiento_comision (    id SERIAL NOT NULL ,    nombre_comision varchar(40) NOT NULL,    costo_comision decimal(6,2) NOT NULL,    CONSTRAINT movimiento_comision_pk PRIMARY KEY (id))')

# conexion.commit()
# conexion.close()

#-----------------------------------
# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()

# cursor.execute('CREATE TABLE transaccion (    id SERIAL NOT NULL ,    monto float(14,2) NOT NULL,    fecha_movimiento date NOT NULL,    cuenta_numero_cuenta int NOT NULL,    comision_id int NOT NULL,    moneda_id int NOT NULL,    CONSTRAINT transaccion_pk PRIMARY KEY (id))')

# conexion.commit()
# conexion.close()

#-----------------------------------

#-------------------------------------
#-------------INSERT-UN ELEMENTO------------------

# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()
# cursor.execute('INSERT INTO MONEDA VALUES (4, "REAL", "BRASIL", 70, 80)')

# conexion.commit()

# conexion.close()
#-------------------------------------

#-------------INSERT-MUCHOS ELEMENTOS------------------

# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()
# monedas = [(2, 'PESO', 'ARGENTINA', 0, 0),(3, 'REAL', 'BRASIL', 70, 80)]

# cursor.executemany('INSERT INTO MONEDA VALUES (?,?,?,?,?)', monedas)

# conexion.commit()

# conexion.close()
#-------------------------------------

# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()
# sucursales = [(1,'TANDIL', 'MARCONI 1450'),
# (2,'TANDIL','RIVADAVIA 235'),
# (3,'BALCARCE', 'FANGIO 541'),
# (4,'AYACUCHO', 'SOLANET 652'),
# (5,'RAUCH', 'PAZ 52'),
# (6,'TANDIL', '9 DE JULIO 784')]

# cursor.executemany('INSERT INTO SUCURSAL VALUES (?,?,?)', sucursales)

# conexion.commit()

# conexion.close()
#-------------------------------------

# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()
# tipos_de_cuentas = [(1, 'CAJA AHORRO COMUN'),(2, 'CAJA AHORRO SR'),(3, 'CUENTA CORRIENTE COMUN'),(4, 'CUENTA CORRIENTE SR')]

# cursor.executemany('INSERT INTO TIPO_CUENTA VALUES (?,?)', tipos_de_cuentas)

# conexion.commit()

# conexion.close()
#-------------------------------------

# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()
# tipo_usuarios = [(1, 'ADMINISTRADOR'), (2, 'INDIVIDUO'), (3, 'PYME'), (4, 'EMPLEADO')]

# cursor.executemany('INSERT INTO TIPO_USUARIO VALUES (?,?)', tipo_usuarios)

# conexion.commit()

# conexion.close()
#-------------------------------------

# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()
# usuarios = [(1,True, 1),
# (2,True, 3),
# (3,False, 2),
# (4,True, 1),
# (5,True, 1),
# (6,True, 2),
# (7,True, 4),
# (8,True, 3),
# (9,False, 3) ]

# cursor.executemany('INSERT INTO USUARIO VALUES (?,?,?)', usuarios)

# conexion.commit()

# conexion.close()
#-------------------------------------

# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()
# cuentas = [(1,'985698569', 200, 1,1,1),
# (2,'325632563', 1400, 4, 2,  2),
# (3,'214521452', 62000, 2, 4,  7),
# (4,'258741258', 2300, 3, 2,  4)]

# cursor.executemany('INSERT INTO CUENTA VALUES (?,?,?,?,?,?)', cuentas)

# conexion.commit()

# conexion.close()
#-------------------------------------

# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()
# login = [('USUARIO 1', 'PASS 1', 1),
# ('USUARIO 2', 'PASS 2', 2),
# ('USUARIO 3', 'PASS 3', 3),
# ('USUARIO 4', 'PASS 4', 4)]

# cursor.executemany('INSERT INTO LOGIN VALUES (?,?,?)', login)

# conexion.commit()

# conexion.close()
#-------------------------------------

# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()
# datos_usuarios = [(2025412547, '23456789', 'PEPE', 'ARGENTO', '', '55587484', '' ,1),
# (2356854785, '21458745', 'ARTURO', 'BUENO', '', '65478969', '', 2),
# (2789655856, '27845888', 'MARIA', 'ANTONIETA', '', '55587458', 'mantonieta@gmail.com', 3)]

# cursor.executemany('INSERT INTO DATOS_USUARIO VALUES (?,?,?,?,?,?,?,?)', datos_usuarios)

# conexion.commit()

# conexion.close()
#-------------------------------------

#-----------------------------------

#-------------SELECT- UN ELEMENTO----------------

# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()
# cursor.execute('SELECT * FROM MONEDA')

# usuario = cursor.fetchone()
# print(usuario)

# conexion.close()

#-------------------------------------

#-------------------------------------

#-------------SELECT- TODOS LOS ELEMENTOS DE UNA TABLA----------------

# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()
# cursor.execute('SELECT * FROM MONEDA')

# usuario = cursor.fetchall()
# for u in usuario:
#     print(u)

# conexion.close()

#-------------------------------------

# conexion = sqlite3.connect('sistema_brulim.db')

# cursor = conexion.cursor()
# cursor.execute('SELECT * FROM DATOS_USUARIO')

# usuario = cursor.fetchall() # MUESTRA TODOS LOS CAMPOS DE CADA LINEA
# for u in usuario:
#     print(u)

# usuario1 = cursor.fetchall() # MUESTRA EL CAMPO 3 DE CADA LINEA
# for u in usuario1:
#     print(u[3])

# usuario2 = cursor.fetchall() # MUESTRA EL CAMPO 3 Y EL 5 DE CADA LINEA
# for u in usuario2:
#     print("APELLIDO",u[3],"\t", "TELEFONO", u[5])

# conexion.close()