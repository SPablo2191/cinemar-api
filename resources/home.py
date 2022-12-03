from flask import Blueprint,g
from database.db import dbQuery
home = Blueprint('home',__name__)

DATABASE = 'database\database.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = dbQuery(DATABASE)
    return db


@home.route('/', methods=['GET'])
def index():
    return {
        'greeting' : 'Bienvenido a la API de CINEMAR - MIL PROGRAMADORES PYTHON 2022🐍',
        'author' : 'Pablo Sandoval🐱‍🚀'
    }