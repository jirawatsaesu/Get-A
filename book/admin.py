from django.contrib import admin

from .models import Book, Categories

class BookInline(admin.StackedInline):
    model = Book
    extra = 3

class CategoriesAdmin(admin.ModelAdmin):
    inlines = [BookInline]

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Book)
