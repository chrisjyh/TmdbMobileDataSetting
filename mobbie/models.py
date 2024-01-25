from django.db import models

# Create your models here.
class MovieInfo(models.Model):
    movie_id = models.AutoField(primary_key=True)
    original_title = models.CharField(max_length=500,default='')
    title = models.CharField(max_length=500,default='')
    post = models.TextField(default='')
    genre = models.CharField(max_length=100,default='')
    summary = models.TextField(default='')
    grade = models.FloatField(default=0)
    release_date = models.DateField(default='')
    reg_date = models.DateField(default='')
    surver_id = models.TextField(default="")

    class Meta:
        db_table = 'movie_info'
        verbose_name = verbose_name_plural = "영화정보"

class UserInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(default='')
    password = models.CharField(max_length=100,default='')
    nick_name = models.CharField(max_length=200,default='')
    reg_date = models.DateField(default='')

    class Meta:
        db_table = 'user_info'
        verbose_name = verbose_name_plural = "사용자정보"

