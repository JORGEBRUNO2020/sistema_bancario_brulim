from  templates.models.cuentas import Cuenta
from  templates.models.cuenta_corriente import Cuenta_corriente

class Cuenta_corriente_sr(Cuenta_corriente ,Cuenta):

    def __init__(self, titular, sucursal, numero_cuenta, cbu, fecha_apertura, saldo, tipo, saldo_retenido):
        Cuenta.__init__(self, titular, sucursal, numero_cuenta, cbu, fecha_apertura, saldo)
        Cuenta_corriente.__init__(self, tipo)
        self.__saldo_retenido = saldo_retenido

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

    def get_saldo_retenido():
        pass
