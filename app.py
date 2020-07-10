from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'

from views import *

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

def Imprimir(mensagem):
    print(mensagem)
    os.system(mensagem)
    return 0
    

if __name__ == '__main__':
    app.run()