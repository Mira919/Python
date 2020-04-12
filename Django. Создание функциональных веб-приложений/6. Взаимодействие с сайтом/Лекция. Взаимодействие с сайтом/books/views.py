from django.shortcuts import render, redirect

from books.forms import BookForm
from books.models import Book


def books_view(request): # возвращаем HTML страничку
    template_name = 'books/list.html' # где лежит HTML страничка
    context = {
        'books': Book.objects.prefetch_related('authors').all() # все книги
    }

    if request.method == 'POST': # если метод POST, создать книгу, иначе просто вернем форму
        form = BookForm(request.POST) # форма из файла forms.py
        if form.is_valid(): # если форма валидная то мы ее сохраняем
            form.save()
            return redirect('books-list')

        context['form'] = form
    else:
        context['form'] = BookForm()
    return render(request, template_name, context)
