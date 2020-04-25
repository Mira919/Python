# для создания моделей (таблиц) БД и связи между ними
from django.contrib.auth.models import User
from django.db import models

ORDER_STATUS = (
    ('new', 'новый'),
    ('processing', 'обработка'),
    ('executed', 'выполнен'),
    ('error', 'ошибка')
)


class Store(models.Model): # Таблица магазинов
    name = models.CharField(max_length=255) # название магазина
    user = models.OneToOneField(User, on_delete=models.PROTECT) # владелец магазина, у одного магазина один владелец

    class Meta:
        verbose_name = 'Магазин' # как отображается в админке
        verbose_name_plural = "Список магазинов" # как отображается в админке
        ordering = ('name',) # сортируем по имени

    def __str__(self): # как выводится
        return self.name


class Category(models.Model): # Таблица категорий
    name = models.CharField(max_length=255) # название категории

    class Meta:
        verbose_name = 'Категория' # как отображается в админке
        verbose_name_plural = "Список категорий" # как отображается в админке
        ordering = ('name',) # сортируем по имени

    def __str__(self): # как выводится
        return self.name


class Product(models.Model): # таблица товаров
    name = models.CharField(max_length=255) # название товара
    category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True) # категория товара, связь о-м с таблицой категорий

    class Meta:
        verbose_name = 'Товар' # как отображается в админке
        verbose_name_plural = "Список товаров" # как отображается в админке
        ordering = ('-name',) # сортируем по имени

    def __str__(self): # как выводится
        return self.name


class PriceItem(models.Model): # Таблица позиции прайс листа товара
    product = models.ForeignKey(Product, on_delete=models.PROTECT) # товар, связь о-м с таблицой товаров
    quantity = models.PositiveIntegerField() # количество
    cost = models.FloatField() # цена

    class Meta:
        verbose_name = 'Позиция прайс-листа' # как отображается в админке
        verbose_name_plural = "Список позиций прайс-листов" # как отображается в админке

    def __str__(self): # как выводится
        return f'{self.product} ({self.quantity} x {self.cost})'


class Price(models.Model): # Таблица Прайс листа
    store = models.ForeignKey(Store, on_delete=models.PROTECT) # магазин, связь о-м с таблицой магазинов
    date = models.DateTimeField(auto_now_add=True, auto_now=False) # дата
    price_items = models.ManyToManyField(PriceItem) # стоимость товаров, связь м-м с таблицой позиции прайс листа товаров

    class Meta:
        verbose_name = 'Прайс-лист' # как отображается в админке
        verbose_name_plural = "Прайс-листы" # как отображается в админке
        ordering = ('-date',) # сортируем по дате

    def __str__(self): # как выводится
        return f'{self.store.name} price'


class Parameter(models.Model): # Таблица характеристик
    name = models.CharField(max_length=255) # название параметра

    class Meta:
        verbose_name = 'Параметр товара' # как отображается в админке
        verbose_name_plural = "Список параметров товаров" # как отображается в админке

    def __str__(self): # как выводится
        return self.name


class ProductParameter(models.Model): # Таблица характеристики товара
    product = models.ForeignKey(Product, on_delete=models.PROTECT) # товар, связь о-м с таблицой товаров
    parameter = models.ForeignKey(Parameter, on_delete=models.PROTECT) # параметр, связь о-м с таблицой Параметров
    value = models.CharField(max_length=255) # значение

    class Meta:
        verbose_name = 'Характеристики товара' # как отображается в админке
        verbose_name_plural = "Список характеристик товаров" # как отображается в админке

    def __str__(self): # как выводится
        return f'{self.product.name} ({self.parameter.name}={self.value})'


class OrderItem(models.Model): # Таблица позиции заказов
    product = models.ForeignKey(Product, on_delete=models.PROTECT) # товар, связь о-м с таблицой товаров
    quantity = models.PositiveIntegerField() # количество
    cost = models.FloatField() # цена

    class Meta:
        verbose_name = 'Позиция заказа' # как отображается в админке
        verbose_name_plural = "Список позиций заказов" # как отображается в админке


class Order(models.Model): # Таблица заказов
    user = models.ForeignKey(User, on_delete=models.PROTECT) # владелец магазина, связь о-м с таблицой пользователей
    store = models.ForeignKey(Store, on_delete=models.PROTECT) # название магазина, связь о-м с таблицой магазинов
    date = models.DateTimeField(auto_now_add=True, auto_now=False) # дата заказа
    order_items = models.ManyToManyField(OrderItem) # позиция заказа, связь м-м с таблицой позиции заказов
    status = models.CharField(max_length=255, choices=ORDER_STATUS, default='new') # статус заказа

    class Meta:
        verbose_name = 'Заказ' # как отображается в админке
        verbose_name_plural = "Список заказов" # как отображается в админке
        ordering = ('-date',) # сортируем по дате

    def __str__(self): # как выводится
        return f'{self.store.name} - {self.user.username} order'

