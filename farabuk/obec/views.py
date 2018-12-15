from django.shortcuts import render
from obec.models import Obec, Album, Foto, Dokument, Uzivatel, Komentar

# Create your views here.
def index(request):
    Obce = Obec.objects.all()
    return render(request, 'index.html', {'Obce': Obce})

def album(request, obec):

    ob = Obec.objects.get(uri = obec)
    alba = Album.objects.filter(ck_id_obec = ob.uri)
    return render(request, 'album.html', {'alba':alba})
