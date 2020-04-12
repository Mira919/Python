from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os

def home_view(request):
    template_name = 'app/home.html'

    pages = { # показывается на начальной странице
        'Главная страница': reverse('home'), # переводит на главную страницу (home из файла urls.py)
        'Показать текущее время': reverse('time'), # переводит на страницу, которая показывает текущее время (time из файла urls.py)
        'Показать содержимое рабочей директории': reverse('workdir') # переводит на страницу, которая показывает все файла в папке проекта (workdir из файла urls.py)
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request): # функция которая выводит на страницу текущее время
    current_time = datetime.datetime.time(datetime.datetime.now())
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request): # функция которая выводит на страницу файлы в папке проекта через перенос строки
    msg = os.listdir(path=".")
    return HttpResponse('<br/>'.join(msg))
