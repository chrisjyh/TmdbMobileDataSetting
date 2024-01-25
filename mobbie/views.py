import datetime

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests

from mobbie.models import MovieInfo

from datetime import datetime, timedelta


# Create your views here.
def getMovie(request):
    total_data = []
    TMDB_API_KEY = "2a177f23d9a8339ceb122cc1752dcdc0"

    # 1페이지부터 500페이지까지의 데이터를 가져옴.
    for i in range(1, 2):
        request_url = f"https://api.themoviedb.org/3/movie/popular?language=ko&region=ko&api_key={TMDB_API_KEY}&page={i}"
        movies = requests.get(request_url).json()
        total_data = total_data + movies['results']

    for data in total_data:
        data['title']

    return render(request, "mobbie/mobbie.html", {"total_data": total_data})


def insertMovie(request):
    total_data = []
    TMDB_API_KEY = "2a177f23d9a8339ceb122cc1752dcdc0"

    # 1페이지부터 500페이지까지의 데이터를 가져옴.
    for i in range(1, 100):
        request_url = f"https://api.themoviedb.org/3/movie/popular?language=ko&region=ko&api_key={TMDB_API_KEY}&page={i}"
        movies = requests.get(request_url).json()
        total_data = total_data + movies['results']

    yesterday = datetime.today() - timedelta(1)

    for data in total_data:
        movie_db = MovieInfo()
        if not MovieInfo.objects.filter(surver_id=data['id']).exists():
            movie_db.surver_id = data['id']
            movie_db.original_title = data['original_title']
            movie_db.title = data['title']
            movie_db.post = data['poster_path']
            movie_db.genre = data['genre_ids']
            movie_db.summary = data['overview']
            movie_db.grade = data['vote_average']
            movie_db.release_date = data['release_date']
            movie_db.reg_date = yesterday
            movie_db.save()
        else:
            print(f"already: ${data['id']}")

    return HttpResponse("success")
