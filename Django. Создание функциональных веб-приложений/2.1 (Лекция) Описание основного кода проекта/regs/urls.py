"""regs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import datetime

from django.contrib import admin
from django.urls import path, register_converter

from app.views import contact_view, hello_view, since_view, pagi_view


class DataConverter: # конвертор дат, из интернета
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}' # формат: 4 числа от 0-9 - 2 числа от 0-9 - 2 числа от 0-9
    def to_python(self, value):
        return datetime.datetime.strptime(value, '%Y-%m-%d') # перевод в правильный формат
    def to_url(self, value):
        return value.strftime('%Y-%m-%d')


register_converter(DataConverter, 'date') # подключаем конвертер дат из интернета

urlpatterns = [ # задает урлы и функции которые буду выполняться при переходе на урлы
    path('admin/', admin.site.urls),
    path('contact/', contact_view, name='contact'), # по ссылке 127.0.0.1:8000/contact/ , будет выполнять функцию contact_view(views.py)
    path('hello/', hello_view, name='hello'), # по ссылке 127.0.0.1:8000/hello/, будет выполнять функцию hello_view(views.py)
    path('since/<date:dt>/', since_view, name='since'), # по ссылке 127.0.0.1:8000/since/ , будет выполнять функцию since_view(views.py). Date будет браться из урла и передаваться в функцию since_view(views.py)
    path('pagi/', pagi_view, name='pagi') # по ссылке 127.0.0.1:8000/since/ , будет выполнять функцию since_view(views.py). Date будет браться из урла и передаваться в функцию since_view(views.py)
]

