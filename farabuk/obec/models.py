from django.db import models

from django.db import models
from datetime import datetime

# blank = True - nepovinný parametr
# ImageField - Spceciální field pro fotky
# FileField - field pro soubory
# TextField - pro více textu

class Obec(models.Model):
    erb = models.CharField(max_length=70)
    nazev = models.CharField(max_length=50)
    uri = models.CharField(max_length=50)

    def __str__(self):
        return "{} {} {}".format(self.nazev, self.erb, self.uri)


class Album(models.Model):
    nazev = models.CharField(max_length=100)
    je_uvodni = models.IntegerField(blank = True)
    ck_id_obec = models.ForeignKey ('Obec', on_delete=models.CASCADE)

    def __str__(self):
        return "{}{}{}".format(self.ck_id_obec.nazev, self.nazev, self.je_uvodni)


class Foto(models.Model):
    datum = models.DateField(auto_now_add = True) # auto_now_add = True
    sirka = models.IntegerField(blank = True)
    nazev_souboru = models.CharField(max_length=70)
    soubor = models.ImageField(blank = True)
    popis = models.CharField(max_length=150, blank = True)
    ck_id_album = models.ForeignKey('Album', on_delete=models.CASCADE)

    def __str__(self):
        return "{}{}{}{}{}".format(self.ck_id_album.nazev, self.datum, self.sirka, self.nazev_souboru, self.popis)


class Dokument(models.Model):
    nadpis = models.CharField(max_length=100)
    uri = models.CharField(max_length=150)
    obsah = models.TextField()
    datum_pridani = models.DateField(default = datetime.now)
    obrazek = models.ImageField(blank = True)
    ck_id_obec = models.ForeignKey('Obec', on_delete=models.CASCADE)

    def __str__(self):
        return "{}{}{}{}{}{}".format(self.ck_id_obec.nazev, self.nadpis, self.uri, self.obsah, self.datum_stazeni, self.obrazek)


class Uzivatel(models.Model):
    nick = models.CharField(max_length=50)
    heslo = models.CharField(max_length=70)
    email = models.CharField(max_length=100)
    datum_narozeni = models.DateField()
    ban = models.IntegerField(default = 0)
    ck_id_obec = models.ForeignKey('Obec', on_delete=models.CASCADE)

    def __str__(self):
        return "{}{}{}{}".format(self.email, self.nick, self.nick, self.datum_narozeni, self.ban, self.ck_id_obec.nazev)


class Komentar(models.Model):
    obsah = models.TextField()
    ck_id_uzivatel = models.ForeignKey('Uzivatel', on_delete=models.CASCADE)
    ck_id_dokument = models.ForeignKey('Dokument', on_delete=models.CASCADE)
    ck_id_foto = models.ForeignKey('Foto', on_delete=models.CASCADE)

    def __str__(self):
        return "{}{}{}{}".format(self.ck_id_uzivatel.nick, self.obsah, self.ck_id_dokument, self.ck_id_foto)
