# Generated by Django 3.0.8 on 2020-08-07 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battleship', '0005_gamemoves_turn'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamemoves',
            name='eSunk',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='gamemoves',
            name='pSunk',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]