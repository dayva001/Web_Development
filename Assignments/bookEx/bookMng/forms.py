from django import forms
from django.forms import ModelForm
from .models import Book, BookRating


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]


class RateBook(ModelForm):
    class Meta:
        model = BookRating
        fields = [
            'book_id',
            'rating',
            'user_id',
        ]
