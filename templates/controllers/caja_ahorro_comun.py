from templates.controllers.cuentas import Cuenta

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

    def get_saldo(listar_saldos, conn, usuario_id):
        usuario_id = usuario_id
        listar_saldos.execute('select * from usuario us join datos_usuario du on us.id = du.usuario_id join cuenta cu on us.id = cu.usuario_id join tipo_cuenta tc on tc.id = cu.tipo_cuenta_id where us.id =%s order by cu.numero_cuenta asc',(usuario_id))
        cuentas_datos=listar_saldos.fetchall()
        conn.commit()
        return cuentas_datos

    def get_tipo():
        pass

    def get_movimientos(listar_movimientos, conn, usuario_id):
        usuario_id = usuario_id
       # listar_movimientos.execute(	'select * from usuario us join datos_usuario du on us.id = du.usuario_id join cuenta cu on us.id = cu.usuario_id join tipo_cuenta tc on tc.id = cu.tipo_cuenta_id where us.id =%s order by cu.numero_cuenta asc',(usuario_id))
        listar_movimientos.execute('select ca.numero_cuenta, ca.tipo_cuenta_id, ts.id, ts.monto, ts.fecha_movimiento, mc.nombre_comision, mc.costo_comision, mo.nombre, mo.precio_compra, mo.precio_venta from transaccion ts join cuenta ca on ts.cuenta_numero_cuenta = ca.numero_cuenta join movimiento_comision mc on mc.id = ts.movimiento_comision_id join moneda mo on mo.id = ts.moneda_id where ts.cuenta_numero_cuenta  =%s',(usuario_id))
        cuenta_movimientos=listar_movimientos.fetchall()
        print(cuenta_movimientos)
        conn.commit()
        return cuenta_movimientos

