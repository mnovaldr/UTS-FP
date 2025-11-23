from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets

from .models import Anggota, Buku, Peminjaman
from .forms import AnggotaForm, BukuForm, PeminjamanForm
from .serializers import AnggotaSerializer, BukuSerializer, PeminjamanSerializer

# ===== VIEWS UNTUK WEB (HTML) =====

# === ANGGOTA VIEWS ===
class AnggotaListView(ListView):
    model = Anggota
    template_name = 'perpustakaan/anggota_list.html'
    context_object_name = 'anggota_list'
    ordering = ['-tanggal_daftar']

class AnggotaDetailView(DetailView):
    model = Anggota
    template_name = 'perpustakaan/anggota_detail.html'
    context_object_name = 'anggota'

class AnggotaCreateView(CreateView):
    model = Anggota
    form_class = AnggotaForm
    template_name = 'perpustakaan/anggota_form.html'
    success_url = reverse_lazy('anggota-list')

class AnggotaUpdateView(UpdateView):
    model = Anggota
    form_class = AnggotaForm
    template_name = 'perpustakaan/anggota_form.html'
    success_url = reverse_lazy('anggota-list')

class AnggotaDeleteView(DeleteView):
    model = Anggota
    template_name = 'perpustakaan/anggota_confirm_delete.html'
    success_url = reverse_lazy('anggota-list')

# === BUKU VIEWS ===
class BukuListView(ListView):
    model = Buku
    template_name = 'perpustakaan/buku_list.html'
    context_object_name = 'buku_list'
    ordering = ['judul']

class BukuDetailView(DetailView):
    model = Buku
    template_name = 'perpustakaan/buku_detail.html'
    context_object_name = 'buku'

class BukuCreateView(CreateView):
    model = Buku
    form_class = BukuForm
    template_name = 'perpustakaan/buku_form.html'
    success_url = reverse_lazy('buku-list')

class BukuUpdateView(UpdateView):
    model = Buku
    form_class = BukuForm
    template_name = 'perpustakaan/buku_form.html'
    success_url = reverse_lazy('buku-list')

class BukuDeleteView(DeleteView):
    model = Buku
    template_name = 'perpustakaan/buku_confirm_delete.html'
    success_url = reverse_lazy('buku-list')

# === PEMINJAMAN VIEWS ===
class PeminjamanListView(ListView):
    model = Peminjaman
    template_name = 'perpustakaan/peminjaman_list.html'
    context_object_name = 'peminjaman_list'
    ordering = ['-tanggal_pinjam']

class PeminjamanDetailView(DetailView):
    model = Peminjaman
    template_name = 'perpustakaan/peminjaman_detail.html'
    context_object_name = 'peminjaman'

class PeminjamanCreateView(CreateView):
    model = Peminjaman
    form_class = PeminjamanForm
    template_name = 'perpustakaan/peminjaman_form.html'
    success_url = reverse_lazy('peminjaman-list')

class PeminjamanUpdateView(UpdateView):
    model = Peminjaman
    form_class = PeminjamanForm
    template_name = 'perpustakaan/peminjaman_form.html'
    success_url = reverse_lazy('peminjaman-list')

class PeminjamanDeleteView(DeleteView):
    model = Peminjaman
    template_name = 'perpustakaan/peminjaman_confirm_delete.html'
    success_url = reverse_lazy('peminjaman-list')


# ===== VIEWS UNTUK API (DRF) =====

class AnggotaViewSet(viewsets.ModelViewSet):
    queryset = Anggota.objects.all().order_by('-tanggal_daftar')
    serializer_class = AnggotaSerializer
    basename = 'api-anggota'

class BukuViewSet(viewsets.ModelViewSet):
    queryset = Buku.objects.all().order_by('judul')
    serializer_class = BukuSerializer
    basename = 'api-buku'


class PeminjamanViewSet(viewsets.ModelViewSet):
    queryset = Peminjaman.objects.all().order_by('-tanggal_pinjam')
    serializer_class = PeminjamanSerializer
    basename = 'api-peminjaman'
