class Banco():

    def __init__(self, nombre):
        self.nombre = nombre

    def validar_login(cursor, conn, _usuario, _password):
        cursor.execute("select * from login where nombre_usuario=%s",(_usuario))
        password=cursor.fetchall()
        conn.commit()
        try: 
            if password[0][0] == _usuario and password[0][1] == _password:
                return True
            else:
                return False
        except Exception as e:
            print("Exception Occured while code Execution: "+ str(e))
            return False