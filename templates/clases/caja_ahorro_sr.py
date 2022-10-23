from  templates.clases.caja_ahorro_comun import Caja_ahorro_comun
from  templates.clases.caja_ahorro_comun import Caja_ahorro_comun, Cuenta


class Caja_ahorro_saldo_retenido(Caja_ahorro_comun, Cuenta):

    def __init__(self, titular, sucursal, numero_cuenta, cbu, fecha_apertura, saldo, tipo, saldo_retenido):
        Caja_ahorro_comun.__init__(self, titular, sucursal, numero_cuenta, cbu, fecha_apertura, saldo, tipo)
        Cuenta.__init__((self, titular, sucursal, numero_cuenta, cbu, fecha_apertura, saldo))
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

