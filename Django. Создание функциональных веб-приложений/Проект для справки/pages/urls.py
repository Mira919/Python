from django.urls import path
from . import views

urlpatterns = [
    path('1/', views.one_view), # при запросе http://localhost:8000/pages/1/ выполняет функцию one_view из: views.py
    path('2/', views.two_view), # при запросе http://localhost:8000/pages/2/ выполняет функцию two_view из: views.py
]
