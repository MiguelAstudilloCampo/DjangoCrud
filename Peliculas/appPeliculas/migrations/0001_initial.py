# Generated by Django 5.0.4 on 2024-04-24 01:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gen_nombre', models.CharField(max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='peliculas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pel_codigo', models.CharField(max_length=10, unique=True)),
                ('pel_titulo', models.CharField(max_length=80)),
                ('pel_protagonista', models.CharField(max_length=80)),
                ('pel_duracion', models.IntegerField()),
                ('pel_sinopsis', models.CharField(max_length=2000)),
                ('pel_foto', models.ImageField(blank=True, null=True, upload_to='fotos/')),
                ('pel_genero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPeliculas.genero')),
            ],
        ),
    ]
