from flask import Blueprint
home = Blueprint('home',__name__)
@home.route('/', methods=['GET'])
def index():
    return {
        'greeting' : 'Bienvenido a la API de CINEMAR - MIL PROGRAMADORES PYTHON 2022🐍',
        'author' : 'Pablo Sandoval🐱‍🚀'
    }