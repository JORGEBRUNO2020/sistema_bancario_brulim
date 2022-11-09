from flask import render_template
from  templates.models.cuentas import Cuenta
import random as rd

class Cuenta_corriente(Cuenta):

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

    def get_saldo():
        pass

    def get_tipo():
        pass

    def set_crear_cuenta_corriente_pesos(cursor, conn, usuario):
        cbu = rd.randint(90000000,99999999)
        cursor.execute("insert into cuenta (cbu, saldo, sucursal_id, tipo_cuenta_id, usuario_id) VALUES (%s, 0, 1, 3, %s)",(cbu, usuario))
        conn.commit()
        return render_template('/views/main_page.html')
