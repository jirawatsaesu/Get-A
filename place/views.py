from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def find_place(request):
    return render(request, 'place.html')
