from django.db import models

from django.db import models
from datetime import date


class obec(models.Model):
    erb = models.CharField(max_lenght=70)
    nazev = models.CharField(max_lenght=50)
    uri = models.CharField(max_lenght=50)

class album(models.Model):
    nazev = models.CharFiels(max_lenght=100)
    je_uvodni = models.IntegerField()
    ck_id_obec = models.ForeignKey ('obec', on_delete=models.CASCADE)

class foto(models.Model):
    datum = models.DateField(default=date.now)
    sirka = models.IntegerField()
    nazev_souboru = models.CharField(max_length= 70)
    popis = models.CharField()
    ck_id_album = models.ForeignKey('album', on_delete=models.CASCADE)


