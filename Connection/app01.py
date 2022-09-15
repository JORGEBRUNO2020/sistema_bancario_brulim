from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")

def index():
    usuario_banco = "marce limi"

