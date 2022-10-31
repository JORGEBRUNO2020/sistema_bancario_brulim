class Usuario():

    def __init__(self,nombre_usuario, password):
        self.__nombre = nombre_usuario
        self.__password = password

    def __str__(self):
        return ("Nombre de usuario: " + str(self.__nombre) + "\nPassword: " + str(self.__password))

    def get_usuarios(listar_usuarios, conn):
        listar_usuarios.execute('select us.id, du.nombre, du.apellido, du.razon_social, tu.usuario_tipo from usuario us	join datos_usuario du on us.id = du.usuario_id 	join tipo_usuario tu on us.tipo_usuario_id = tu.id order by us.id asc')
        listado_usuarios=listar_usuarios.fetchall()
        conn.commit()
        return listado_usuarios

    def get_nombre_usuario():
        pass

    def get_password():
        pass

    def set_password():
        pass
        
    def set_nombre_usuario():
        pass


