from django.db import models
from django.utils.text import slugify

class Phone(models.Model): # создаем модель Phone с полями:
    id = models.IntegerField(primary_key=True, unique=True) # id, числовой, основной ключ, уникальный
    name = models.CharField(max_length=50) # name, текстовый, максимальная длина 50
    image = models.URLField() # image, тип - ссылка
    price = models.IntegerField() # price, числовой
    release_date = models.DateField() # release_date, тип - дата
    lte_exists = models.BooleanField() # lte_exists, тип - булевый
    slug = models.SlugField(unique=True) # slug от name, текстовый, максимальная длина 50

    # слаг - транслитерация текста + приведение в нижний регистр + замена пунктуации
    def save(self, *args, **kwargs): # функция для слага
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)