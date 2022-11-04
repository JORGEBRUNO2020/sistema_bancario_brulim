import mysql.connector
from flask import Flask
from templates.models.usuarios import *
from templates.models.banco import *
from templates.models.caja_ahorro_comun import *
from templates.models.cuentas import *
from templates.models.administrador import *
from templates.models.cuenta_corriente import*
from flask import Blueprint, render_template
from database import mysql

app_administrador = Blueprint("app_administrador", __name__, static_folder="static", template_folder="template")


# Routeos del administrador
#Lanza página administrador_main.html
@app_administrador.route('/administrador_header')
def administrador():
    return render_template('/views/administrador_main.html')

#Lanza página administrador_listar_saldos.html
@app_administrador.route('/administrador_listar_saldos', methods=['GET'])
def listar_todos_los_saldos():
    conn= mysql.connect()
    listar_todos_saldos=conn.cursor()
    listado_todos_saldos=Cuenta.get_todos_los_saldos(listar_todos_saldos, conn)
    return render_template('/views/administrador_listar_saldos.html',listado_todos_saldos=listado_todos_saldos )

#Lanza página administrador_listar_cuentas.html
@app_administrador.route('/administrador_listar_cuentas', methods=['GET'])
def administrador_listar_cuentas():
    conn= mysql.connect()
    listar_todas_cuentas=conn.cursor()
    listado_todas_cuentas= Administrador.get_todas_cuentas(listar_todas_cuentas, conn)
    return render_template('/views/administrador_listar_cuentas.html', listado_todas_cuentas=listado_todas_cuentas)

#Lanza página administrador_listar_usuarios.html
@app_administrador.route('/administrador_listar_usuarios', methods=['GET'])
def administrador_listar_usuarios():
    conn= mysql.connect()
    listar_usuarios=conn.cursor()
    listado_usuarios=Usuario.get_usuarios(listar_usuarios, conn)
    return render_template('/views/administrador_listar_usuarios.html', listado_usuarios = listado_usuarios)

#Lanza página administrador_listar_movimientos.html
@app_administrador.route('/administrador_listar_movimientos')
def administrador_listar_movimientos():
    return render_template('/views/administrador_listar_movimientos.html')

#Lanza página administrador_modificar_datos_cliente.html
@app_administrador.route('/administrador_modificar_datos_cliente')
def administrador_modificar_datos_cliente():
    return render_template('/views/administrador_modificar_datos_cliente.html')

#Lanza página administrador_ver_comisiones.html
@app_administrador.route('/administrador_ver_comisiones')
def administrador_ver_comisiones():
    return render_template('/views/administrador_ver_comisiones.html')

#Lanza página index.html para salir
@app_administrador.route('/login')
def administrador_salir():
    return render_template('views/login.html')
