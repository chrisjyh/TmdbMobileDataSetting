# Generated by Django 4.2.9 on 2024-01-25 10:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mobbie", "0006_gengre_alter_movieinfo_reg_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movieinfo",
            name="reg_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="movieinfo",
            name="release_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="movieinfo",
            name="surver_id",
            field=models.TextField(blank=True, default="", null=True),
        ),
    ]
