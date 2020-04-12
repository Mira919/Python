from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import render, redirect


def logout_view(request): # функция выхода пользователя из учетки
    auth.logout(request)
    return redirect('main')


def main_view(request):
    template = 'shop/base.html'
    context = {}
    return render(request, template, context)


def show_cart_view(request): # функция показа корзины
    template = 'shop/cart.html'
    context = {}
    return render(request, template, context)