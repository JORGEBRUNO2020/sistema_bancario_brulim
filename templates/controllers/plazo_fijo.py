from  templates.controllers.individuo import Individuos 

class Plazo_fijo():

    def __init__(self, numero_plazo_fijo, cuitCuil, plazo, monto, fecha_inicio, intereses):
        self.__numero_plazo_fijo = numero_plazo_fijo
        self.__cuit_cuil = cuitCuil
        self.__plazo = plazo
        self.__monto = monto
        self.__fecha_inicio = fecha_inicio
        self.__intereses = intereses

    def __str__(self):
        txt = "N° Plazo Fijo: {0} \nCuit Cuil: {1} \nPlazo (dias): {2} \nMonto: $ {3} \nFecha de inicio: {4} \nIntereses: {5}%"
        return txt.format(self.__numero_plazo_fijo, self.__cuit_cuil, self.__plazo, self.__monto, self.__fecha_inicio, self.__intereses)
    

    def get_numero_plazo_fijo():
        pass

    def get_titular():
        pass

    def get_plazo():
        pass

    def get_monto():
        pass

    def get_fecha_inicio():
        pass

    def get_fecha_vencimiento():
        pass

    def get_intereses():
        pass

    def get_monto_retiro():
        pass

    def set_monto():
        pass

    def set_fecha_vencimiento():
        pass
