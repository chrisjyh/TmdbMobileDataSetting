from django.contrib import admin

from mobbie.models import MovieInfo, UserInfo


# Register your models

@admin.register(MovieInfo)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date']

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = [ 'user_id', 'nick_name', 'email']