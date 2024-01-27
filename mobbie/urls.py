from django.urls import path
from . import views

urlpatterns = [
    path("", views.getMovie, name="getMovie"),
    path("insert/", views.insertMovie, name="insertMovie"),
    path("genre/", views.insertGenre, name="insertGenre"),
    path("review/", views.insertReview, name="insertReview"),
]
