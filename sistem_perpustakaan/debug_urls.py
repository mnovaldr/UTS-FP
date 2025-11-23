# debug_urls.py
import os
import django
from django.urls import get_resolver

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistem_perpustakaan.settings')
django.setup()

def print_urls(urls=None, prefix=''):
    if urls is None:
        urls = get_resolver().url_patterns
    
    for url in urls:
        if hasattr(url, 'url_patterns'):
            # Ini adalah include()
            print_urls(url.url_patterns, prefix + str(url.pattern))
        else:
            print(f"{prefix}{url.pattern} -> {url.name}")

print("=== URL PATTERNS YANG TERDAFTAR ===")
print_urls()