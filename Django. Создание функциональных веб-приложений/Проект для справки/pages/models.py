from django.db import models
from django.utils import timezone
import datetime


class Post(models.Model): # добавлем модель (таблицу) Post в Базу данных

    post_title = models.CharField(max_length=120) # небольшое текстовое поле Post_title с максимальной длиной 120
    post_text = models.TextField() # большое текстовое поле Text
    date = models.DateTimeField() # поле дата с типом дата

    def was_published_recently(self): # функция, проверяет был ли пост опубликован недавно
        return self.date >= (timezone.now() - datetime.timedelta(days=7)) # возвращает True если дата публикации статьи не больше 7 дней

        # В python manage.py shell:
        # from pages.models import Post
        # a = Post.objects.first() (берем первый обьект)
        # a.was_published_recently() (проверяем на функцию, выводит True)

    class Meta: # для визуального
        verbose_name = 'Пост'  # отображается на странице постов
        verbose_name_plural = 'Посты'  # отображается на главной странице админа

    def __str__(self): # для показа обьектов в терминале: python manage.py shell -> from pages.models import Post -> Post.objects.all() выводятся поля обьектов, которые мы укажем
        return f'{self.post_title}: {self.post_text}'


class Comment(models.Model): # добавлем модель (таблицу) Comment в Базу данных

    author_name = models.CharField(max_length=120) # небольшое текстовое поле Author_name с максимальной длиной 120
    comment_text = models.TextField() # большое текстовое поле Text
    post = models.ForeignKey( # связь между моделью (таблицей) Post (у каждого поста свой коммент)
        Post, # с какой моделью связывать
        on_delete=models.CASCADE) # что делать с комментом если пост удалится (CASCADE удалился пост - удалились все комменты)

    class Meta: # для визуального
        verbose_name = 'Комментарий'  # отображается на странице комментариев
        verbose_name_plural = 'Комментарии'  # отображается на главной странице админа

    def __str__(self): # для показа обьектов в терминале: python manage.py shell -> from pages.models import Comment -> Comment.objects.all() выводятся поля обьектов которые мы укажем
        return f'{self.author_name} {self.comment_text}'


# Добавляем данные в БД, в консоли python manage.py shell:

    # Для таблицы Post (добавляем посты):
        # 1. from pages.models import Post (импортируем модели Post)
        # 2. from django.utils import timezone (импортируем модуль который определяет время)
        # 3. Post.objects.create(post_title='Пост 1', post_text='текст для Поста 1', date=timezone.now()) (создаем запись и присваем значения полям pos_title, post_text, date)
        # 4. Post.objects.all() (вывести все обьекты модeли Post)

    # Для таблицы Comment (добавляем комментарии к постам, можно добавить в интерфейсе админки):
        # 1. from pages.models import Post, Comment (импортируем модели Post и Comment)
        # 2. a = Post.objects.first() (берем первый пост)
        # 3. a.comment_set.create(author_name='Мира', comment_text='Коммент 1 к первому посту') (добавить первый коммент в первому посту)
        # 4. a.comment_set.create(author_name='Денис', comment_text='Коммент 2 к первому посту') (добавить второй коммент в первому посту)
        # . a.comment_set.all() (вывести все комментарии первого поста)

