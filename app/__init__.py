from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY']= 'cu_cu'

from app import routes