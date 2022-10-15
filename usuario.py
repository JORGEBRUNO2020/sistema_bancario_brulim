from flaskext.mysql import MySQL
from conexion import *


class Usuario():

    def __init__(self,nombre_us, password):
        self.nombre_us = nombre_us
        self.password = password
  
    def validar_login(us, log, cursor, con, bbdd):
        conn= bbdd.connect()

        cursor=conn.cursor()
        cursor.execute("select * from login where nombre_usuario=%s",(us))
        password=cursor.fetchall()
        con.commit()
        if password[0][1] == log:
            correcto = True
        else: 
            correcto = False
        return correcto
        
        
        

 