from django.core.cache import cache
from django.shortcuts import render

from students.models import Course

cache_key = 'students-list-courses' # ключ для кэширования курсов


def list_courses(request):
    template_name = 'students/list.html' # HTML шаблон

    cache_courses = cache.get(cache_key)  # получаем кэширование
    if not cache_courses:  # если хэша нет, то делаем запрос и кэширование курсов
        courses = Course.objects.prefetch_related('students').all() # для оптимизации запросов
        cache.set(cache_key, courses, timeout=5)  # сохраняем кэширование
    else:
        courses = cache_courses # получаем кэш

    context = {'courses': courses} # модель курсов
    return render(request, template_name, context)