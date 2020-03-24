from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=50) # создать текстовое поле брэнд с длинной 50
    model = models.CharField(max_length=50) # создать текстовое поле модели с длинной 50

    class Meta:
        ordering = ['-id'] # от элемента с большим id к элементу с меньшим. Тогда новые записи будут наверху.
        verbose_name = 'Автомобиль' # отображается на странице автомобилей
        verbose_name_plural = 'Автомобили' # отображается на общей странице со всеми таблицами

    def __str__(self): # для красивого вывода
        return f'{self.brand} {self.model}'

    def review_count(self):
        return Review.objects.filter(car=self).count()


class Review(models.Model):

    class Meta:
        ordering = ['-id'] # от элемента с большим id к элементу с меньшим. Тогда новые записи будут наверху.
        verbose_name = 'Обзор' # отображается на странице обзоров
        verbose_name_plural = 'Обзоры' # отображается на общей странице со всеми таблицами

    car = models.ForeignKey(Car, on_delete=models.CASCADE) # создать ключевое поле машины и соединить с моделью автомобилей
    title = models.CharField(max_length=100) # создать текстовое поле заголовок обзора
    text = models.TextField() # создать текстовое поле с описанием машины

    def __str__(self): # для красивого вывода
        return str(self.car) + ' ' + self.title

