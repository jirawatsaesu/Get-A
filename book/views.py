from django.shortcuts import render
from book.models import Book

def find_book(request):
    if request.method == 'GET':
        books = Book.objects.filter(name__contains=request.GET.get('book_name', ''))
        return render(request, 'book.html', {'books': books})

    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})
