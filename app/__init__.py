from flask import Flask
from config import Config
#from flask_pymongo import PyMongo

def create_app(object_name=Config):
    app = Flask(__name__)
    app.config.from_object(object_name)
    #mongo = PyMongo(app)

    return app

app = create_app()

from app import routes, errors
