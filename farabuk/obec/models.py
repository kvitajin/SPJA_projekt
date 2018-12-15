from django.db import models

from django.db import models
from datetime import date


class Obec(models.Model):
    erb = models.CharField(max_lenght=70)
    nazev = models.CharField(max_lenght=50)
    uri = models.CharField(max_lenght=50)


class Album(models.Model):
    nazev = models.CharFiel(max_lenght=100)
    je_uvodni = models.IntegerField()
    ck_id_obec = models.ForeignKey ('Obec', on_delete=models.CASCADE)


class Foto(models.Model):
    datum = models.DateField(default=date.now)
    sirka = models.IntegerField()
    nazev_souboru = models.CharField(max_length=70)
    popis = models.CharField()
    ck_id_album = models.ForeignKey('Album', on_delete=models.CASCADE)


class Dokument(models.Model):
    nadpis = models.CharField()
    uri = models.CharField()
    obsah = models.CharField()
    datum_stazeni = models.DateField()
    obrazek = models.CharField()
    ck_id_obec = models.ForeignKey('Obec', on_delete=models.CASCADE)


class Uzivatel(models.Model):
    nick = models.CharField()
    heslo = models.CharField()
    emial = models.CharField()
    datum_narozeni = models.DateField()
    ban = models.IntegerField()
    ck_id_obec = models.ForeignKey('Obec', on_delete=models.CASCADE)

class Komentar(models.Model):
    obsah = models.CharField(max_lenght=300)
    ck_id_uzivatel = models.ForeignKey('Uzivatel', on_delete=models.CASCADE)
    ck_id_dokument = models.ForeignKey('Dokument', on_delete=models.CASCADE)
    ck_id_foto = models.ForeignKey('Foto', on_delete=models.CASCADE)

