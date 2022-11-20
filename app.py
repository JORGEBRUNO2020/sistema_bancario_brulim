import mysql.connector
from flask import Flask
from flask import render_template,request,redirect
from flaskext.mysql import MySQL
from datetime import datetime
from flask import send_from_directory
import os
from templates.models.usuarios import *
from templates.models.banco import *
from templates.models.caja_ahorro_comun import *
from templates.models.cuentas import *
from templates.models.administrador import *
from templates.models.cuenta_corriente import*
from templates.models.cuenta_corriente_dolares import*
from app_administrador import app_administrador
from database import mysql


app= Flask(__name__, static_url_path='/static')
app.register_blueprint(app_administrador, url_prefix="")

global id_usuario_login
id_usuario_login = []



#Conexión con base de datos
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema_bancario'
mysql.init_app(app)

carpeta_imagenes = os.path.join('/templates/images')
app.config['carpeta_imagenes'] = carpeta_imagenes


def valor_variable(id):
    id_usuario_login.append(id)
    return id_usuario_login[0]
    

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
    del id_usuario_login[:]
    _usuario = request.form['txt_usuario'] 
    _password = request.form['txt_password'] 
    conn= mysql.connect()
    cursor=conn.cursor()
    valido = Banco.validar_login(cursor, conn, _usuario, _password)
    try:
        if valido[0] == 1 and valido[1][0][4] != 'Administrador':
            valor_variable(valido[1][0][2])
            return render_template('/views/main_page.html')
        if valido[0] == 1 and valido[1][0][4] == 'Administrador':
            valor_variable(valido[1][0][2])
            return render_template('/views/administrador_main.html')
        if valido[0] != 1:
             return render_template('/views/login.html')
    except Exception as e:
        print("Exception Occured while code Execution: "+ str(e))
        return render_template('/views/login.html')

#Lanza página crear_cuenta.html
@app.route('/crear_cuenta', methods=['GET'])
def crear_cuenta():
    return render_template('/views/crear_cuenta.html')

@app.route('/crear_cuenta_caja_ahorro', methods=['GET'])
def crear_cuenta_caja_ahorro():
    conn= mysql.connect()
    caja_ahorro_com=conn.cursor()
    Caja_ahorro_comun.set_crear_cuenta_caja_ahorro(caja_ahorro_com ,conn, id_usuario_login[0])

    return render_template('/views/main_page.html')

@app.route('/volver', methods=['GET'])
def volver():
    return render_template('/views/main_page.html')

@app.route('/crear_cuenta_corriente_pesos', methods=['GET'])
def crear_cuenta_corriente_pesos():
    conn= mysql.connect()
    cuenta_corriente_pesos=conn.cursor()
    Cuenta_corriente.set_crear_cuenta_corriente_pesos(cuenta_corriente_pesos ,conn, id_usuario_login[0])
    return render_template('/views/main_page.html')

@app.route('/crear_cuenta_corriente_dolares', methods=['GET'])
def crear_cuenta_corriente_dolares():
    conn= mysql.connect()
    cuenta_corriente_pesos=conn.cursor()
    Cuenta_corriente_dolares.set_crear_cuenta_corriente_dolares(cuenta_corriente_pesos ,conn, id_usuario_login[0])
    return render_template('/views/main_page.html')

#Lanza página listar_cuentas.html
@app.route('/listar_cuentas', methods=['GET'])
def listar_cuentas():
    conn= mysql.connect()
    listar_cuentas=conn.cursor()
    listado_cuentas=Cuenta.get_cuentas(listar_cuentas, conn, id_usuario_login[0])
    
    return render_template('/views/listar_cuentas.html',listado_cuentas=listado_cuentas )

#Lanza página listar_movimientos.html
@app.route('/listar_movimientos', methods=['POST','GET'])
def listar_movimientos():
    conn= mysql.connect()
    listar_movimientos=conn.cursor()
    listado_movimientos=Caja_ahorro_comun.get_movimientos(listar_movimientos, conn, id_usuario_login[0])
    try:
        if request.method == 'POST':
            cuenta_movimiento = request.form["cuenta_movimiento"]
            id_cuenta = Caja_ahorro_comun.get_id_cuenta(cuenta_movimiento)
            movimientos_resultados = Caja_ahorro_comun.get_listado_movimientos(listado_movimientos,id_cuenta,)
        return render_template('/views/listar_movimientos_resultados.html',movimientos_resultados=movimientos_resultados)
    except Exception as e:
        print("Exception Occured while code Execution: "+ str(e))
        return render_template('/views/listar_movimientos.html')


