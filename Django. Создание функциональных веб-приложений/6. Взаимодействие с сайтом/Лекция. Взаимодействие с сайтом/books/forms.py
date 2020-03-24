from django import forms

from books.models import Book


class BookForm(forms.ModelForm):

    year = forms.IntegerField() # поле year может быть только числовое

    class Meta:
        model = Book # к какой модели эту форму описываем
        fields = ('name', 'year', 'authors',)

    def clean_year(self): # проверка что книга не старее 1900 года
        year = self.cleaned_data['year']
        if year < 1900:
            raise forms.ValidationError('Допустимы только соврменные книги') # выдаст сообщение
        return year