"""
CinemarAPI 
@author: Pablo Sandoval

"""
from flask import Flask,g
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from resources.movie import movies
from resources.show import shows
from resources.room import rooms
from resources.reservation import reservations
from resources.home import home
from resources.user import users
from resources.discount import discounts
app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = 't1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'
jwt = JWTManager(app)
CORS(app)
@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

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
# Users routes
app.register_blueprint(users)
# Discounts routes
app.register_blueprint(discounts)
app.run(debug=True)