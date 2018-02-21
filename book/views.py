from django.shortcuts import render

def find_book(request):
    return render(request, 'book.html')
