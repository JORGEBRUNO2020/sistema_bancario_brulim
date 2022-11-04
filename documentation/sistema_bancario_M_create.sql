-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-10-25 04:41:15.518

-- tables
-- Table: cuenta
CREATE TABLE cuenta (
    numero_cuenta int NOT NULL AUTO_INCREMENT,
    cbu varchar(10) NOT NULL,
    saldo decimal(14,2) NOT NULL,
    sucursal_id int NOT NULL,
    tipo_cuenta_id int NOT NULL,
    usuario_id int NOT NULL,
    CONSTRAINT cuenta_pk PRIMARY KEY (numero_cuenta)
);

-- Table: datos_cuenta
CREATE TABLE datos_cuenta (
    cuenta_numero_cuenta int NOT NULL,
    fecha_apertura date NOT NULL,
    estado boolean NOT NULL,
    CONSTRAINT datos_cuenta_pk PRIMARY KEY (cuenta_numero_cuenta)
);

-- Table: datos_usuario
CREATE TABLE datos_usuario (
    cuil_cuit int NOT NULL,
    dni varchar(8) NULL,
    nombre varchar(45) NULL,
    apellido varchar(40) NULL,
    razon_social varchar(45) NULL,
    telefono varchar(20) NOT NULL,
    email varchar(60) NOT NULL,
    usuario_id int NOT NULL,
    CONSTRAINT datos_usuario_pk PRIMARY KEY (cuil_cuit)
);

-- Table: login
CREATE TABLE login (
    nombre_usuario varchar(40) NOT NULL,
    password varchar(25) NOT NULL,
    usuario_id int NOT NULL,
    CONSTRAINT login_pk PRIMARY KEY (nombre_usuario)
);

-- Table: moneda
CREATE TABLE moneda (
    id int NOT NULL AUTO_INCREMENT,
    nombre varchar(25) NOT NULL,
    pais varchar(15) NOT NULL,
    precio_compra decimal(10,2) NOT NULL,
    precio_venta decimal(10,2) NOT NULL,
    CONSTRAINT moneda_pk PRIMARY KEY (id)
);

-- Table: movimiento_comision
CREATE TABLE movimiento_comision (
    id int NOT NULL AUTO_INCREMENT,
    nombre_comision varchar(40) NOT NULL,
    costo_comision decimal(6,2) NOT NULL,
    CONSTRAINT movimiento_comision_pk PRIMARY KEY (id)
);

-- Table: sucursal
CREATE TABLE sucursal (
    id int NOT NULL AUTO_INCREMENT,
    ciudad varchar(30) NOT NULL,
    direccion varchar(45) NOT NULL,
    CONSTRAINT sucursal_pk PRIMARY KEY (id)
);

-- Table: tipo_cuenta
CREATE TABLE tipo_cuenta (
    id int NOT NULL AUTO_INCREMENT,
    nombre varchar(30) NOT NULL,
    CONSTRAINT tipo_cuenta_pk PRIMARY KEY (id)
);

-- Table: tipo_usuario
CREATE TABLE tipo_usuario (
    id int NOT NULL AUTO_INCREMENT,
    usuario_tipo varchar(30) NOT NULL,
    CONSTRAINT tipo_usuario_pk PRIMARY KEY (id)
);

-- Table: transaccion
CREATE TABLE transaccion (
    id int NOT NULL AUTO_INCREMENT,
    monto float(14,2) NOT NULL,
    fecha_movimiento date NOT NULL,
    cuenta_numero_cuenta int NOT NULL,
    moneda_id int NOT NULL,
    movimiento_comision_id int NOT NULL,
    CONSTRAINT transaccion_pk PRIMARY KEY (id)
);

-- Table: usuario
CREATE TABLE usuario (
    id int NOT NULL AUTO_INCREMENT,
    estado boolean NOT NULL,
    tipo_usuario_id int NOT NULL,
    CONSTRAINT usuario_pk PRIMARY KEY (id)
);

-- foreign keys
-- Reference: cliente_tipo_usuario (table: usuario)
ALTER TABLE usuario ADD CONSTRAINT cliente_tipo_usuario FOREIGN KEY cliente_tipo_usuario (tipo_usuario_id)
    REFERENCES tipo_usuario (id);

-- Reference: cuenta_sucursal (table: cuenta)
ALTER TABLE cuenta ADD CONSTRAINT cuenta_sucursal FOREIGN KEY cuenta_sucursal (sucursal_id)
    REFERENCES sucursal (id);

-- Reference: cuenta_tipo_cuenta (table: cuenta)
ALTER TABLE cuenta ADD CONSTRAINT cuenta_tipo_cuenta FOREIGN KEY cuenta_tipo_cuenta (tipo_cuenta_id)
    REFERENCES tipo_cuenta (id);

-- Reference: cuenta_usuario (table: cuenta)
ALTER TABLE cuenta ADD CONSTRAINT cuenta_usuario FOREIGN KEY cuenta_usuario (usuario_id)
    REFERENCES usuario (id);

-- Reference: datos_cuenta_cuenta (table: datos_cuenta)
ALTER TABLE datos_cuenta ADD CONSTRAINT datos_cuenta_cuenta FOREIGN KEY datos_cuenta_cuenta (cuenta_numero_cuenta)
    REFERENCES cuenta (numero_cuenta);

-- Reference: datos_usuario_usuario (table: datos_usuario)
ALTER TABLE datos_usuario ADD CONSTRAINT datos_usuario_usuario FOREIGN KEY datos_usuario_usuario (usuario_id)
    REFERENCES usuario (id);

-- Reference: login_usuario (table: login)
ALTER TABLE login ADD CONSTRAINT login_usuario FOREIGN KEY login_usuario (usuario_id)
    REFERENCES usuario (id);

-- Reference: movimiento_cuenta (table: transaccion)
ALTER TABLE transaccion ADD CONSTRAINT movimiento_cuenta FOREIGN KEY movimiento_cuenta (cuenta_numero_cuenta)
    REFERENCES cuenta (numero_cuenta);

-- Reference: transaccion_moneda (table: transaccion)
ALTER TABLE transaccion ADD CONSTRAINT transaccion_moneda FOREIGN KEY transaccion_moneda (moneda_id)
    REFERENCES moneda (id);

-- Reference: transaccion_movimiento_comision (table: transaccion)
ALTER TABLE transaccion ADD CONSTRAINT transaccion_movimiento_comision FOREIGN KEY transaccion_movimiento_comision (movimiento_comision_id)
    REFERENCES movimiento_comision (id);

-- End of file.

