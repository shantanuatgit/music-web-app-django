# Generated by Django 2.2.13 on 2021-01-14 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boom', '0011_remove_playlist_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='song',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='boom.Song'),
        ),
    ]