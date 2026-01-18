from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Anggota, Buku, Peminjaman
from .forms import AnggotaForm, BukuForm, PeminjamanForm
from .serializers import AnggotaSerializer, BukuSerializer, PeminjamanSerializer

# ===== VIEWS UNTUK WEB (HTML) =====

# Mixin untuk membatasi akses hanya untuk Admin (Staff)
class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

# Permission Custom untuk API: User biasa bisa baca (GET), Admin bisa tulis (POST/PUT/DELETE)
class IsAdminOrAuthenticatedReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff

# === ANGGOTA VIEWS ===
class AnggotaListView(LoginRequiredMixin, ListView):
    model = Anggota
    template_name = 'perpustakaan/anggota_list.html'
    context_object_name = 'anggota_list'
    ordering = ['-tanggal_daftar']

class AnggotaDetailView(LoginRequiredMixin, DetailView):
    model = Anggota
    template_name = 'perpustakaan/anggota_detail.html'
    context_object_name = 'anggota'

class AnggotaCreateView(AdminRequiredMixin, CreateView):
    model = Anggota
    form_class = AnggotaForm
    template_name = 'perpustakaan/anggota_form.html'
    success_url = reverse_lazy('anggota-list')

class AnggotaUpdateView(AdminRequiredMixin, UpdateView):
    model = Anggota
    form_class = AnggotaForm
    template_name = 'perpustakaan/anggota_form.html'
    success_url = reverse_lazy('anggota-list')

class AnggotaDeleteView(AdminRequiredMixin, DeleteView):
    model = Anggota
    template_name = 'perpustakaan/anggota_confirm_delete.html'
    success_url = reverse_lazy('anggota-list')

# === BUKU VIEWS ===
class BukuListView(LoginRequiredMixin, ListView):
    model = Buku
    template_name = 'perpustakaan/buku_list.html'
    context_object_name = 'buku_list'
    ordering = ['judul']

class BukuDetailView(LoginRequiredMixin, DetailView):
    model = Buku
    template_name = 'perpustakaan/buku_detail.html'
    context_object_name = 'buku'

class BukuCreateView(AdminRequiredMixin, CreateView):
    model = Buku
    form_class = BukuForm
    template_name = 'perpustakaan/buku_form.html'
    success_url = reverse_lazy('buku-list')

class BukuUpdateView(AdminRequiredMixin, UpdateView):
    model = Buku
    form_class = BukuForm
    template_name = 'perpustakaan/buku_form.html'
    success_url = reverse_lazy('buku-list')

class BukuDeleteView(AdminRequiredMixin, DeleteView):
    model = Buku
    template_name = 'perpustakaan/buku_confirm_delete.html'
    success_url = reverse_lazy('buku-list')

# === PEMINJAMAN VIEWS ===
class PeminjamanListView(LoginRequiredMixin, ListView):
    model = Peminjaman
    template_name = 'perpustakaan/peminjaman_list.html'
    context_object_name = 'peminjaman_list'
    ordering = ['-tanggal_pinjam']

class PeminjamanDetailView(LoginRequiredMixin, DetailView):
    model = Peminjaman
    template_name = 'perpustakaan/peminjaman_detail.html'
    context_object_name = 'peminjaman'

class PeminjamanCreateView(AdminRequiredMixin, CreateView):
    model = Peminjaman
    form_class = PeminjamanForm
    template_name = 'perpustakaan/peminjaman_form.html'
    success_url = reverse_lazy('peminjaman-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Jika status DIPINJAM, kurangi stok buku
        if self.object.status == 'DIPINJAM':
            buku = self.object.buku
            buku.stok -= 1
            buku.save()
        return response

class PeminjamanUpdateView(AdminRequiredMixin, UpdateView):
    model = Peminjaman
    form_class = PeminjamanForm
    template_name = 'perpustakaan/peminjaman_form.html'
    success_url = reverse_lazy('peminjaman-list')

    def form_valid(self, form):
        # Ambil status lama sebelum disimpan
        old_status = Peminjaman.objects.get(pk=self.object.pk).status
        response = super().form_valid(form)
        
        new_status = self.object.status
        buku = self.object.buku
        
        # Logika perubahan stok:
        # 1. Jika sebelumnya DIPINJAM dan sekarang DIKEMBALIKAN/TERLAMBAT -> Stok Bertambah
        if old_status == 'DIPINJAM' and new_status in ['DIKEMBALIKAN', 'TERLAMBAT']:
            buku.stok += 1
            buku.save()
        # 2. Jika sebelumnya DIKEMBALIKAN/TERLAMBAT dan sekarang DIPINJAM -> Stok Berkurang
        elif old_status in ['DIKEMBALIKAN', 'TERLAMBAT'] and new_status == 'DIPINJAM':
            buku.stok -= 1
            buku.save()
            
        return response

class PeminjamanDeleteView(AdminRequiredMixin, DeleteView):
    model = Peminjaman
    template_name = 'perpustakaan/peminjaman_confirm_delete.html'
    success_url = reverse_lazy('peminjaman-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        # Jika menghapus data yang sedang dipinjam, kembalikan stok
        if self.object.status == 'DIPINJAM':
            buku = self.object.buku
            buku.stok += 1
            buku.save()
        return super().delete(request, *args, **kwargs)


# ===== VIEWS UNTUK API (DRF) =====

class AnggotaViewSet(viewsets.ModelViewSet):
    queryset = Anggota.objects.all().order_by('-tanggal_daftar')
    serializer_class = AnggotaSerializer
    basename = 'api-anggota'
    permission_classes = [IsAdminOrAuthenticatedReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['nomor_anggota', 'email']
    search_fields = ['nama_lengkap', 'alamat', 'nomor_anggota']
    ordering_fields = ['tanggal_daftar', 'nama_lengkap']

class BukuViewSet(viewsets.ModelViewSet):
    queryset = Buku.objects.all().order_by('judul')
    serializer_class = BukuSerializer
    basename = 'api-buku'
    permission_classes = [IsAdminOrAuthenticatedReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['kategori', 'tahun_terbit', 'penulis']
    search_fields = ['judul', 'penulis', 'penerbit', 'isbn']
    ordering_fields = ['judul', 'tahun_terbit', 'stok']


class PeminjamanViewSet(viewsets.ModelViewSet):
    queryset = Peminjaman.objects.all().order_by('-tanggal_pinjam')
    serializer_class = PeminjamanSerializer
    basename = 'api-peminjaman'
    permission_classes = [IsAdminOrAuthenticatedReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['anggota', 'buku', 'status']
    search_fields = ['anggota__nama_lengkap', 'buku__judul']
    ordering_fields = ['tanggal_pinjam', 'status', 'tanggal_kembali']

    def perform_create(self, serializer):
        instance = serializer.save()
        if instance.status == 'DIPINJAM':
            instance.buku.stok -= 1
            instance.buku.save()

    def perform_update(self, serializer):
        instance = self.get_object()
        old_status = instance.status
        updated_instance = serializer.save()
        
        new_status = updated_instance.status
        buku = updated_instance.buku
        
        if old_status == 'DIPINJAM' and new_status in ['DIKEMBALIKAN', 'TERLAMBAT']:
            buku.stok += 1
            buku.save()
        elif old_status in ['DIKEMBALIKAN', 'TERLAMBAT'] and new_status == 'DIPINJAM':
            buku.stok -= 1
            buku.save()

    def perform_destroy(self, instance):
        if instance.status == 'DIPINJAM':
            instance.buku.stok += 1
            instance.buku.save()
        instance.delete()
