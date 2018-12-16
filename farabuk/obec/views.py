from django.shortcuts import render, get_object_or_404, redirect
from obec.models import Obec, Album, Foto, Dokument, Uzivatel, Komentar
from django.http import HttpResponse
from obec.forms import CreateAlbumForm

# Create your views here.


def index(request):
    Obce = Obec.objects.all()
    return render(request, 'index.html', {'Obce': Obce})

def album(request, obec):
    ob = get_object_or_404(Obec, uri=obec)
    alba = Album.objects.filter(ck_id_obec=ob)
    return render(request, 'album.html', {'alba': alba})

def pridatAlbum(request, obec):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            #save to db
            instance = form.save(commit = False)
            instance.je_uvodni = 0
            instance.save()
            return redirect('index')
    else:
        form = CreateAlbumForm()
    return render(request, 'createAlbum.html', {'form':form})


def foto(request, obec, album):
    alb = get_object_or_404(Album, pk = album)
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
    uziv = Uzivatel.objects.get(pk=request.session)
    return render(request, 'profil.html', {'uziv': uziv})


def prihlas(request):
    uziv=Uzivatel.objects.get(nick=request.POST['nick'])
    if uziv.heslo == request.POST['heslo']:
        request.session['id'] = uziv.id                           #todo tady mozna bude potreba misto uziv.id dat jen uziv
        HttpResponse('Jste prihlasen')
    else:
        HttpResponse('Prihlaseni se nezdario')


def odhlas(request):
    try:
        del request.session['id']
    except KeyError:
        pass
    return HttpResponse("Jste Odhlasen")
