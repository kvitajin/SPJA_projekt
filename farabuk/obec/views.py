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


def pridatAlbum(request, obec):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            #save to db
            instance = form.save(commit = False)
            instance.je_uvodni = 0
            instance.save()
            return redirect('album', obec)
    else:
        form = CreateAlbumForm()
    return render(request, 'createAlbum.html', {'form': form})


def foto(request, obec, album):
    alb = get_object_or_404(Album, pk=album)
    fotky = Foto.objects.filter(ck_id_album=alb)
    return render(request, 'foto.html', {'fotky': fotky})


def komentarFoto(request, obec, album, fotka):
    foto = get_object_or_404(Foto, pk=fotka)
    komentare = Komentar.objects.filter(ck_id_foto=foto)
    return render(request, 'commentFoto.html', {'komentare': komentare})


def pridatFoto(request, obec, album):
    if request.method == 'POST':
        form = AddFoto(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.ck_id_album = get_object_or_404(Album, pk=album)
            instance.save()
            return redirect('fotky', obec, album)
        else:
            return HttpResponse('Something is wrong :(')
    else:
        form = AddFoto()
    return render(request, 'addFoto.html', {'form': form})


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
            uziv = Uzivatel.objects.get(nick=request.POST['username'])
            request.session['id'] = uziv.pk
            request.session['ban'] = uziv.ban
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
    return redirect('index')


def registruj(request):
    if request.method == "POST":
        form = Registruj(request.POST)
        # nick = form.cleaned_data['nick']
        # heslo =form.cleaned_data['heslo']
        # email=form.cleaned_data['email']
        # ban =form.cleaned_data['ban']
        # datum_narozeni =form.cleaned_data['datum_narozeni']
        # ck_id_obec =
        instance=form.save(commit=False)
        instance.ban = 0
        instance.save()
        return redirect('index')
    else:
        form = Registruj()
    return render(request, 'registruj.html', {'form': form})


def addDocument(request, obec):
    if request.method == "POST":
        form = AddDoc(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            obec_id = get_object_or_404(Obec, uri=obec)
            instance.ck_id_obec = obec_id
            instance.save()
            return redirect('index')
    else:
        form = AddDoc()
    return render(request, 'add_document.html', {'form': form})



def addCommentFoto(request, obec, idAlba, idFoto):
    if request.method == "POST":
        form = AddCommentFoto(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.ck_id_uzivatel = get_object_or_404(Uzivatel, pk=1)
            instance.ck_id_foto = get_object_or_404(Foto, pk=idFoto)
            instance.ck_id_dokument = get_object_or_404(Dokument, pk =1)
            instance.save()
            return redirect('index')
    else:
        form = AddCommentFoto()
    return render(request, 'add_comment_foto.html', {'form': form})


def images(request):
    return None

