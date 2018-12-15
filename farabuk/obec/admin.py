from django.contrib import admin
from obec.models import Obec, Album, Foto, Dokument, Uzivatel, Komentar

# Register your models here.

admin.site.register(Obec)
admin.site.register(Album)
admin.site.register(Foto)
admin.site.register(Dokument)
admin.site.register(Uzivatel)
admin.site.register(Komentar)

