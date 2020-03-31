from django.contrib import admin
from students.models import Student, Course
# Register your models here.


class StudentAdmin(admin.ModelAdmin): # добавление студентов в админку
    pass


class CourseAdmin(admin.ModelAdmin): # добавление студентов в админку
    pass


admin.site.register(Student, StudentAdmin) # добавление студентов в админку
admin.site.register(Course, CourseAdmin) # добавление студентов в админку
