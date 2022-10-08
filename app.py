from flask import Flask
from flask import render_template,request,redirect
from flaskext.mysql import MySQL
from datetime import datetime


app= Flask(__name__)

mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='sistema_bancario'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('views/index.html')


@app.route('/pagina_login')
def pagina_login():
    return render_template('views/login.html')


@app.route('/login', methods=['POST'])
def login():
    _usuario = request.form['txt_usuario'] 
    _password = request.form['txt_password'] 
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute("select * from login where nombre_usuario=%s",(_usuario))
    password=cursor.fetchall()
    conn.commit()
    print(password)
    print(_password)
    if password[0][1] == _password:
        return render_template('/views/main_page.html')
    else:
        return render_template('/views/login.html')






#Execute APP
if __name__== '__main__':
    app.run(debug=True)



