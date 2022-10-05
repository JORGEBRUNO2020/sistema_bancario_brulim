
from distutils.command.config import config
from flask import Flask, render_template
from flaskext.mysql import MySQL


app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template()


# if __name__== '__main__':
#     app.config.from_object(config['development'])



# mysql = MySQL()
# app.config['MYSQL_DATABASE_HOST']='localhost'
# app.config['MYSQL_DATABASE_USER']='root'
# app.config['MYSQL_DATABASE_PASSWORD']=''
# app.config['MYSQL_DATABASE_DB']='sistema_bancario_create'
# mysql.init_app(app)



@app.route('/')
def index():

    # sql = "select * from datos_usuario"
    # conn = mysql.connect()
    # cursor = conn.cursor()
    # cursor.execute(sql)
    # conn.commit()

    return render_template('sistema_bancario_brulim/index.html')

if __name__ == '__main__':
    app.run(debug=True)