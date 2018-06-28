from flask import Flask
from config import Config
#from mygpio import gpio


app = Flask(__name__)
app.config.from_object(Config)


from app import routes