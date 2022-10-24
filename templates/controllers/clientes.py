from  templates.controllers.usuarios import Usuario

class Cliente(Usuario):

    def __init__(self, nombre_usuario, password, domicilio, cuitCuil, telefono, mail):
        Usuario.__init__(self, nombre_usuario, password )
        self.__domicilio = domicilio
        self.__cuitCuil = cuitCuil
        self.__telefono = telefono
        self.__mail = mail
    

    def get_saldo():
        pass
        
    def get_numero_cuenta():
        pass

    def get_cbu():
        pass

    def get_fecha_apertura():
        pass

    def set_cuenta():
        pass

    def set_depositar():
        pass

    def set_extraer():
        pass

    def set_transferir():
        pass

    def set_compar_moneda_extranjera():
        pass

    def set_abrir_plazo_fijo():
        pass

    def set_pagar_en_linea():
        pass

    def set_cerrar_cuenta():
        pass



