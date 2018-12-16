from django.shortcuts import render, get_object_or_404, redirect
from obec.models import Obec, Album, Foto, Dokument, Uzivatel, Komentar
from django.http import HttpResponse
from obec.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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


def doument_detail(request, obec, id):
    clanek = get_object_or_404(Dokument, pk=id)
    return render(request, 'detail.html', {'clanek': clanek})


def profil(request):
    uziv = Uzivatel.objects.get(pk=request.session['id'])
    return render(request, 'profil.html', {'uziv': uziv})


def prihlas(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'prihlas_butt.html', {'form': form})




        # form = Prihlas(request.POST)
    #     if form.is_valid():
    #         uziv = Uzivatel.objects.get(email=form.email)
    #         if uziv.heslo == request.POST['heslo']:
    #             request.session['id'] = uziv.id                         #todo tady mozna bude potreba misto uziv.id dat jen uziv
    #             return HttpResponse('Jste prihlasen')
    #     else:
    #         return HttpResponse('Prihlaseni se nezdario')
    #         pass
    # else:
    #     return HttpResponse('o kurwa')


def odhlas(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return HttpResponse("Jste Odhlasen")


def registruj(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('index')
        else:
            form = UserCreationForm()
    return render(request, 'registruj.html', {'form': form})
