# Generated by Django 4.1.3 on 2022-11-16 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_album_artist_song_album_song_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('songs', models.ManyToManyField(to='music.song')),
            ],
        ),
    ]
