from django.urls import path, include
from . import views

urlpatterns = [
    path('1/', views.index, name='index'), # пересылает в файл: pages/urls.py
]
