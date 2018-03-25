from django.contrib import admin

from .models import Book, Categories

admin.site.register(Categories)
admin.site.register(Book)
