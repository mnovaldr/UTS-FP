from django.db import models

# Create your models here.
class Anggota(models.Model):
    nomor_anggota = models.CharField(max_length=10, unique=True, verbose_name="Nomor Anggota")
    nama_lengkap = models.CharField(max_length=100, verbose_name="Nama Lengkap")
    email = models.EmailField(verbose_name="Alamat Email")
    no_telepon = models.CharField(max_length=15, blank=True, verbose_name="Nomor Telepon")
    alamat = models.TextField(verbose_name="Alamat")
    tanggal_daftar = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nomor_anggota} - {self.nama_lengkap}"
    
class Buku(models.Model):
    KATEGORI_CHOICES = [
        ('FIKSI', 'Fiksi'),
        ('NONFIKSI', 'Non-Fiksi'),
        ('TEKNOLOGI', 'Teknologi'),
        ('SEJARAH', 'Sejarah'),
        ('SASTRA', 'Sastra'),
    ]

    isbn = models.CharField(max_length=13, unique=True, verbose_name="ISBN")
    judul = models.CharField(max_length=200, verbose_name="Judul Buku")
    penulis = models.CharField(max_length=100, verbose_name="Penulis")
    kategori = models.CharField(max_length=10, choices=KATEGORI_CHOICES, default='FIKSI')
    tahun_terbit = models.IntegerField(verbose_name="Tahun Terbit")
    penerbit = models.CharField(max_length=100, verbose_name="Penerbit")
    stok = models.IntegerField(default=1, verbose_name="Stok Tersedia")

    def __str__(self):
        return f"{self.judul} - {self.penulis}"
    
class Peminjaman(models.Model):
    STATUS_CHOICES = [
        ('DIPINJAM', 'Dipinjam'),
        ('DIKEMBALIKAN', 'Dikembalikan'),
        ('TERLAMBAT', 'Terlambat'),
    ]

    anggota = models.ForeignKey(Anggota, on_delete=models.CASCADE, related_name='peminjaman')
    buku = models.ForeignKey(Buku, on_delete=models.CASCADE, related_name='peminjaman')
    tanggal_pinjam = models.DateField(auto_now_add=True, verbose_name="Tanggal Pinjam")
    tanggal_kembali = models.DateField(verbose_name="Tanggal Kembali")
    tanggal_dikembalikan = models.DateField(null=True, blank=True, verbose_name="Tanggal Dikembalikan")
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='DIPINJAM')
    denda = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Denda")

    def __str__(self):
        return f"{self.anggota.nama_lengkap} - {self.buku.judul}"