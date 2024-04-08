# Generated by Django 2.2.13 on 2021-01-21 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boom', '0017_auto_20210119_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boom.Song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
