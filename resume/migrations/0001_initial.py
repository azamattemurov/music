# Generated by Django 5.0.7 on 2024-12-06 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=200)),
                ('artist_name', models.CharField(max_length=200)),
                ('album_thumbnail', models.ImageField(blank=True, null=True, upload_to='album_thumbnails/')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to='songs/')),
                ('download_count', models.IntegerField(default=0)),
            ],
        ),
    ]
