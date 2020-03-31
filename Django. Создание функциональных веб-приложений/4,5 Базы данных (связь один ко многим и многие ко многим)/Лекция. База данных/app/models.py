from django.db import models

ATTR_MAX_LEN = 64 # максимальная длина колонки
BREND_LEN = 32 # максимальная длина колонки

BREND_CHOICES = [ # первое будет хранится в БД, другое на показ пользователю
    ('BMW', 'БМВ'),
    ('AUDI', 'Ауди'),
    ('TESLA', 'Тесла'),
]


class Person(models.Model): # владелец автомобиля

    name = models.CharField( # добавляем имя человека
        max_length=ATTR_MAX_LEN, # задаем максимальную длину колонки
        blank=True, # позволяет сохранять пустые строки
        null=False, # не позволяет сохранять строки Null
    )

    def __str__(self): # для красивого вывода
        return f'{self.id}: {self.name}'

    test = models.IntegerField() # обьявлено поле Test


class Car(models.Model): # сущность автомобиля

    brand = models.CharField( # добавляем бренд автомобиля
        max_length=BREND_LEN, # задаем максимальную длину колонки
        choices=BREND_CHOICES,
    )

    owner = models.ForeignKey( # добавляем владельца автомобиля
        Person,
        null=True, # позволяет сохранять строки Null
        # unique=True, # уникальное поле
        on_delete=models.SET_NULL # если владелец удаляется из Person то сущность автомибиля будет NULL
    )

    def __str__(self): # для красивого вывода
        return f'{self.id}: {self.name}'