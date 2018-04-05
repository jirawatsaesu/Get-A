import csv
from book.models import Book, Categories


class NameDuplicate(Exception):
    def __init__(self, name):
        self.name = name


def create_books():
    with open('data/all_book.csv', 'r') as f:
        reader = csv.reader(f)
        for book_detail in reader:
            book_name = book_detail[0]
            book_score = float(book_detail[1])
            book_cat = book_detail[-1].split(',')                                # Split category

            try:
                if Book.objects.filter(name__exact=book_name):                   # Check for an existing book
                    raise NameDuplicate(book_name)
                else:
                    b = Book(name=book_name, score=book_score)
                    b.save()

                    for c in book_cat:
                        if Categories.objects.filter(name__exact=c):             # Check for an existing category
                            b.categories.add(Categories.objects.get(name=c))
                        else:
                            Categories(name=c).save()
                            b.categories.add(Categories.objects.get(name=c))

            except NameDuplicate as n:
                print('NameDuplicate: There is an existing ' + n.name + ' book')


def delete_all():
    Categories.objects.all().delete()
    Book.objects.all().delete()


def delete_books():
    Book.objects.all().delete()
