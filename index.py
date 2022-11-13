"""CinemarAPI 
@author: Pablo Sandoval
"""

from flask import Flask
# import requests
app = Flask(__name__)
key = '1f54bd990f1cdfb230adb312546d765d'

@app.route('/movies', methods=['GET'])
def get_movies():
    # response = requests.get(f'https://api.themoviedb.org/3/movie/now_playing?api_key={key}&language=en-US')
    return 'response.json()'

@app.route('/movies/<int:index>', methods=['GET'])
def get_movie(index):
    # response = requests.get(f'https://api.themoviedb.org/3/movie/{str(index)}?api_key={key}&language=en-US')
    return 'response.json()'


# app.run(debug=True)