from  templates.models.cuentas import Cuenta
from  templates.models.cuenta_corriente import Cuenta_corriente
from flask import render_template
import random as rd
from datetime import datetime

class Cuenta_corriente_dolares(Cuenta_corriente ,Cuenta):

    def __init__(self, titular, sucursal, numero_cuenta, cbu, fecha_apertura, saldo, tipo, moneda):
        Cuenta.__init__(self, titular, sucursal, numero_cuenta, cbu, fecha_apertura, saldo)
        Cuenta_corriente.__init__(self, tipo)
        self.__moneda = moneda

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

    def get_moneda():
        pass

    def set_crear_cuenta_corriente_dolares(cursor, conn, usuario):

        cbu = rd.randint(90000000,99999999)
        cursor.execute("insert into cuenta (cbu, saldo, sucursal_id, tipo_cuenta_id, usuario_id) VALUES (%s, 0, 1, 5, %s)",(cbu, usuario))
        conn.commit()
        cursor.execute('SELECT max(numero_cuenta) FROM cuenta') 
        ultimo = cursor.fetchall()
        cursor.execute("INSERT INTO datos_cuenta ( cuenta_numero_cuenta, fecha_apertura, estado) VALUES(%s,%s, 1)",(ultimo, datetime.now()))
        conn.commit()
        return render_template('/views/main_page.html')