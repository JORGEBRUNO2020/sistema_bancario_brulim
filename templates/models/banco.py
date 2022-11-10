class Banco():
    

    def __init__(self, nombre):
        self.__nombre = nombre

    # def get_Nombre(self, cursor, conn, _usuario, _password):
    #     cursor.execute('select  du.nombre, du.apellido, du.razon_social	from usuario us	join datos_usuario du on us.id = du.usuario_id join cuenta ca on ca.usuario_id = us.id where lg.nombre_usuario=%s',(_usuario))
    #     password=cursor.fetchall()
    #     print(password)
    #     conn.commit()
    #     return password[1]

    def validar_login(cursor, conn, _usuario, _password):
        validacion = []
        cursor.execute("select lg.nombre_usuario, lg.password, us.id, us.estado, tu.usuario_tipo from login lg join usuario us on lg.usuario_id = us.id join tipo_usuario tu on tu.id = us.tipo_usuario_id  where lg.nombre_usuario=%s",(_usuario))
        password=cursor.fetchall()
        conn.commit()
        try: 
            if password[0][0] == _usuario and password[0][1] == _password:
                validacion.append(1)
                validacion.append(password)
                return validacion
            else:
                validacion = [0]
                return validacion
        except Exception as e:
            print("Exception Occured while code Execution: "+ str(e))
            validacion = [0]
            return ('/views/login.html')

    def validar_administrador(cursor, conn,id_usuario_login):
        cursor.execute("select lg.nombre_usuario, lg.password, us.id, us.estado, tu.usuario_tipo from login lg join usuario us on lg.usuario_id = us.id join tipo_usuario tu on tu.id = us.tipo_usuario_id where us.id=%s",(id_usuario_login))
        datos_usuario=cursor.fetchall()
        conn.commit()
        if (datos_usuario[0][4]) != 'Administrador':
            return False
        else :
            return True



