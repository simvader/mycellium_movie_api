# Generated by Django 4.1.2 on 2022-12-04 23:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('actors', models.ManyToManyField(to='movies.actor')),
                ('directors', models.ManyToManyField(to='movies.director')),
            ],
        ),
        migrations.CreateModel(
            name='MovieProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.movie')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.country')),
                ('seen_movies', models.ManyToManyField(through='movies.MovieProfile', to='movies.movie')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movieprofile',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.profile'),
        ),
        migrations.AddField(
            model_name='director',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.profile'),
        ),
        migrations.AddField(
            model_name='actor',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movies.profile'),
        ),
    ]
