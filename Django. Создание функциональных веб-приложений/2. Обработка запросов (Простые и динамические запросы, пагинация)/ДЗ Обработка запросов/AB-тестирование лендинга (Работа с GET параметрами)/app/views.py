from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    url = request.GET.get('from-landing')
    if url == 'original':
        counter_click['original'] += 1
    if url == 'test':
        counter_click['test'] += 1
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    url = request.GET.get('ab-test-arg', 'original')
    if url == 'original':
        counter_show['original'] += 1
        return render_to_response('landing.html')
    if url == 'test':
        counter_show['test'] += 1
        return render_to_response('landing_alternate.html')

def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    try:
        test = counter_click['test'] / counter_show['test']
        original = counter_click['original']/counter_show['original']
        return render_to_response('stats.html', context={
            'test_conversion': test,
            'original_conversion': original,
        })
    except ZeroDivisionError:
        print('Количество показов одной из страниц равняется 0, пожалуйста, подождите еще')
        return render_to_response('stats.html', context={
            'test_conversion': 0.0,
            'original_conversion': 0.0,
        })
