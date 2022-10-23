from templates.clases.cuentas import Cuenta

class Caja_ahorro_comun(Cuenta):

    def __init__(self, titular, sucursal, numero_cuenta, cbu, fecha_apertura, saldo, tipo):
        Cuenta.__init__(self, titular, sucursal, numero_cuenta, cbu, fecha_apertura, saldo)
        self.__tipo = tipo

    def get_titular():
        pass

    def get_sucursal():
        pass

    def get_numero_cuenta():
        pass

    def get_fecha_apertura():
        pass

    def get_cbu():
        pass

    def get_fecha_apertura():
        pass

    def get_saldo(cursor, conn, usuario_id):
        usuario_id = usuario_id
        cursor.execute(	'select * from usuario us join cuenta cu on us.id = cu.usuario_id join tipo_cuenta tc on tc.id = cu.tipo_cuenta_id join sucursal sc on sc.id = cu.sucursal_id join datos_cuenta dc on cu.numero_cuenta = dc.cuenta_numero_cuenta where us.id =%s',(usuario_id))
        cuentas_datos=cursor.fetchall()
        conn.commit()
        return cuentas_datos

    def get_tipo():
        pass

