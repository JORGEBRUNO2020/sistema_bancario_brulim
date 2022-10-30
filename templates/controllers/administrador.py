from  templates.controllers.usuarios import Usuario
from flask import render_template



class Administrador(Usuario):

    def __init__(self, nombre_usuario, password):
        Usuario.__init__(self, nombre_usuario, password )
        self.__nombre_usuario = nombre_usuario
        self.__password = password

    def __str__(self):
        return ("\nUsuario administrador: " + str(self.__nombre_usuario) + "\nPassword administrador: " + str(self.__password) + "\n")

    def get_cliente_individuo():
        pass

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
    



    def set_datos_cliente_individuo(conn, cargar_individuo, cuitcuil, dni, nombre, apellido, telefono, email):
        cargar_individuo.execute("SELECT max(id) FROM usuario")
        ultimo = cargar_individuo.fetchall()
        print(ultimo[0][0]) # BORRAR
        query = "INSERT INTO  datos_usuario (cuil_cuit, dni, nombre, apellido, razon_social, telefono, email, usuario_id) values (%s,%s, %s, %s, %s, %s, %s, %s)"
        datos = (cuitcuil, dni, nombre, apellido, '',telefono, email, ultimo[0][0])
        
        cargar_individuo.execute(query, datos) 
        
        conn.commit()
        return render_template('/views/administrador_cargar_cliente_individuo.html')

    def set_datos_cliente_pyme(conn, cargar_pyme, _cuitcuil, _razon_social, _telefono, _email):
        cargar_pyme.execute("SELECT max(id) FROM usuario")
        ultimo = cargar_pyme.fetchall()
        

        query = "INSERT INTO  datos_usuario (cuil_cuit, dni, nombre, apellido, razon_social, telefono, email, usuario_id) values (%s,%s, %s, %s, %s, %s, %s, %s)"
        datos = (_cuitcuil, '', '', '', _razon_social, _telefono, _email, ultimo[0][0])
        
        cargar_pyme.execute(query, datos) 
        
        conn.commit()
        return render_template('/views/administrador_cargar_cliente_pyme.html')

    def set_costos_mantenimiento():

        pass

    def set_login(conn, cargar_individuo, nombre_usuario, password):

        ultimo = cargar_individuo.execute("SELECT max(id) FROM usuario")
        ultimo = cargar_individuo.fetchall() 
        

        query = "INSERT INTO  login values ( %s,%s, %s)"
        datos = (nombre_usuario, password, ultimo[0][0])
        
        cargar_individuo.execute(query, datos) 
        
        conn.commit()
        return render_template('/views/administrador_cargar_cliente_individuo.html')
    
    def set_usuario(conn, cargar_individuo, tipo):
        
        cargar_individuo.execute("insert into usuario (estado, tipo_usuario_id) values ( 1,%s)", tipo)

        conn.commit()

        return render_template('/views/administrador_cargar_cliente_individuo.html')


    # def set_password():
    #     pass