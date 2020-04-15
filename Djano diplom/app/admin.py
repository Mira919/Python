# для настройки отображения админки

from django.contrib import admin
from .models import Section, Product, Article, Review, ReviewProductRelation, Order, OrderProductRelation


# @admin.register(ReviewProductRelation) # добавляем в админку промежуточную таблицу отзыв - товар
# class ReviewProductRelationAdmin(admin.ModelAdmin):
#     pass


class ReviewProductRelationInline(admin.TabularInline):
    model = ReviewProductRelation
    extra = 0


@admin.register(Section) # добавляем в админку Разделы
class SectionAdmin(admin.ModelAdmin):
    pass


@admin.register(Product) # добавляем в админку Товары
class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewProductRelationInline]


@admin.register(Article) # добавляем в админку Статьи
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Review) # добавляем в админку Отзывы
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderProductRelation) # добавляем в админку промежуточную таблицу заказ - товар
class OrderProductRelationAdmin(admin.ModelAdmin):
    pass


class OrderProductRelationInline(admin.TabularInline):
    model = OrderProductRelation
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductRelationInline]

