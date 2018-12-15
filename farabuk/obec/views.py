from django.shortcuts import render, get_object_or_404
from obec.models import Obec, Album, Foto, Dokument, Uzivatel, Komentar

# Create your views here.


def index(request):
    Obce = Obec.objects.all()
    return render(request, 'index.html', {'Obce': Obce})


def album(request, obec):
    ob = get_object_or_404(Obec, uri = obec)
    alba = Album.objects.filter(ck_id_obec = ob)
    return render(request, 'album.html', {'alba':alba})

def get_fk(tmp):
    ck = get_object_or_404(Obec, uri=tmp)
    return ck


def obec_dokument(request, uri):
    tmp = get_fk(uri)
    dokumenty = Dokument.objects.filter(ck_id_obec=tmp)
    return render(request, 'obec.html', {'dokumenty': dokumenty})
