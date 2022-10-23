from flask import Flask
from flask import render_template,request,redirect
from flaskext.mysql import MySQL
from datetime import datetime
from flask import send_from_directory
import os
from templates.clases.usuarios import *
from templates.clases.banco import *
from templates.clases.caja_ahorro_comun import *




app= Flask(__name__, static_url_path='/static')



#Conexión con base de datos
mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema_bancario'
mysql.init_app(app)

carpeta_imagenes = os.path.join('/templates/images')
app.config['carpeta_imagenes'] = carpeta_imagenes


@app.route('/carpeta_imagenes/<nombre_imagen>')
def get_imagen(nombre_imagen):
    return send_from_directory(app.config['carpeta_imagenes'], nombre_imagen)

#Lanza página index.html
@app.route('/')
def index():
    return render_template('views/index.html')

#Lanza página pagina_login.html
@app.route('/pagina_login')
def pagina_login():
    return render_template('views/login.html')

#Método POST verifica usuario/contraseña
@app.route('/login', methods=['POST'])
def login():
    _usuario = request.form['txt_usuario'] 
    _password = request.form['txt_password'] 
    conn= mysql.connect()
    cursor=conn.cursor()
    valido = Banco.validar_login(cursor, conn, _usuario, _password)
    if valido:
        return render_template('/views/main_page.html')
    else:
        return render_template('/views/login.html')
        

#Lanza página crear_cuenta.html
@app.route('/crear_cuenta')
def crear_cuenta():
    return render_template('/views/crear_cuenta.html')


#Lanza página listar_cuentas.html
@app.route('/listar_cuentas')
def listar_cuentas():
    return render_template('/views/listar_cuentas.html')


#Lanza página listar_movimientos.html
@app.route('/listar_movimientos')
def listar_movimientos():
    return render_template('/views/listar_movimientos.html')


#Lanza página listar_saldos.html
@app.route('/listar_saldos')
def listar_saldos():
    conn= mysql.connect()
    cursor=conn.cursor()
    Caja_ahorro_comun.get_saldo(cursor, conn, 1, 1, 1)
    return render_template('/views/listar_saldos.html')


#Lanza página realizar_deposito.html
@app.route('/realizar_deposito')
def realizar_deposito():
    return render_template('/views/realizar_deposito.html')


#Lanza página realizar_transferencial.html
@app.route('/realizar_transferencia')
def realizar_transferencia():
    return render_template('/views/realizar_transferencia.html')


#Lanza página realizar_retiro.html
@app.route('/realizar_retiro')
def realizar_retiro():
    return render_template('/views/realizar_retiro.html')

#Lanza página cerrar_cuenta.html
@app.route('/cerrar_cuenta')
def cerrar_cuenta():
    return render_template('/views/cerrar_cuenta.html')







#Execute APP
if __name__== '__main__':
    app.run(debug=True)



