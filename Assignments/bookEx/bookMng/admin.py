from django.contrib import admin

# Register your models here.

from .models import MainMenu, BookRating, Book

admin.site.register(MainMenu)
admin.site.register(Book)
admin.site.register(BookRating)
