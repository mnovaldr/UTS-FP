"""
URL configuration for sistem_perpustakaan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Landing Page & Auth Web
    path('', TemplateView.as_view(template_name='perpustakaan/landing.html'), name='home'),
    path('accounts/login/', LoginView.as_view(template_name='perpustakaan/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    
    path('perpustakaan/', include('perpustakaan.urls')),
    path('api/', include('perpustakaan.api_urls')),
    path('api/token/', obtain_auth_token, name='api_token_auth'),

    # Endpoint untuk mengunduh schema YAML/JSON
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Endpoint untuk tampilan UI Redoc
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]