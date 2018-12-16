from django import forms
from obec.models import Album, Obec

class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['nazev', 'ck_id_obec']
