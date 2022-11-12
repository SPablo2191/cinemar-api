from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'mil programadores'

@app.route('/gonza')
def index():
    return 'SIUUUUUUUUU'