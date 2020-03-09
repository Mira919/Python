from django.shortcuts import render
import csv

def inflation_view(request):
    template_name = 'inflation.html'

    inflation_list = []
    with open('inflation_russia.csv', encoding='UTF-8') as f: # читаем CSV файл
        reader = csv.DictReader(f, delimiter=';')
        for inflation in reader:
            inflation_list.append({'Year': inflation['Год'], # добавляем в список словари
                                   'January': inflation['Янв'],
                                   'February': inflation['Фев'],
                                   'March': inflation['Мар'],
                                   'April': inflation['Апр'],
                                   'May': inflation['Май'],
                                   'June': inflation['Июн'],
                                   'July': inflation['Июл'],
                                   'August': inflation['Авг'],
                                   'September': inflation['Сен'],
                                   'October': inflation['Окт'],
                                   'November': inflation['Ноя'],
                                   'December': inflation['Дек'],
                                   'Sum': inflation['Суммарная']
                                   })

    context = {'inflation': inflation_list}

    return render(request, template_name, context)