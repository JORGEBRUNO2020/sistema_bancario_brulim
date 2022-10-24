class Cuenta():

    def __init__(self, titular, sucursal, numero_cuenta, cbu, fecha_apertura, saldo):
        self.__titular = titular
        self.__sucursal = sucursal
        self.__numero_cuenta = numero_cuenta
        self.__cbu = cbu
        self.__fecha_apertura = fecha_apertura
        self.__saldo = saldo

    def __str__(self):
        return ("Titular: " + str(self.__titular) + "\nSucursal: " + str(self.__sucursal) + "\nN° de cuenta: " + str(self.__numero_cuenta) + "\nC.B.U.: " + str(self.__cbu) + "\nFecha de Apertura: " + str(self.__fecha_apertura) + "\nSaldo : $ " + str(self.__saldo))
    
    def get_cuentas(listar_cuentas, conn, usuario_id):
        usuario_id = usuario_id
        listar_cuentas.execute('select cu.cbu, cu.numero_cuenta, cu.sucursal_id, tc.nombre,dc.fecha_apertura, sc.direccion, sc.ciudad  from usuario us join cuenta cu on us.id = cu.usuario_id join tipo_cuenta tc on tc.id = cu.tipo_cuenta_id join sucursal sc on sc.id = cu.sucursal_id join datos_cuenta dc on cu.numero_cuenta = dc.cuenta_numero_cuenta where us.id = %s order by cu.numero_cuenta asc',(usuario_id))
        listado_cuentas=listar_cuentas.fetchall()
        print(listado_cuentas)
        conn.commit()
        return listado_cuentas
    
    def get_saldo():
        pass
        
    def get_titular():
        pass

    def get_numero_cuenta():
        pass

    def get_cbu():
        pass

    def get_saldo():
        pass

    def get_fecha_apertura():
        pass