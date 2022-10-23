from  templates.clases.clientes import Usuario, Cliente



class Individuos(Cliente,Usuario):
    def __init__ (self, nombre, apellido, dni, domicilio, cuitCuil, telefono, mail, nombre_usuario, password):
        Cliente.__init__(self, domicilio, cuitCuil, telefono, mail)
        Usuario.__init__(self,nombre_usuario, password)
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        
    def __str__(self):
        return ("Nombre: " + str(self.__nombre) + "\nApellido: " + str(self.__apellido) + "\nDomicilio: " + str(self.__domicilio) + "\nDNI: " + str(self.__dni) + "\nCUIT/CUIL: " + str(self.__cuitCuil) + "\nTelefono: " + str(self.__telefono) + "\nEmail: " + str(self.__mail) + "\nUsuario: " + str(self.__nombre_usuario) + "\nPassword: " + str(self.__password) + "\n")

    def get_cuentas ():
        pass

    def get_transferir():
        pass

    def get_depositar():
        pass

    def get_nombre():
        pass

    def get_apellido():
        pass

    def set_nombre(): #¿ PORQUÉ QUISIERA CAMBIAR EL NOMBRE O EL APELLIDO?
        pass

    def set_apellido():
        pass


