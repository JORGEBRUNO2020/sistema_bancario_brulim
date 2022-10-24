from  templates.controllers.clientes import Usuario, Cliente



class Pyme(Cliente,Usuario):
    def __init__ (self, razon_social, domicilio, cuitCuil, telefono, mail, nombre_usuario, password):
        Cliente.__init__(self, domicilio, cuitCuil, telefono, mail)
        Usuario.__init__(self,nombre_usuario, password)
        self.__razon_social = razon_social

    def __str__(self):
        return ("Razón social: " + str(self.__razon_social) + "\nDomicilio: " + str(self.__domicilio) + "\nCUIT/CUIL: " + str(self.__cuitCuil) + "\nTelefono: " + str(self.__telefono) + "\nEmail: " + str(self.__mail) + "\nUsuario: " + str(self.__nombre_usuario) + "\nPassword: " + str(self.__password) + "\n")

    def get_nombre_usuario():
        pass