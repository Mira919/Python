from django.contrib import admin

from app.models import Person, Car


class PersonAdmin(admin.ModelAdmin): # добавление в админку модель (таблицу) Person
    pass


class CarAdmin(admin.ModelAdmin): # добавление в админку модель (таблицу) Car
    list_display = ('id', 'brand', 'owner') # чтобы отображалось админке эти поля


admin.site.register(Person, PersonAdmin) # добавление в админку модель (таблицу) Person
admin.site.register(Car, CarAdmin) # добавление в админку модель (таблицу) Car
