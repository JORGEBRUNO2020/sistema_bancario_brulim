from flask import Flask
from flask import render_template,request,redirect
from flaskext.mysql import MySQL
from datetime import datetime
from flask import send_from_directory
import os

def conexion(app):
    # app= Flask(__name__, static_url_path='/static')

    mysql= MySQL()
    app.config['MYSQL_DATABASE_HOST']='localhost'
    app.config['MYSQL_DATABASE_USER']='root'
    app.config['MYSQL_DATABASE_PASSWORD']=''
    app.config['MYSQL_DATABASE_DB']='sistema_bancario'
    bbdd =  mysql.init_app(app)
    return bbdd