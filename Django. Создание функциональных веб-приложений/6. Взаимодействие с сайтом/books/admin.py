from django.contrib import admin

from books.models import Book, Author


class BookAdmin(admin.ModelAdmin): # для визуального взаимодейтсвия с БД с таблицой книг
    pass


class AuthorAdmin(admin.ModelAdmin): # для визуального взаимодейтсвия с БД с таблицой авторов
    pass


admin.site.register(Book, BookAdmin) # для визуального взаимодейтсвия с БД с таблицой книг
admin.site.register(Author, AuthorAdmin) # для визуального взаимодейтсвия с БД с таблицой авторов
