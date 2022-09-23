from flask import Flask, render_template
import mysql.connector

connection = mysql.connector.connect(host='localhost',
                                        database='sistema_bancario',
                                        user='root',
                                        password='')

sql_select_Query = "select * from sucursal"
cursor = connection.cursor()
cursor.execute(sql_select_Query)
# get all records
records = cursor.fetchall()

app = Flask(__name__)


@app.route("/")



def index():
    #usuario_banco = "marce limi"
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Apellido  = ", row[2])
        # print("Telefono  = ", row[4])
        # print("mail  = ", row[5])
        # print("Usuario  = ", row[6])
        # print("Password  = ", row[7],"\n")
    return row



if __name__ == "__main__":
    app.run()

