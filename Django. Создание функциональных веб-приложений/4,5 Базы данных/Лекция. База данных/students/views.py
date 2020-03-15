from django.shortcuts import render

from students.models import Course


def list_courses(request):
    template_name = 'students/list.html' # HTML шаблон
    courses = Course.objects.prefetch_related('students').all() # для оптимизации запросов
    context = {'courses': courses} # модель курсов
    return render(request, template_name, context)