from flask import Blueprint
import requests
movies = Blueprint('movies',__name__)
key = '1f54bd990f1cdfb230adb312546d765d'
@movies.route('/movies', methods=['GET'])
def get_movies():
    response = requests.get(f'https://api.themoviedb.org/3/movie/now_playing?api_key={key}&language=en-US')
    return response.json()

@movies.route('/movies/<int:index>', methods=['GET'])
def get_movie(index):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{str(index)}?api_key={key}&language=en-US')
    return response.json()