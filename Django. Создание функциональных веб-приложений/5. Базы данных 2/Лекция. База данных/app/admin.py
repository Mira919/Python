from django.contrib import admin

from app.models import Person, Car

class PersonAdmin(admin.ModelAdmin):
    pass


class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'owner') # чтобы отображалосьв админке эти поля


admin.site.register(Person, PersonAdmin)
admin.site.register(Car, CarAdmin)
