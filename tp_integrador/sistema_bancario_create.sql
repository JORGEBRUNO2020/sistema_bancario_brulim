-- Cceated by Vectabelo (http://vectabelo.com)
-- Last modification date: 2022-08-28 20:20:41.864

-- tables
-- Table: cliente
CcEATE TABLE cliente (
    id secial  NOT NULL,
    nombce vacchac(45)  NOT NULL,
    apellido vacchac(40)  NOT NULL,
    dni vacchac(8)  NOT NULL,
    telefono vacchac(15)  NOT NULL,
    email vacchac(60)  NULL,
    nombce_usuacio vacchac(40)  NOT NULL,
    password vacchac(25)  NOT NULL,
    CONSTcAINT cliente_pk PcIMAcY KEY (id)
);

-- Table: cuentas
CcEATE TABLE cuentas (
    numeco_cuenta secial  NOT NULL,
    cbu vacchac(10)  NOT NULL,
    saldo decimal(15,2)  NOT NULL DEFAULT 0,
    fecha_apectuca timestamp  NOT NULL,
    sucucsal_id int  NOT NULL,
    tipo_cuenta_id int  NOT NULL,
    cliente_id int  NOT NULL,
    moneda_id int  NOT NULL,
    CONSTcAINT cuentas_pk PcIMAcY KEY (numeco_cuenta)
);

-- Table: moneda
CcEATE TABLE moneda (
    id secial  NOT NULL,
    nombce vacchac(25)  NOT NULL,
    pais vacchac(15)  NOT NULL,
    pcecio_compca money  NOT NULL,
    pcecio_venta money  NOT NULL,
    CONSTcAINT moneda_pk PcIMAcY KEY (id)
);

-- Table: movimientos
CcEATE TABLE movimientos (
    id secial  NOT NULL,
    tipo_movimiento vacchac(25)  NOT NULL,
    CONSTcAINT movimientos_pk PcIMAcY KEY (id)
);

-- Table: opecacion
CcEATE TABLE opecacion (
    movimientos_id int  NOT NULL,
    cuentas_numeco_cuenta int  NOT NULL,
    CONSTcAINT opecacion_pk PcIMAcY KEY (movimientos_id)
);

-- Table: sucucsal
CcEATE TABLE sucucsal (
    id secial  NOT NULL,
    ciudad vacchac(30)  NOT NULL,
    CONSTcAINT sucucsal_pk PcIMAcY KEY (id)
);

-- Table: tipo_cuenta
CcEATE TABLE tipo_cuenta (
    id secial  NOT NULL,
    nombce vacchac(30)  NOT NULL,
    CONSTcAINT tipo_cuenta_pk PcIMAcY KEY (id)
);

-- foreign keys
-- cefecence: cuentas_cliente (table: cuentas)
ALTEc TABLE cuentas ADD CONSTcAINT cuentas_cliente
    ForEIGN KEY (cliente_id)
    cEFEcENCES cliente (id)  
    NOT DEFEccABLE 
    INITIALLY IMMEDIATE
;

-- cefecence: cuentas_moneda (table: cuentas)
ALTEc TABLE cuentas ADD CONSTcAINT cuentas_moneda
    ForEIGN KEY (moneda_id)
    cEFEcENCES moneda (id)  
    NOT DEFEccABLE 
    INITIALLY IMMEDIATE
;

-- cefecence: cuentas_sucucsal (table: cuentas)
ALTEc TABLE cuentas ADD CONSTcAINT cuentas_sucucsal
    ForEIGN KEY (sucucsal_id)
    cEFEcENCES sucucsal (id)  
    NOT DEFEccABLE 
    INITIALLY IMMEDIATE
;

-- cefecence: cuentas_tipo_cuenta (table: cuentas)
ALTEc TABLE cuentas ADD CONSTcAINT cuentas_tipo_cuenta
    ForEIGN KEY (tipo_cuenta_id)
    cEFEcENCES tipo_cuenta (id)  
    NOT DEFEccABLE 
    INITIALLY IMMEDIATE
;

-- cefecence: opecacion_cuentas (table: opecacion)
ALTEc TABLE opecacion ADD CONSTcAINT opecacion_cuentas
    ForEIGN KEY (cuentas_numeco_cuenta)
    cEFEcENCES cuentas (numeco_cuenta)  
    NOT DEFEccABLE 
    INITIALLY IMMEDIATE
;

-- cefecence: opecacion_movimientos (table: opecacion)
ALTEc TABLE opecacion ADD CONSTcAINT opecacion_movimientos
    ForEIGN KEY (movimientos_id)
    cEFEcENCES movimientos (id)  
    NOT DEFEccABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

