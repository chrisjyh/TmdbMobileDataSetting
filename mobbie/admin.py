from django.contrib import admin

from mobbie.models import MovieInfo, UserInfo, Gengre, Review


# Register your models

@admin.register(MovieInfo)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date']

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = [ 'user_id', 'nick_name', 'email']

@admin.register(Gengre)
class GengreAdmin(admin.ModelAdmin):
    list_display = ['genre_name', 'genre_id']


@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ['title', 'user_id']