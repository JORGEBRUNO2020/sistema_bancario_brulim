class Banco():
    

    def __init__(self, nombre):
        self.__nombre = nombre

    def get_Nombre(self):
        return self.__nombre

    def validar_login(cursor, conn, _usuario, _password):
        validacion = []
        cursor.execute("select lg.nombre_usuario, lg.password, us.id, us.estado, tu.usuario_tipo  from login lg join usuario us on lg.usuario_id = us.id join tipo_usuario tu on tu.id = us.id where lg.nombre_usuario=%s",(_usuario))
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


