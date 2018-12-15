from django.shortcuts import render, get_object_or_404
from obec.models import Obec, Album, Foto, Dokument, Uzivatel, Komentar

# Create your views here.


def index(request):
    Obce = Obec.objects.all()
    return render(request, 'index.html', {'Obce': Obce})

<<<<<<< HEAD
def album(request, obec):

    ob = Obec.objects.get(uri = obec)
    alba = Album.objects.filter(ck_id_obec = ob.uri)
    return render(request, 'album.html', {'alba':alba})
=======

def get_fk(tmp):
    ck = get_object_or_404(Obec, uri=tmp)
    return ck


def obec_dokument(request, uri):
    tmp = get_fk(uri)
    dokumenty = Dokument.objects.filter(ck_id_obec=tmp)
    return render(request, 'obec.html', {'dokumenty': dokumenty})
>>>>>>> 6aa5fbad57150a27198e2276aa792e5d632bba9d
