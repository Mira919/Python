from django.shortcuts import render


class Test:
    a = 5
    b = 7
    name = 'Name'

    def age(self):
        return 22


def user_info_view(request): # возьмет шаблон user_info.html и на основании контекста просто выведет слово Vova
    return render(request, 'user_info.html', context={'user_info': 'Vova', 'message': 'Простой текст'})


def user_info_view3(request): # возьмет шаблон user_info.html и на основании контекста выведет Dima
    return render(request, 'user_info.html', context={
        'u': {
            'name': 'Dima',
            'a': 7,
    }})


def user_info_view2(request): # возьмет шаблон user_info.html и на основании контекста выведет цифры 5, 7
    user = Test()
    return render(request, 'user_info.html', context={'u': user})


def user_info_view4(request): # возьмет шаблон user_info.html и на основании контекста выведет цифры 5, 7
    return render(request, 'user_info.html', context={'u': Test()})


def cats(request):
    return {'cats': [1, 2, 3]}