from django.urls import path
from . import views

urlpatterns = [
    path('1/', views.one_view), # выполняет функцию one_view из: views.py
    path('2/', views.two_view), # выполняет функцию two_view из: views.py
]
