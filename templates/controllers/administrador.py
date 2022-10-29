from  templates.controllers.usuarios import Usuario
from flask import render_template



class Administrador(Usuario):

    def __init__(self, nombre_usuario, password):
        Usuario.__init__(self, nombre_usuario, password )
        self.__nombre_usuario = nombre_usuario
        self.__password = password

    def __str__(self):
        return ("\nUsuario administrador: " + str(self.__nombre_usuario) + "\nPassword administrador: " + str(self.__password) + "\n")

    def get_cliente_individuo(conn, cargar_individuo, cuitcuil, password, nombre, apellido, telefono, email):
        query = "INSERT INTO  datos_usuario values (%s,%s, %s, %s, %s, %s, %s, %s)"
        datos = (cuitcuil, password, nombre, apellido, '',telefono, email, "2")
        
        cargar_individuo.execute(query, datos) 
        
        conn.commit()
        return render_template('/views/administrador_cargar_cliente_individuo.html')

    def get_cliente_pyme():
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