from django.shortcuts import render
from book.models import Book, Categories

def find_book(request):
    if request.method == 'GET':
        cate_name1 = request.GET.get('com', '')
        cate_name2 = request.GET.get('math', '')
        cate_name3 = request.GET.get('phy', '')
        cate_name4 = request.GET.get('sport', '')
        search_name = request.GET.get('book_name', '')

        if cate_name1 != '' or cate_name2 != '' or cate_name3 != '' or cate_name4 != '':
            if cate_name1 != '':
                cates_list = Categories.objects.filter(name__contains=cate_name1)[0]
                book_list1 = cates_list.book_set.filter(name__contains=search_name)
            else:
                book_list1 = Book.objects.none()
            if cate_name2 != '':
                cates_list = Categories.objects.filter(name__contains=cate_name2)[0]
                book_list2 = cates_list.book_set.filter(name__contains=search_name)
            else:
                book_list2 = Book.objects.none()
            if cate_name3 != '':
                cates_list = Categories.objects.filter(name__contains=cate_name3)[0]
                book_list3 = cates_list.book_set.filter(name__contains=search_name)
            else:
                book_list3 = Book.objects.none()
            if cate_name4 != '':
                cates_list = Categories.objects.filter(name__contains=cate_name4)[0]
                book_list4 = cates_list.book_set.filter(name__contains=search_name)
            else:
                book_list4 = Book.objects.none()

            books = book_list1 | book_list2 | book_list3 | book_list4
            return render(request, 'book.html', {'books': books})

        if search_name != '':
            books = Book.objects.filter(name__contains=search_name)
            return render(request, 'book.html', {'books': books})

    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})
