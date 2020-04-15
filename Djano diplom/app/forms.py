# для создания форм у авторизации, регистрации и отзывах

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext, ugettext_lazy as _


class RegistrationForm(UserCreationForm): # форма для регистрации
    error_messages = { # выводит уведомление что пароли при регистрации совпадают
        'password_mismatch': _("Пароли не совпадают."),
    }
    first_name = forms.CharField(max_length=100, # поле Имя
                                 label=_("Имя пользователя:"),
                                 widget=forms.TextInput(
                                     attrs={'id': 'inputUsername',
                                            'class': 'form-control first-field',
                                            'placeholder': 'Имя',
                                            'value': '', # значение по умолчание
                                            'required': '',
                                            'autofocus': '',
                                            'data-cip-id': 'inputUsername'})
                                 )
    username = forms.EmailField(max_length=254, # поле Email
                                label=_("E-mail пользователя:"),
                                widget=forms.EmailInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Email',
                                           'value': '', # значение по умолчание
                                           'required': '',
                                           'data-cip-id': 'inputEmail'})
                                )
    password1 = forms.CharField(label=_("Придумайте пароль:"), # поле пароля
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Пароль', # отображается на страничке
                                           'required': '',
                                           'data-cip-id': 'inputPassword1'})
                                )
    password2 = forms.CharField(label=_("Подтвердите пароль:"), # поле подтверждения пароля, label не обязательно
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control last-field',
                                           'placeholder': 'Повторите пароль',
                                           'required': '',
                                           'data-cip-id': 'repeatPassword2'}),
                                help_text=_("Введите тот же пароль, что и ранее."))
    field_order = ['first_name', 'username', 'password1', 'password2']


class LoginForm(forms.Form): # форма для авторизации
    username = forms.EmailField(max_length=254, # поле Email
                                label=_("E-mail пользователя:"),
                                widget=forms.EmailInput(
                                    attrs={'class': 'form-control first-field',
                                           'placeholder': 'Email',
                                           'value': '', # значение по умолчание
                                           'required': '',
                                           'autofocus': '',
                                           'data-cip-id': 'inputEmail'})
                                )
    password = forms.CharField(label=_("Пароль:"), # поле пароля
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control last-field',
                                          'placeholder': 'Пароль', # отображается на страничке
                                          'required': '',
                                          'data-cip-id': 'inputPassword1'})
                               )
    field_order = ['username', 'password']


CHOICES=[('1', '1'), # строковое поле, предназначенное для выбора конкретного варианта из списка доступных вариантов.
         ('2', '2'),
         ('3', '3'),
         ('4', '4'),
         ('5', '5')]


class ReviewForm(forms.Form): # форма отзывов у конкретного товара
    name = forms.CharField(label=_("Имя:"), # поле Имя автора
                           widget=forms.TextInput(
                               attrs={'class': 'form-control',
                                      'aria-describedby': 'nameHelp',
                                      'placeholder': 'Представьтесь', # отображается на страничке
                                      'required': '',
                                      'data-cip-id': 'name'}),
                           )
    description = forms.CharField(label=_("Содержание"),
                                  widget=forms.Textarea(
                                      attrs={'class': 'form-control',
                                             'placeholder': 'Содержание', # отображается на страничке
                                             'required': '',
                                             'rows': '',
                                             'cols': ''}),
                                  )
    mark = forms.ChoiceField(choices=CHOICES, # поле Оценка, надо выбирать вариант из CHOICES
                             widget=forms.RadioSelect(
                                 attrs={'class': 'form-check-input'})
                             )
