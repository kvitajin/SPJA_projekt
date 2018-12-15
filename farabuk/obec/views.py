from django.shortcuts import render
from obec.models import Obec, Album, Foto, Dokument, Uzivatel, Komentar

# Create your views here.
def index(request):
    Obce = Obec.objects.all()
    return render
