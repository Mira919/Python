"""online_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls), # переводит на страницу админа
    path('', views.main_view, name='main'), # переводит на главную страницу
    path('login/', views.login_view, name='login'), # переводит на страницу входа в учетку
    path('logout/', views.logout_view, name='logout'), # выходит из учетки пользователя
    path('signup/', views.signup_view, name='signup'), # переводит на регистрацию
    path('add_to_cart/<product_id>/', views.add_to_cart_view, name='add_to_cart'), # добавление товара в корзину
    path('cart/', views.show_cart_view, name='cart'), # переводит в корзину
    path('<section>/', views.show_section_view, name='section'), # показ какого - либо раздела и пагинация раздела
    path('<section_slug>/<product_slug>/', views.show_product_view, name='product'), # показ информации и отзывы о товаре
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # подключаем статику
