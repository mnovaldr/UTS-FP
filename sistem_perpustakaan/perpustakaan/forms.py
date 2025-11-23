from django import forms
from .models import Anggota, Buku, Peminjaman

class AnggotaForm(forms.ModelForm):
    class Meta:
        model = Anggota
        fields = ['nomor_anggota', 'nama_lengkap', 'email', 'no_telepon', 'alamat']
        widgets = {
            'nomor_anggota': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contoh: AGT001'}),
            'nama_lengkap': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama lengkap anggota'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@contoh.com'}),
            'no_telepon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '08123456789'}),
            'alamat': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Alamat lengkap'}),
        }
        labels = {
            'nomor_anggota': 'Nomor Anggota',
            'nama_lengkap': 'Nama Lengkap',
            'email': 'Alamat Email',
            'no_telepon': 'Nomor Telepon',
            'alamat': 'Alamat',
        }

class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = ['isbn', 'judul', 'penulis', 'kategori', 'tahun_terbit', 'penerbit', 'stok']
        widgets = {
            'isbn': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '13 digit ISBN'}),
            'judul': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Judul buku'}),
            'penulis': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama penulis'}),
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'tahun_terbit': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Tahun terbit'}),
            'penerbit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nama penerbit'}),
            'stok': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }
        labels = {
            'isbn': 'ISBN',
            'judul': 'Judul Buku',
            'penulis': 'Penulis',
            'kategori': 'Kategori',
            'tahun_terbit': 'Tahun Terbit',
            'penerbit': 'Penerbit',
            'stok': 'Stok Tersedia',
        }

class PeminjamanForm(forms.ModelForm):
    class Meta:
        model = Peminjaman
        fields = ['anggota', 'buku', 'tanggal_kembali', 'status', 'denda']
        widgets = {
            'anggota': forms.Select(attrs={'class': 'form-control'}),
            'buku': forms.Select(attrs={'class': 'form-control'}),
            'tanggal_kembali': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'denda': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': 0}),
        }
        labels = {
            'anggota': 'Peminjam',
            'buku': 'Buku yang Dipinjam',
            'tanggal_kembali': 'Tanggal Harus Kembali',
            'status': 'Status Peminjaman',
            'denda': 'Denda (Rp)',
        }