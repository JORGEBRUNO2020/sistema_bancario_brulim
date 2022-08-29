-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-08-28 13:20:21.705

-- tables
-- Table: cliente
CREATE TABLE cliente (
    id serial  NOT NULL,
    nombre varchar(45)  NOT NULL,
    apellido varchar(40)  NOT NULL,
    dni varchar(8)  NOT NULL,
    telefono varchar(15)  NOT NULL,
    email varchar(60)  NULL,
    nombre_usuario varchar(40)  NOT NULL,
    password varchar(25)  NOT NULL,
    CONSTRAINT cliente_pk PRIMARY KEY (id)
);

-- Table: cuentas
CREATE TABLE cuentas (
    numero_cuenta serial  NOT NULL,
    cbu varchar(10)  NOT NULL,
    saldo decimal(15,2)  NOT NULL DEFAULT 0,
    fecha_apertura timestamp  NOT NULL,
    sucursal_id int  NOT NULL,
    tipo_cuenta_id int  NOT NULL,
    cliente_id int  NOT NULL,
    moneda_id int  NOT NULL,
    CONSTRAINT cuentas_pk PRIMARY KEY (numero_cuenta)
);

-- Table: moneda
CREATE TABLE moneda (
    id serial  NOT NULL,
    nombre varchar(25)  NOT NULL,
    pais varchar(15)  NOT NULL,
    precio_compra money  NOT NULL,
    precio_venta money  NOT NULL,
    CONSTRAINT moneda_pk PRIMARY KEY (id)
);

-- Table: movimientos
CREATE TABLE movimientos (
    id serial  NOT NULL,
    tipo_movimiento varchar(25)  NOT NULL,
    CONSTRAINT movimientos_pk PRIMARY KEY (id)
);

-- Table: operacion
CREATE TABLE operacion (
    movimientos_id int  NOT NULL,
    cuentas_numero_cuenta int  NOT NULL,
    CONSTRAINT operacion_pk PRIMARY KEY (movimientos_id)
);

-- Table: sucursal
CREATE TABLE sucursal (
    id serial  NOT NULL,
    ciudad varchar(30)  NOT NULL,
    CONSTRAINT sucursal_pk PRIMARY KEY (id)
);

-- Table: tipo_cuenta
CREATE TABLE tipo_cuenta (
    id serial  NOT NULL,
    nombre varchar(30)  NOT NULL,
    CONSTRAINT tipo_cuenta_pk PRIMARY KEY (id)
);

-- foreign keys
-- Reference: cuentas_cliente (table: cuentas)
ALTER TABLE cuentas ADD CONSTRAINT cuentas_cliente
    FOREIGN KEY (cliente_id)
    REFERENCES cliente (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: cuentas_moneda (table: cuentas)
ALTER TABLE cuentas ADD CONSTRAINT cuentas_moneda
    FOREIGN KEY (moneda_id)
    REFERENCES moneda (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: cuentas_sucursal (table: cuentas)
ALTER TABLE cuentas ADD CONSTRAINT cuentas_sucursal
    FOREIGN KEY (sucursal_id)
    REFERENCES sucursal (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: cuentas_tipo_cuenta (table: cuentas)
ALTER TABLE cuentas ADD CONSTRAINT cuentas_tipo_cuenta
    FOREIGN KEY (tipo_cuenta_id)
    REFERENCES tipo_cuenta (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: operacion_cuentas (table: operacion)
ALTER TABLE operacion ADD CONSTRAINT operacion_cuentas
    FOREIGN KEY (cuentas_numero_cuenta)
    REFERENCES cuentas (numero_cuenta)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: operacion_movimientos (table: operacion)
ALTER TABLE operacion ADD CONSTRAINT operacion_movimientos
    FOREIGN KEY (movimientos_id)
    REFERENCES movimientos (id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

