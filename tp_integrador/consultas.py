import mysql.connector

class Banco:
    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user = "root", passwd = "", database = "sistema_banco")

    def __str__(self):
        datos = self.consulta()
        # i = ""
        # for row in datos:
        #     i = i + str(row) + "\n"
        # return i
        return print(datos)

    def consulta(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM 'cliente'")
        datos = cur.nombre()
        cur.close()
        return datos


banco = Banco()
print(banco.consulta)


