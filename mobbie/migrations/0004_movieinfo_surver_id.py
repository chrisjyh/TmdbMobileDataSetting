# Generated by Django 4.2.9 on 2024-01-23 11:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mobbie", "0003_movieinfo_grade_alter_movieinfo_genre_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="movieinfo",
            name="surver_id",
            field=models.TextField(default=""),
        ),
    ]