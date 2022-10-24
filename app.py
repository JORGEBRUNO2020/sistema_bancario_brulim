
from flask import Flask
from flask import render_template,request,redirect
from flaskext.mysql import MySQL
from datetime import datetime
from flask import send_from_directory
import os
from templates.clases.usuarios import *
from templates.clases.banco import *
from templates.clases.caja_ahorro_comun import *
from templates.clases.cuentas import *




app= Flask(__name__, static_url_path='/static')

global id_usuario_login
id_usuario_login = []



#Conexión con base de datos
mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema_bancario'
mysql.init_app(app)

carpeta_imagenes = os.path.join('/templates/images')
app.config['carpeta_imagenes'] = carpeta_imagenes


def valor_variable(id):
    id_usuario_login.append(id)
    return id_usuario_login
    

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
    # print(valido[1][0])
    if len(valido)>1:
        if valido[0] == 1 and valido[1][0] !=4:
            valor_variable(valido[1])
            return render_template('/views/main_page.html')
        elif valido[1][0] == 4:
            return render_template('/views/administrador_main.html')
        else:
            return render_template('/views/login.html')
    else:
        return render_template('/views/login.html')
        

#Lanza página crear_cuenta.html
@app.route('/crear_cuenta')
def crear_cuenta():
    return render_template('/views/crear_cuenta.html')


#Lanza página listar_cuentas.html
@app.route('/listar_cuentas', methods=['GET'])
def listar_cuentas():
    conn= mysql.connect()
    listar_cuentas=conn.cursor()
    listado_cuentas=Cuenta.get_cuentas(listar_cuentas, conn, id_usuario_login[0][0])
    return render_template('/views/listar_cuentas.html',listado_cuentas=listado_cuentas )



#Lanza página listar_movimientos.html
@app.route('/listar_movimientos')
def listar_movimientos():
    return render_template('/views/listar_movimientos.html')


#Lanza página listar_saldos.html
@app.route('/listar_saldos', methods=['GET'])
def listar_saldos():
    conn= mysql.connect()
    listar_saldos=conn.cursor()
    cuentas_datos=Caja_ahorro_comun.get_saldo(listar_saldos, conn, id_usuario_login[0][0])
    return render_template('/views/listar_saldos.html',cuentas_datos=cuentas_datos )


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

# Routeos del administrador
#Lanza página administrador_main.html
@app.route('/administrador_header')
def administrador():
    return render_template('/views/administrador_main.html')

#Lanza página administrador_cargar_cliente_individuo.html
@app.route('/administrador_cargar_cliente_individuo')
def administrador_cargar_cliente_individuo():
    return render_template('/views/administrador_cargar_cliente_individuo.html')

#Lanza página administrador_cargar_cliente_pyme.html
@app.route('/administrador_cargar_cliente_pyme')
def administrador_cargar_cliente_pyme():
    return render_template('/views/administrador_cargar_cliente_pyme.html')

#Lanza página administrador_listar_cuentas.html
@app.route('/administrador_listar_cuentas')
def administrador_listar_cuentas():
    return render_template('/views/administrador_listar_cuentas.html')

#Lanza página administrador_listar_saldos.html
@app.route('/administrador_listar_saldos')
def administrador_listar_saldos():
    return render_template('/views/administrador_listar_saldos.html')

#Lanza página administrador_listar_movimientos.html
@app.route('/administrador_listar_movimientos')
def administrador_listar_movimientos():
    return render_template('/views/administrador_listar_movimientos.html')

#Lanza página administrador_modificar_datos_cliente.html
@app.route('/administrador_modificar_datos_cliente')
def administrador_modificar_datos_cliente():
    return render_template('/views/administrador_modificar_datos_cliente.html')

#Lanza página administrador_ver_comisiones.html
@app.route('/administrador_ver_comisiones')
def administrador_ver_comisiones():
    return render_template('/views/administrador_ver_comisiones.html')

#Lanza página index.html para salir
@app.route('/login')
def administrador_salir():
    return render_template('views/login.html')

#Execute APP
if __name__== '__main__':
    app.run(debug=True)



