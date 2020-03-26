from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), # при запросе http://localhost:8000/admin/ открывает админку
    path('pages/', include('pages.urls')), # пересылает в файл: pages/urls.py
    path('news/', include('news.urls')), # пересылает в файл: news/urls.py
]
