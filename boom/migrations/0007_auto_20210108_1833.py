# Generated by Django 2.2.13 on 2021-01-08 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boom', '0006_auto_20210107_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.CharField(max_length=200)),
                ('song_name', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
                ('song_file', models.FileField(blank=True, upload_to='songs/')),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]
