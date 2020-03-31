from django.db import models

NAME_LEN = 64
STUDENT_NAME_LEN = 64


class Course(models.Model): # создаем модель курсов
    name = models.CharField(max_length=NAME_LEN) # текстовый тип поля
    description = models.TextField() # большой текстовый тип поля

    def __str__(self): # красивый вывод
        return self.name


class Student(models.Model): # создаем модель Студентов
    name = models.CharField(max_length=STUDENT_NAME_LEN) # текстовый тип поля
    courses = models.ManyToManyField(Course, related_name='students') # связь многие ко многим с классом Course

    def __str__(self): # красивый вывод
        return self.name