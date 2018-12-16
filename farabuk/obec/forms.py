from django import forms
from obec.models import *


class Registruj(forms.ModelForm):
    class Meta:
        model=Uzivatel
        fields=['nick', 'heslo', 'email', 'datum_narozeni', 'ck_id_obec']
    # nick: forms.CharField(max_length=50, label='nick')
    # heslo: forms.CharField(max_length=70, label='heslo')
    # email: forms.CharField(max_length=100, label='email')
    # datum_narozeni: forms.DateField(label='datum_narozeni')
    # ck_id_obec: forms.ModelChoiceField(Obec.nazev)


class Prihlas(forms.Form):
    email: forms.CharField(max_length=100, label='email')
    heslo: forms.CharField(max_length=70, label='heslo')
