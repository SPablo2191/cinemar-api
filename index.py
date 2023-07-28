"""CinemarAPI 
@author: Pablo Sandoval
"""
from flask import Flask
from flask_cors import CORS
from resources.movie import movies
from resources.room import rooms

app = Flask(__name__)
CORS(app)
# Movies routes
app.register_blueprint(movies)
# Rooms routes
app.register_blueprint(rooms)

if __name__ == "__main__":
    app.run(debug=True)
