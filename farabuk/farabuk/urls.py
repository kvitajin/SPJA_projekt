"""farabuk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import obec.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', obec.views.index, name="index"),
    path('<obec>', obec.views.obec, name='obec'),
    path('<uri>/dokumenty/', obec.views.obec_dokument, name='dokument'),
    path('<obec>/alba/', obec.views.album, name = 'album'),
    path('<obec>/alba/pridatalbum/', obec.views.pridatAlbum, name = 'create_album'),
    path('<obec>/alba/<album>/', obec.views.foto, name = 'fotky'),
    path('<obec>/alba/<album>/pridatfotku/', obec.views.pridatFoto, name = 'add_foto'),
    path('<obec>/dokumenty/<id>', obec.views.doument_detail, name='detail'),
    path('profil/', obec.views.profil, name='profil'),
    path('prihlas/', obec.views.prihlas, name='prihlas_butt'),
    path('registruj/', obec.views.registruj, name='registruj'),


]

urlpatterns += staticfiles_urlpatterns()
