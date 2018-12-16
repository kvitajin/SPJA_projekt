from django import forms
from obec.models import Album, Obec, Foto

class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['nazev', 'ck_id_obec']


class AddFoto(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['nazev_souboru', 'popis', 'soubor']
