from book.models import Book, Categories

class NameDuplicate(Exception):
    def __init__(self, name):
        self.name = name


def create_books():
    f = open('data/all_book.txt', 'r')

    for line in f:
        all_book = [word for word in line.split('\t') if word not in '']         # Split name, score and categories
        all_book[1] = float(all_book[1])
        all_book[-1] = all_book[-1][:-1].split(',')                              # Delete /n and split category

        try:
            if Book.objects.filter(name__exact=all_book[0]):                     # Check for an existing book
                raise NameDuplicate(all_book[0])
            else:
                b = Book(name=all_book[0], score=all_book[1])
                b.save()

                for c in all_book[-1]:
                    if Categories.objects.filter(name__exact=c):                 # Check for an existing category
                        b.categories.add(Categories.objects.get(name=c))
                    else:
                        Categories(name=c).save()
                        b.categories.add(Categories.objects.get(name=c))

        except NameDuplicate as n:
            print('NameDuplicate: There is an existing ' + n.name + ' book')

    f.close()


def delete_all():
    Categories.objects.all().delete()
    Book.objects.all().delete()


def delete_books():
    Book.objects.all().delete()
