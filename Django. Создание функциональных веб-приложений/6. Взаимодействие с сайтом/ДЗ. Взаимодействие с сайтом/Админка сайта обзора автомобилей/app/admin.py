from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin): # добавление в админку автомобилей
    list_display = ('brand', 'model', 'review_count') # какие поля отображаются на странице списка изменений администратора (поля указаны в модели models.py)
    search_fields = ('brand', 'model') # для поиска по названиям
    list_filter = ('brand', 'model') # справа появляется фильтрация по модели и бренду


class ReviewAdmin(admin.ModelAdmin): # добавление в админку обзоров
    form = ReviewAdminForm
    list_display = ('car', 'title') # какие поля отображаются на странице списка изменений администратора (поля указаны в модели models.py)
    search_fields = ('car__brand', 'car__model') # для поиска по названиям
    list_filter = ('title', 'car') # справа появляется фильтрация по заголовкам обзора и по машинам


admin.site.register(Car, CarAdmin) # добавление в админку автомобилей
admin.site.register(Review, ReviewAdmin) # добавление в админку обзоров
