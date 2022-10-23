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
     #   cursor.execute('SELECT * FROM cuenta WHERE usuario_id=%s AND tipo_cuenta_id=%s AND numero_cuenta=%s',(usuario_id,tipo_cuenta_id,numero_cuenta))
        cursor.execute('select * from usuario us join datos_usuario du on us.id = du.usuario_id join cuenta cu on us.id = cu.usuario_id join tipo_cuenta tc on tc.id = cu.tipo_cuenta_id where us.id =%s',(usuario_id))
        cuentas_datos=cursor.fetchall()
        conn.commit()
        return cuentas_datos
        # try: 
        #     if password[0][0] == _usuario and password[0][1] == _password:
        #         return True
        #     else:
        #         return False
        # except Exception as e:
        #     print("Exception Occured while code Execution: "+ str(e))
        #     return False
        

    def get_tipo():
        pass

