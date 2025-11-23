from django.urls import path
from .views import (
    # Views untuk Anggota
    AnggotaListView, AnggotaDetailView, AnggotaCreateView, 
    AnggotaUpdateView, AnggotaDeleteView,
    
    # Views untuk Buku
    BukuListView, BukuDetailView, BukuCreateView,
    BukuUpdateView, BukuDeleteView,
    
    # Views untuk Peminjaman
    PeminjamanListView, PeminjamanDetailView, PeminjamanCreateView,
    PeminjamanUpdateView, PeminjamanDeleteView,
)

urlpatterns = [
    # === URL UTAMA & REDIRECT ===
    path('', AnggotaListView.as_view(), name='home'),
    
    # === URL ANGGOTA ===
    path('anggota/', AnggotaListView.as_view(), name='anggota-list'),
    path('anggota/tambah/', AnggotaCreateView.as_view(), name='anggota-tambah'),
    path('anggota/<int:pk>/', AnggotaDetailView.as_view(), name='anggota-detail'),
    path('anggota/<int:pk>/edit/', AnggotaUpdateView.as_view(), name='anggota-edit'),
    path('anggota/<int:pk>/hapus/', AnggotaDeleteView.as_view(), name='anggota-hapus'),
    
    # === URL BUKU ===
    path('buku/', BukuListView.as_view(), name='buku-list'),
    path('buku/tambah/', BukuCreateView.as_view(), name='buku-tambah'),
    path('buku/<int:pk>/', BukuDetailView.as_view(), name='buku-detail'),
    path('buku/<int:pk>/edit/', BukuUpdateView.as_view(), name='buku-edit'),
    path('buku/<int:pk>/hapus/', BukuDeleteView.as_view(), name='buku-hapus'),
    
    # === URL PEMINJAMAN ===
    path('peminjaman/', PeminjamanListView.as_view(), name='peminjaman-list'),
    path('peminjaman/tambah/', PeminjamanCreateView.as_view(), name='peminjaman-tambah'),
    path('peminjaman/<int:pk>/', PeminjamanDetailView.as_view(), name='peminjaman-detail'),
    path('peminjaman/<int:pk>/edit/', PeminjamanUpdateView.as_view(), name='peminjaman-edit'),
    path('peminjaman/<int:pk>/hapus/', PeminjamanDeleteView.as_view(), name='peminjaman-hapus'),
]