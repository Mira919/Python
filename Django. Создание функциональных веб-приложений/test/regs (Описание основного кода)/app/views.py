import datetime

from django.http import HttpResponse

from django.core.paginator import Paginator

from django.conf import settings # то есть файл settings.py будет прочитан только при необходимости


def contact_view(request):
    return HttpResponse(settings.EMAIL_CONTACT) # выводит на страницу переменную EMAIL_CONTACT(settings.py)


def hello_view(request): # Динамический запрос. Ссылка: 127.0.0.1:8000/hello/?name=Vova&age=22
    name = request.GET.get('name', 'Mira') # если name не указано, то подставляется Mira
    msg = f'hello {name}'
    return HttpResponse(msg) # выводит на страницу переменную msg


# Передает дату через URL в формате since/2018-09-01/ и выводит сколько дней прошло до этой даты. date из урла(urls.py)
# Если в неправильном формате задана дата в URL то выводить ошибку 404(страница не найдена)
def since_view(request, dt):
    msg = f'Дней прошло: {(datetime.datetime.now() - dt).days}'
    return HttpResponse(msg) # выводит на страницу переменную msg


DATA = [str(i) for i in range(2000)] # список цифр от 1 до 2000

# распределяет 2000 элементов по разным страницам
# 127.0.0.1:8000/pagi/ - от 0 до 9
# 127.0.0.1:8000/pagi/?page=2 - от 10 до 19 и т.д.
def pagi_view(request):
    page = int(request.GET.get('page', 1)) # если page не указано, то подставляется 1
    paginator = Paginator(DATA, 10)
    page_obj = paginator.page(min(page, paginator.num_pages))

    msg = '<br/>'.join(page_obj.object_list) # разделяет символы через перенос строчки
    print(page_obj.has_next())
    print(page_obj.has_previous())
    print(page_obj.previous_page_number())

    return HttpResponse(msg)