@app.route('/realizar_deposito/<int:id>', methods = ['POST','GET'])
def realizar_deposito(id):
    
    print("Cuenta" ,id)
    if request.method == 'POST':
        _monto = request.form['depositar']
        conn= mysql.connect()
        mod_saldo=conn.cursor()
        Caja_ahorro_comun.set_saldo(mod_saldo, conn, id_usuario_login[0],id, _monto)
        return render_template('/views/main_page.html')
    else:
        return render_template('/views/main_page.html')
    
#Lanza página listar_saldos.html
@app.route('/listar_saldos', methods=['GET'])
def listar_saldos():
    conn= mysql.connect()
    listar_saldos=conn.cursor()
    cuentas_datos=Caja_ahorro_comun.get_saldo(listar_saldos, conn, id_usuario_login[0])
    return render_template('/views/listar_saldos.html',cuentas_datos=cuentas_datos )

#Lanza página realizar_retiro.html
@app.route('/realizar_retiro/<int:id>', methods=['GET','POST'])
def realizar_retiro(id):
    print("Cuenta" ,id)
    if request.method == 'POST':
        _monto = request.form['retirar']
        _monto = 0-int(_monto)
        conn= mysql.connect()
        mod_saldo=conn.cursor()
        Caja_ahorro_comun.set_saldo(mod_saldo, conn, id_usuario_login[0],id, _monto)
        return render_template('/views/main_page.html')
    else:
        return render_template('/views/main_page.html')

#Lanza página realizar_transferencial.html
@app.route('/realizar_transferencia')
def realizar_transferencia():
    return render_template('/views/realizar_transferencia.html')

#Lanza página cerrar_cuenta.html
@app.route('/cerrar_cuenta')
def cerrar_cuenta():
    return render_template('/views/cerrar_cuenta.html')

#Lanza página administrador_cargar_cliente_individuo.html
@app.route('/administrador_cargar_cliente_individuo', methods =['GET','POST']) 
def administrador_cargar_cliente_individuo():  
    conn= mysql.connect()
    cursor=conn.cursor()
    if Banco.validar_administrador(cursor, conn,id_usuario_login) == False: 
        return render_template('/views/login.html')
    if  request.method == 'POST':
        _cuitcuil = request.form['cuit_cuil']
        _dni = request.form['dni']
        _nombre = request.form['nombre']
        _apellido = request.form['apellido']
        _telefono = request.form['telefono']
        _email = request.form['email']
        _nombre_usuario = request.form['usuario']
        _password = request.form['password']
        try:
            # if Banco.validar_administrador(cursor, conn,id_usuario_login): 
                conn = mysql.connect()
                cargar_individuo = conn.cursor()
                Administrador.set_usuario(conn, cargar_individuo, 1)
                Administrador.set_datos_cliente_individuo(conn, cargar_individuo, _cuitcuil, _dni, _nombre, _apellido, _telefono, _email)
                Administrador.set_login(conn, cargar_individuo, _nombre_usuario, _password)
                return render_template('/views/administrador_cargar_cliente_individuo.html')
            # else:
            #     return render_template('/views/login.html')
        except Exception as e:
            print("Exception Occured while code Execution: "+ str(e))
            return render_template('/views/administrador_cargar_cliente_individuo.html')
    else:
        return render_template('/views/administrador_cargar_cliente_individuo.html')
    

@app.route('/route_name')
def method_name():
    pass





#Lanza página administrador_cargar_cliente_pyme.html
@app.route('/administrador_cargar_cliente_pyme', methods =['GET','POST'])
def administrador_cargar_cliente_pyme():
    conn= mysql.connect()
    cursor=conn.cursor()
    if Banco.validar_administrador(cursor, conn,id_usuario_login) == False: 
        return render_template('/views/login.html')
    if  request.method == 'POST':
        _cuitcuil = request.form['cuit_cuil']
        _razon_social = request.form['razon_social']
        _telefono = request.form['telefono']
        _email = request.form['email']
        _nombre_usuario = request.form['usuario']
        _password = request.form['password']
        conn = mysql.connect()
        cargar_pyme = conn.cursor()
        Administrador.set_usuario(conn, cargar_pyme, 2)
        Administrador.set_datos_cliente_pyme(conn, cargar_pyme, _cuitcuil, _razon_social, _telefono, _email)
        Administrador.set_login(conn, cargar_pyme, _nombre_usuario, _password)
        return render_template('/views/administrador_cargar_cliente_pyme.html')
    else:
        return render_template('/views/administrador_cargar_cliente_pyme.html')



#Execute APP
if __name__== '__main__':
    app.run(debug=True)



