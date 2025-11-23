from rest_framework import serializers
from .models import Anggota, Buku, Peminjaman

class AnggotaSerializer(serializers.ModelSerializer):
    jumlah_peminjaman = serializers.SerializerMethodField()
    
    class Meta:
        model = Anggota
        fields = [
            'id', 'nomor_anggota', 'nama_lengkap', 'email', 
            'no_telepon', 'alamat', 'tanggal_daftar', 'jumlah_peminjaman'
        ]
    
    def get_jumlah_peminjaman(self, obj):
        return obj.peminjaman.count()

class BukuSerializer(serializers.ModelSerializer):
    kategori_display = serializers.CharField(source='get_kategori_display', read_only=True)
    tersedia = serializers.SerializerMethodField()
    
    class Meta:
        model = Buku
        fields = [
            'id', 'isbn', 'judul', 'penulis', 'kategori', 'kategori_display',
            'tahun_terbit', 'penerbit', 'stok', 'tersedia'
        ]
    
    def get_tersedia(self, obj):
        return obj.stok > 0

class PeminjamanSerializer(serializers.ModelSerializer):
    anggota_nama = serializers.CharField(source='anggota.nama_lengkap', read_only=True)
    anggota_nomor = serializers.CharField(source='anggota.nomor_anggota', read_only=True)
    buku_judul = serializers.CharField(source='buku.judul', read_only=True)
    buku_isbn = serializers.CharField(source='buku.isbn', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Peminjaman
        fields = [
            'id', 'anggota', 'anggota_nama', 'anggota_nomor', 
            'buku', 'buku_judul', 'buku_isbn', 'tanggal_pinjam', 
            'tanggal_kembali', 'tanggal_dikembalikan', 'status', 
            'status_display', 'denda'
        ]