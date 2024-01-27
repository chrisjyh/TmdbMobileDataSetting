from django.db import models


# Create your models here.
class MovieInfo(models.Model):
    movie_id = models.AutoField(primary_key=True)
    original_title = models.CharField(max_length=500, default='')
    title = models.CharField(max_length=500, default='')
    post = models.TextField(default='')
    genre_id = models.CharField(max_length=100, default='')
    summary = models.TextField(default='')
    grade = models.FloatField(default=0)
    vote_count = models.IntegerField(default=0)
    release_date = models.DateField(blank=True, null=True)
    reg_date = models.DateField(blank=True, null=True)
    tmdb_id = models.TextField(default='', blank=True, null=True)

    class Meta:
        db_table = 'movie_info'
        verbose_name = verbose_name_plural = "영화정보"


class UserInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(default='')
    password = models.CharField(max_length=100, default='')
    nick_name = models.CharField(max_length=200, default='')
    reg_date = models.DateField(default='')

    class Meta:
        db_table = 'user_info'
        verbose_name = verbose_name_plural = "사용자정보"


class Gengre(models.Model):
    genre_id = models.IntegerField(default='')
    genre_name = models.CharField(max_length=20)

    class Meta:
        db_table = 'genre_info'


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, default='')
    content = models.TextField(default='')
    grade = models.FloatField(default=0)
    reg_date = models.DateField(default='')
    user_id = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    movie_id = models.ForeignKey('MovieInfo', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'review'


class history(models.Model):
    history_id = models.AutoField(primary_key=True)
    reg_date = models.DateField(default='')
    review_id = models.ForeignKey('Review', on_delete=models.CASCADE)

    class Meta:
        db_table = 'history'


class review_like(models.Model):
    user_id = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    review_id = models.ForeignKey('Review', on_delete=models.CASCADE, null=True)
    reg_date = models.DateField(default='')
    status = models.IntegerField(default=0)

    class Meta:
        db_table = 'review_like'


class movie_like(models.Model):
    user_id = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
    movie_id = models.ForeignKey('MovieInfo', on_delete=models.CASCADE)
    reg_date = models.DateField(default='')
    status = models.IntegerField(default=0)

    class Meta:
        db_table = 'movie_like'
