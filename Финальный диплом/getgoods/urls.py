"""getgoods URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.reverse import reverse
from rest_framework.routers import DefaultRouter

from app.views import APICategoryViewSet, APIParameterViewSet, APIProductViewSet, APIProductParameterViewSet, \
    RegisterUserView, RecoverUserView, ResetUserView, RegisterStoreView, PriceView, StorePriceView, OrderView, \
    StoreOrderView, TestView

router = DefaultRouter()
router.register('category', APICategoryViewSet)
router.register('parameter', APIParameterViewSet)
router.register('product', APIProductViewSet)
router.register('productparameter', APIProductParameterViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include((router.urls, 'app'))),
    path('admin-getgoods/user/', RegisterUserView.as_view(), name='admin-user'),
    path('admin-getgoods/recover/', RecoverUserView.as_view(), name='admin-recover'),
    path('admin-getgoods/reset/', ResetUserView.as_view(), name='admin-reset'),
    path('admin-getgoods/store/', RegisterStoreView.as_view(), name='admin-store'),
    path('price/', PriceView.as_view(), name='price'),
    path('price/<int:store_id>', PriceView.as_view(), name='price'),
    path('store-price/', StorePriceView.as_view(), name='store-price'),
    path('order/', OrderView.as_view(), name='order'),
    path('store-order/', StoreOrderView.as_view(), name='store-order'),
    path('', TestView.as_view(), name='test')
]
