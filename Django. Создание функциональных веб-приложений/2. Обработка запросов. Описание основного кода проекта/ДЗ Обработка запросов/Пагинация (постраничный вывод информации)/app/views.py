from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse(bus_stations))


station_list = []
with open('data-398-2018-08-30.csv', encoding='cp1251') as f: # читаем CSV файл и делаем список
    reader = csv.DictReader(f, delimiter=',')
    for station in reader:
        station_list.append({'Name': station["Name"], 'Street': station['Street'], 'District': station['District']})


def bus_stations(request):
    page = int(request.GET.get('page', 1))
    paginator = Paginator(station_list, 10) # пагинатор, вывод по 10 обьектов на странице
    page_obj = paginator.page(min(page, paginator.num_pages)) # пагинатор

    current_page = page

    if page_obj.has_previous(): # если page_obj имеет предыдущую страницу:
        prev_page_url = f'?page={page_obj.previous_page_number()}' # то при нажатии на кнопку он на нее перейдет
    else:
        prev_page_url = None # кнопки не будет

    if page_obj.has_next(): # если page_obj имеет следующую страницу:
        next_page_url = f'?page={page_obj.next_page_number()}' # то при нажатии на кнопку он на нее перейдет
    else:
        next_page_url = None # кнопки не будет

    return render_to_response('index.html', context={
        'bus_stations': page_obj, # данные в таблице
        'current_page': current_page, # начальная страница
        'prev_page_url': prev_page_url, # ссылка на предыдущую страницу
        'next_page_url': next_page_url, # ссылка на следующую страницу
    })

