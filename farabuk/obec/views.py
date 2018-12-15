from django.shortcuts import render, get_object_or_404
from obec.models import Obec, Album, Foto, Dokument, Uzivatel, Komentar

# Create your views here.


def index(request):
    Obce = Obec.objects.all()
    return render(request, 'index.html', {'Obce': Obce})


def album(request, obec):
    ob = get_object_or_404(Obec, uri=obec)
    alba = Album.objects.filter(ck_id_obec=ob)
    return render(request, 'album.html', {'alba': alba})

def foto(request, obec, album):
    alb = get_object_or_404(Album, nazev = album)
    fotky = Foto.objects.filter(ck_id_album = alb)
    return render(request, 'foto.html', {'fotky':fotky})

def get_fk(tmp):
    ck = get_object_or_404(Obec, uri=tmp)
    return ck


def obec_dokument(request, uri):
    tmp = get_fk(uri)
    dokumenty = Dokument.objects.filter(ck_id_obec=tmp)
    return render(request, 'dokument.html', {'dokumenty': dokumenty})


def obec(request, obec):
    obc = get_object_or_404(Obec, uri=obec)
    return render(request, 'obec.html', {'obec': obc})
