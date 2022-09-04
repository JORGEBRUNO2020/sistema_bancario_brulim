-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-09-04 21:50:13.231

-- tables
-- Table: cliente
CREATE TABLE cliente (
    id serial  NOT NULL,
    estado boolean  NOT NULL,
    tipo_cliente_id int  NOT NULL,
    CONSTRAINT cliente_pk PRIMARY KEY (id)
);

-- Table: comision
CREATE TABLE comision (
    id serial  NOT NULL,
    nombre_comision varchar(40)  NOT NULL,
    costo_comision decimal(10,2)  NOT NULL,
    movimiento_id int  NOT NULL,
    CONSTRAINT comision_pk PRIMARY KEY (id)
);

-- Table: cuenta
CREATE TABLE cuenta (
    numero_cuenta serial  NOT NULL,
    cbu varchar(10)  NOT NULL,
    saldo decimal(14,2)  NOT NULL,
    cliente_id int  NOT NULL,
    sucursal_id int  NOT NULL,
    tipo_cuenta_id int  NOT NULL,
    moneda_id int  NOT NULL,
    CONSTRAINT cuenta_pk PRIMARY KEY (numero_cuenta)
);

-- Table: datos_cliente
CREATE TABLE datos_cliente (
    cuil_cuit int  NOT NULL,
    dni int  NOT NULL,
    nombre varchar(45)  NOT NULL,
    apellido varchar(40)  NOT NULL,
    razon_social varchar(45)  NOT NULL,
    telefono varchar(20)  NOT NULL,
    email varchar(60)  NOT NULL,
    cliente_id int  NOT NULL,
    CONSTRAINT datos_cliente_pk PRIMARY KEY (cuil_cuit)
);

-- Table: datos_cuenta
CREATE TABLE datos_cuenta (
    fecha_apertura date  NOT NULL,
    estado boolean  NOT NULL,
    cuenta_numero_cuenta int  NOT NULL,
    CONSTRAINT datos_cuenta_pk PRIMARY KEY (cuenta_numero_cuenta)
);

-- Table: login
CREATE TABLE login (
    nombre_usuario varchar(40)  NOT NULL,
    password varchar(25)  NOT NULL,
    cliente_id int  NOT NULL,
    CONSTRAINT login_pk PRIMARY KEY (nombre_usuario)
);

-- Table: moneda
CREATE TABLE moneda (
    id serial  NOT NULL,
    nombre varchar(25)  NOT NULL,
    pais varchar(15)  NOT NULL,
    precio_compra decimal(10,2)  NOT NULL,
    precio_venta decimal(10,2)  NOT NULL,
    CONSTRAINT moneda_pk PRIMARY KEY (id)
);

-- Table: movimiento
CREATE TABLE movimiento (
    id serial  NOT NULL,
    tipo_movimiento varchar(25)  NOT NULL,
    monto decimal(14,2)  NOT NULL,
    fecha_movimiento date  NOT NULL,
    CONSTRAINT movimiento_pk PRIMARY KEY (id)
);

-- Table: operacion
CREATE TABLE operacion (
    movimientos_id int  NOT NULL,
    cuentas_numero_cuenta int  NOT NULL,
    CONSTRAINT operacion_pk PRIMARY KEY (cuentas_numero_cuenta,movimientos_id)
);

-- Table: sucursal
CREATE TABLE sucursal (
    id serial  NOT NULL,
    ciudad varchar(30)  NOT NULL,
    direccion varchar(45)  NOT NULL,
    CONSTRAINT sucursal_pk PRIMARY KEY (id)
);

-- Table: tipo_cliente
CREATE TABLE tipo_cliente (
    id serial  NOT NULL,
    cliente_tipo varchar(30)  NOT NULL,
    CONSTRAINT tipo_cliente_pk PRIMARY KEY (id)
);

-- Table: tipo_cuenta
CREATE TABLE tipo_cuenta (
    id serial  NOT NULL,
    nombre varchar(30)  NOT NULL,
    CONSTRAINT tipo_cuenta_pk PRIMARY KEY (id)
);

-- foreign keys
-- Reference: cliente_tipo_cliente (table: cliente)
ALTER TABLE cliente ADD CONSTRAINT cliente_tipo_cliente
    FOREIGN KEY (tipo_cliente_id)
    REFERENCES tipo_cliente (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: comision_movimiento (table: comision)
ALTER TABLE comision ADD CONSTRAINT comision_movimiento
    FOREIGN KEY (movimiento_id)
    REFERENCES movimiento (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: cuenta_cliente (table: cuenta)
ALTER TABLE cuenta ADD CONSTRAINT cuenta_cliente
    FOREIGN KEY (cliente_id)
    REFERENCES cliente (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: cuenta_moneda (table: cuenta)
ALTER TABLE cuenta ADD CONSTRAINT cuenta_moneda
    FOREIGN KEY (moneda_id)
    REFERENCES moneda (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: cuenta_sucursal (table: cuenta)
ALTER TABLE cuenta ADD CONSTRAINT cuenta_sucursal
    FOREIGN KEY (sucursal_id)
    REFERENCES sucursal (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: cuenta_tipo_cuenta (table: cuenta)
ALTER TABLE cuenta ADD CONSTRAINT cuenta_tipo_cuenta
    FOREIGN KEY (tipo_cuenta_id)
    REFERENCES tipo_cuenta (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: datos_cliente_cliente (table: datos_cliente)
ALTER TABLE datos_cliente ADD CONSTRAINT datos_cliente_cliente
    FOREIGN KEY (cliente_id)
    REFERENCES cliente (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: datos_cuenta_cuenta (table: datos_cuenta)
ALTER TABLE datos_cuenta ADD CONSTRAINT datos_cuenta_cuenta
    FOREIGN KEY (cuenta_numero_cuenta)
    REFERENCES cuenta (numero_cuenta)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: login_cliente (table: login)
ALTER TABLE login ADD CONSTRAINT login_cliente
    FOREIGN KEY (cliente_id)
    REFERENCES cliente (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: operacion_cuentas (table: operacion)
ALTER TABLE operacion ADD CONSTRAINT operacion_cuentas
    FOREIGN KEY (cuentas_numero_cuenta)
    REFERENCES cuenta (numero_cuenta)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: operacion_movimientos (table: operacion)
ALTER TABLE operacion ADD CONSTRAINT operacion_movimientos
    FOREIGN KEY (movimientos_id)
    REFERENCES movimiento (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

