from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

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


def books_detail_view(request, id): # функция возвращает сколько раз мы просмотривали страницу
    template_name = 'books/detail.html' # какой html шаблон берем
    book = get_object_or_404(Book.objects.prefetch_related('authors'), id=id) # из базы берем таблицу Book и передаем элемент с id который указали в адресной строке, prefetch_related('authors') - так как связь м-м чтобы не делались лишние запросы
    session_key = f'book_{book.id}' # получаем сессию
    views_count = request.session.get(session_key) or 0 # получаем сессию или 0
    views_count = int(views_count)
    views_count += 1
    context = { # что передаем в html страницу
        'book': book,
        'views_count': views_count # сколько раз заходили на страницу
    }
    request.session[session_key] = views_count
    response =  render(request, template_name, context)
    return response