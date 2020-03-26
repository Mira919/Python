from django.shortcuts import render
from django.http import HttpResponse

from .models import Post # импортируем модель Post


def one_view(request): # выводит простой текст на страницу
    return HttpResponse('Этот текст просто выведется на страницу')


def two_view(request): # выводит HTML шаблон (templates/pages/index.html)
    context = {
        'header': 'Я заголовок и передамся динамически с помощью context', # используется в index.html
        'footer': ['Я подвал 1', 'Я подвал 2'], # используется в index.html
        'other': Post.objects.all() # берет данные из БД из модели (таблицы) Post
    }
    return render(request, 'pages/index.html', context)