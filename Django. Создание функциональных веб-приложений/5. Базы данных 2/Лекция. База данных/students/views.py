from django.shortcuts import render

from students.models import Course

def list_courses(request):
    template_name = 'students/list.html'
    courses = Course.objects.prefetch_related('students').all() # для оптимизации запросов
    context = {'courses': courses}
    return render(request, template_name, context)