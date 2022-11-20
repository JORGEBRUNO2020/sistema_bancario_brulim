from flask import render_template
from templates.models.cuentas import Cuenta
import random as rd
from datetime import datetime

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

    def set_saldo(mod_saldo,conn, usuario_id, num, monto):
        monto = int(monto)
        print(monto)
        if monto >= 0:
            usuario_id = usuario_id
            mod_saldo.execute('update cuenta set saldo = saldo + %s where numero_cuenta = %s', (monto, num))
            saldo = mod_saldo.fetchall()
            conn.commit()
            return saldo
        else:
            mod_saldo.execute('select cu.saldo from cuenta cu where cu.numero_cuenta = %s', (num))
            saldo = mod_saldo.fetchall()
            saldo_disponible  = saldo[0][0]
            saldo_disponible = float(saldo_disponible)
            print(saldo_disponible)
            if (saldo_disponible + monto) >= 0:
                usuario_id = usuario_id
                mod_saldo.execute('update cuenta set saldo = saldo + %s where numero_cuenta = %s', (monto, num))
                saldo = mod_saldo.fetchall()
                conn.commit()
                return saldo
       
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
        listar_movimientos.execute('select ca.numero_cuenta, ca.tipo_cuenta_id, ts.id, ts.monto, ts.fecha_movimiento, mc.nombre_comision, mc.costo_comision, mo.nombre, mo.precio_compra, mo.precio_venta from transaccion ts join cuenta ca on ts.cuenta_numero_cuenta = ca.numero_cuenta join movimiento_comision mc on mc.id = ts.movimiento_comision_id join moneda mo on mo.id = ts.moneda_id where ts.cuenta_numero_cuenta  =%s',(usuario_id))
        cuenta_movimientos=listar_movimientos.fetchall()
        conn.commit()
        return cuenta_movimientos

    def get_id_cuenta(numero_cuenta):
        numero_cuenta = numero_cuenta
        numero_cuenta_obtenido = numero_cuenta
        return numero_cuenta_obtenido

    def get_listado_movimientos(array_movimientos, id_cuenta):
        store_resultados= []
        for item in array_movimientos:
            if int(item[0]) == int(id_cuenta):
                store_resultados.append(item)
        return store_resultados

    def set_crear_cuenta_caja_ahorro(cursor, conn, usuario):
        cbu = rd.randint(90000000,99999999)
        cursor.execute("insert into cuenta (cbu, saldo, sucursal_id, tipo_cuenta_id, usuario_id) VALUES (%s, 0, 1, 1, %s)",(cbu, usuario))
        conn.commit()
        cursor.execute('SELECT max(numero_cuenta) FROM cuenta') 
        ultimo = cursor.fetchall()
        cursor.execute("INSERT INTO datos_cuenta ( cuenta_numero_cuenta, fecha_apertura, estado) VALUES(%s,%s, 1)",(ultimo, datetime.now()))
        conn.commit()
        return render_template('/views/main_page.html')

