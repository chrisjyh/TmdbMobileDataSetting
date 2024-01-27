import datetime

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import requests

from mobbie.models import MovieInfo, Gengre

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
        if not MovieInfo.objects.filter(tmdb_id=data['id']).exists():
            movie_db.tmdb_id = data['id']
            movie_db.original_title = data['original_title']
            movie_db.title = data['title']
            movie_db.post = data['poster_path']
            movie_db.genre_id = data['genre_ids'][0] if len(data['genre_ids']) > 0 else 0
            movie_db.summary = data['overview']
            movie_db.grade = data['vote_average']
            movie_db.vote_count = data['vote_count']
            movie_db.release_date = data['release_date'] if data['release_date'] else "1111-11-11"
            movie_db.reg_date = yesterday if yesterday else "1111-11-11"
            movie_db.save()
        else:
            print(f"already: ${data['id']}")

    return HttpResponse("success")


def insertGenre(request):
    url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYTE3N2YyM2Q5YTgzMzljZWIxMjJjYzE3NTJkY2RjMCIsInN1YiI6IjY1YWY3NzRjYWFkOWMyMDBlYTkyMTQzYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.S4zey1AYtaY4ypI1Hko-9ZO08RkLz6g_JNb_5SOZzqk"
    }

    response = requests.get(url, headers=headers)

    for genre in response.json().get("genres"):
        genre_db = Gengre()
        if not Gengre.objects.filter(genre_id=genre.get('id')).exists():
            genre_db.genre_id = genre.get("id")
            genre_db.genre_name = genre.get("name")
            genre_db.save()

    return HttpResponse(response.text)

def insertReview(request):

    movie_list = MovieInfo.objects.all().filter().order_by('release_date')[:3]
    for i in movie_list:
        url = f"https://api.themoviedb.org/3/movie/{str(i.tmdb_id)}/reviews?language=en-US&page=1"
        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyYTE3N2YyM2Q5YTgzMzljZWIxMjJjYzE3NTJkY2RjMCIsInN1YiI6IjY1YWY3NzRjYWFkOWMyMDBlYTkyMTQzYiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.S4zey1AYtaY4ypI1Hko-9ZO08RkLz6g_JNb_5SOZzqk"
        }
        response = requests.get(url, headers=headers).json()
        if not response.get("results") == []:
            reviews = response.get('results')
            for review in reviews:
                print("xxxxxx")
                print(review.get('title'))
                print(review.get('author'))
                print(review.get('created_at'))

    return HttpResponse(response, content_type='text/plain')

