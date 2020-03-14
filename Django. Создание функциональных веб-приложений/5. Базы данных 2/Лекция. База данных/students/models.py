from django.db import models

NAME_LEN = 64
STUDENT_NAME_LEN = 64

class Course(models.Model):
    name = models.CharField(max_length=NAME_LEN) # текстовый тип
    description = models.TextField() # большой текстовый тип

    def __str__(self):
        return self.name

class Student(models.Model):

    name = models.CharField(max_length=STUDENT_NAME_LEN)

    courses = models.ManyToManyField(Course, related_name='students') # связь многие ко многим с классом Course

    def __str__(self):
        return self.name