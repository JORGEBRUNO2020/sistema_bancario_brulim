


class Banco():
    

    def __init__(self, nombre):
        self.__nombre = nombre

    def get_Nombre(self):
        return self.__nombre

    def validar_login(cursor, conn, _usuario, _password):
        validacion = []
        cursor.execute("select * from login where nombre_usuario=%s",(_usuario))
        password=cursor.fetchall()
        conn.commit()
        try: 
            if password[0][0] == _usuario and password[0][1] == _password:
                
                validacion = [1,[password[0][2]]]
                
                return validacion
            else:
                validacion = [0]
                return validacion
        except Exception as e:
            print("Exception Occured while code Execution: "+ str(e))
            validacion = [0]
            ruta = ('/views/login.html')
            return  ruta

    #def asignar_usuario

# banco = Banco("Brulim")

# # print(banco.get_Nombre())