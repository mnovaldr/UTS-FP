from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AnggotaViewSet, 
    BukuViewSet, 
    PeminjamanViewSet
)

# Buat router untuk API
router = DefaultRouter()
router.register(r'anggota', AnggotaViewSet, basename='api-anggota')
router.register(r'buku', BukuViewSet, basename='api-buku')
router.register(r'peminjaman', PeminjamanViewSet, basename='api-peminjaman')

urlpatterns = [
    path('', include(router.urls)),
    
]