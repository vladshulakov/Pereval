# Generated by Django 4.2.7 on 2023-11-11 14:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import perevalapi.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(blank=True, max_length=9, verbose_name='широта')),
                ('longitude', models.FloatField(blank=True, max_length=9, verbose_name='долгота')),
                ('height', models.IntegerField(blank=True, verbose_name='высота')),
            ],
        ),
        migrations.CreateModel(
            name='Levels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(choices=[('', 'не указано'), ('1A', '1a'), ('1B', '1б'), ('2А', '2а'), ('2В', '2б'), ('3А', '3а'), ('3В', '3б')], default='', max_length=2, verbose_name='зима')),
                ('summer', models.CharField(choices=[('', 'не указано'), ('1A', '1a'), ('1B', '1б'), ('2А', '2а'), ('2В', '2б'), ('3А', '3а'), ('3В', '3б')], default='', max_length=2, verbose_name='лето')),
                ('autumn', models.CharField(choices=[('', 'не указано'), ('1A', '1a'), ('1B', '1б'), ('2А', '2а'), ('2В', '2б'), ('3А', '3а'), ('3В', '3б')], default='', max_length=2, verbose_name='осень')),
                ('spring', models.CharField(choices=[('', 'не указано'), ('1A', '1a'), ('1B', '1б'), ('2А', '2а'), ('2В', '2б'), ('3А', '3а'), ('3В', '3б')], default='', max_length=2, verbose_name='весна')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254, verbose_name='почта')),
                ('phone', models.CharField(max_length=15, verbose_name='телефон')),
                ('name', models.CharField(max_length=30, verbose_name='имя')),
                ('surname', models.CharField(max_length=30, verbose_name='фамилия')),
                ('otch', models.CharField(max_length=30, verbose_name='отчество')),
            ],
        ),
        migrations.CreateModel(
            name='PerevalAdded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('new', 'новый'), ('pending', 'на модерации'), ('accepted', 'принят'), ('rejected', 'не принят')], default='new', max_length=25)),
                ('beautyTitle', models.CharField(choices=[('poss', 'перевал'), ('mountain_peak', 'горная вершина'), ('gorge', 'ущелье'), ('plateau', 'плато')], max_length=50, verbose_name='тип')),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='название')),
                ('other_titles', models.CharField(max_length=50, verbose_name='иные названия')),
                ('connect', models.CharField(max_length=250, verbose_name='соединение')),
                ('add_time', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('coord_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='perevalapi.coords')),
                ('levels', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='perevalapi.levels')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perevalapi.users')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photos', models.ImageField(blank=True, null=True, upload_to=perevalapi.models.get_image_path, verbose_name='Фото')),
                ('pereval', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='perevalapi.perevaladded')),
            ],
        ),
    ]
