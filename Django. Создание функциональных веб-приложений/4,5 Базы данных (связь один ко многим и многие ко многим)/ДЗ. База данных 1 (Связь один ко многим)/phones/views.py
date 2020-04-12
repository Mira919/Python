from django.shortcuts import render
from .models import Phone

def show_catalog(request): # сортировка
    sort = request.GET.get('sort')
    if sort:
        if sort == 'name': # сортировка по названию
            phones = Phone.objects.all().order_by('name')
        elif sort == 'min_price': # сортировка по убыванию цены
            phones = Phone.objects.all().order_by('price')
        elif sort == 'max_price': # сортировка по возрастанию цены
            phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all() # просто вывод
    context = {
        'phones': phones
    }

    return render(request, 'catalog.html', context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone
    }

    return render(request, 'product.html', context)
