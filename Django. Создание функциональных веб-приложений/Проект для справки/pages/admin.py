# для использования админки сначала надо создать админа: python manage.py createsuperuser
from django.contrib import admin

from . import models

admin.site.register(models.Post) # отображает нашу модель Post в админке
admin.site.register(models.Comment) # отображает нашу модель Comment в админке