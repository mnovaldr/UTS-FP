from django.contrib import admin
from .models import Anggota, Buku, Peminjaman

admin.site.register(Anggota)
admin.site.register(Buku)
admin.site.register(Peminjaman)