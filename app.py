from flask import Flask
from flask import render_template,request,redirect
from flaskext.mysql import MySQL
from datetime import datetime
from flask import send_from_directory
import os


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
    cursor.execute("select * from login where nombre_usuario=%s",(_usuario))
    password=cursor.fetchall()
    conn.commit()
    try: 
        if password[0][0] == _usuario and password[0][1] == _password:
            return render_template('/views/main_page.html')
        else:
            return render_template('/views/login.html')
    except Exception as e:
        print("Exception Occured while code Execution: "+ str(e))
        return render_template('/views/login.html')
  
    
        







#Execute APP
if __name__== '__main__':
    app.run(debug=True)



