"""
CinemarAPI 
@author: Pablo Sandoval
"""
from flask import Flask
from flask_cors import CORS
from resources.movie import movies
from resources.show import shows
from resources.room import rooms
from resources.reservation import reservations
from resources.home import home
app = Flask(__name__)
CORS(app)
# HOME route
app.register_blueprint(home)
# Movies routes
app.register_blueprint(movies)
# Shows routes
app.register_blueprint(shows)
# Rooms routes
app.register_blueprint(rooms)
# Reservations routes
app.register_blueprint(reservations)


# app.run(debug=True)