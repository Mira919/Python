from django.db import models


class Post(models.Model): # добавлем модель (таблицу) Post в Базу данных

    post_title = models.CharField(max_length=120) # небольшое текстовое поле Post_title с максимальной длиной 120
    post_text = models.TextField() # большое текстовое поле Text
    date = models.DateTimeField() # поле дата с типом дата

    def __str__(self): # для показа обьектов в терминале: python manage.py shell -> from pages.models import Post -> Post.objects.all() выводятся полные поля обьектов
        return f'{self.post_title}: {self.post_text}'


class Comment(models.Model): # добавлем модель (таблицу) Comment в Базу данных

    author_name = models.CharField(max_length=120) # небольшое текстовое поле Author_name с максимальной длиной 120
    comment_text = models.TextField() # большое текстовое поле Text
    post = models.ForeignKey( # связь между моделью (таблицей) Post (у каждого поста свой коммент)
        Post, # с какой моделью связывать
        on_delete=models.CASCADE) # что делать с комментом если пост удалится (CASCADE удалился пост - удалились все комменты)

    def __str__(self): # для показа обьектов в терминале: python manage.py shell -> from pages.models import Comment -> Comment.objects.all() выводятся полные поля обьектов
        return f'{self.comment_text}'


# Создаем данные в БД:
# В консоли python manage.py shell:
# 1. from pages.models import Post, Comment (импортируем модель Post)
# 2. Post.objects.create(title='Title 1', text='this is text of the first post') (создаем запись и присваем значения полям title и text)
# 3. Post.objects.all() (вывести все обьекты модeли Post)


# в шпоры:

# обычно сначал создаем еще одиин файл urls.py в новом приложении

# pip install ipython (красивая оболочка для python manage.py shell)

# def __str__(self): # чтобы при показе обьектов вб: python manage.py shell -> from pages.models import Post -> Post.objects.all() выводились полные названия обьектов
#       return self.title

# в админке можно с помощью графического интерфейса изменять/создавать записи

# init.py - для того чтобы python распознавал папку как пакет
# apps.py - конфиг нащего приложения
# views.py - логика приложения