from django.views.generic import ListView, DetailView
from django.urls import path, include
from . import views
from pages.models import Post

urlpatterns = [
    path('1/', views.one_view), # при запросе http://localhost:8000/pages/1/ выполняет функцию one_view из: views.py
    path('2/', views.two_view), # при запросе http://localhost:8000/pages/2/ выполняет функцию two_view из: views.py
    # url('3/', ListView.as_view(queryset=Post.objects.all().order_by('-date'),template_name='pages/list.html')), # при запросе http://localhost:8000/pages/2/ выполняет функцию two_view из: views.py
]
