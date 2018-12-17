# Generated by Django 2.1.3 on 2018-12-17 14:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=100)),
                ('je_uvodni', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dokument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nadpis', models.CharField(max_length=100)),
                ('uri', models.CharField(max_length=150)),
                ('obsah', models.TextField()),
                ('datum_pridani', models.DateField(default=datetime.date.today)),
                ('obrazek', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datum', models.DateField(default=datetime.date.today)),
                ('sirka', models.IntegerField(blank=True, default=0)),
                ('nazev_souboru', models.CharField(max_length=70)),
                ('soubor', models.ImageField(blank=True, upload_to='')),
                ('popis', models.CharField(blank=True, max_length=150)),
                ('ck_id_album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obec.Album')),
            ],
        ),
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obsah', models.TextField()),
                ('ck_id_dokument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obec.Dokument')),
                ('ck_id_foto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obec.Foto')),
            ],
        ),
        migrations.CreateModel(
            name='Obec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('erb', models.ImageField(upload_to='')),
                ('nazev', models.CharField(max_length=50)),
                ('uri', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Uzivatel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick', models.CharField(max_length=50)),
                ('heslo', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=100)),
                ('datum_narozeni', models.DateField()),
                ('ban', models.IntegerField(default=0)),
                ('ck_id_obec', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obec.Obec')),
            ],
        ),
        migrations.AddField(
            model_name='komentar',
            name='ck_id_uzivatel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obec.Uzivatel'),
        ),
        migrations.AddField(
            model_name='dokument',
            name='ck_id_obec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obec.Obec'),
        ),
        migrations.AddField(
            model_name='album',
            name='ck_id_obec',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obec.Obec'),
        ),
    ]
