from  templates.controllers.usuarios import Usuario

class Administrador(Usuario):

    def __init__(self, nombre_usuario, password):
        Usuario.__init__(self, nombre_usuario, password )
        self.__nombre_usuario = nombre_usuario
        self.__password = password

    def __str__(self):
        return ("\nUsuario administrador: " + str(self.__nombre_usuario) + "\nPassword administrador: " + str(self.__password) + "\n")

    def get_cliente():
        pass

    def get_movimientos_cuentas():
        pass

    def get_nombre_usuario():
        pass

    def get_password():
        pass

    def get_saldo():
        pass

    def set_cliente():
        pass

    def set_datos_cliente():
        pass

    def set_costos_mantenimiento():
        pass

    def set_nombre_usuario():
        pass

    def set_password():
        pass