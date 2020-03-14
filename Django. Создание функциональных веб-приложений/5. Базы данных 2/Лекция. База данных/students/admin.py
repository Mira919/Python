from django.contrib import admin
from students.models import Student, Course
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    pass


class CourseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
