from django.db import models


class Author(models.Model): # создаем таблицу авторов
    name = models.CharField(max_length=100) # создаем поле имя автора

    def __str__(self): # для красивого показа
        return self.name


class Book(models.Model): # создаем таблицу книг
    name = models.CharField(max_length=100) # создаем поле название книги
    year = models.IntegerField() # создаем поле год книги
    authors = models.ManyToManyField(Author) # соединяем с таблицей авторов (связь многие ко многим)

    def __str__(self): # для красивого показа
        return f'{self.year} - {self.name}'
