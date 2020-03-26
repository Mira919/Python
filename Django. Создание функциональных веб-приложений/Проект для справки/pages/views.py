from django.shortcuts import render
from django.http import HttpResponse


def one_view(request): # выводит простой текст на страницу
    return HttpResponse('Этот текст выведется на страницу')


def two_view(request): # выводит HTML шаблон (templates/pages/index.html)
    context = {
        'header': 'Я заголовок и передамся динамически с помощью context',
        'footer': ['Я подвал 1', 'Я подвал 2'],
    } # выводится на страничке (как {{ header }})
    return render(request, 'pages/index.html', context)