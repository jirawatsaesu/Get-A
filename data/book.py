from book.models import Book, Categories
 
categories = [
'Computer',
'Math',
'Physic',
'Sport',
]

# [Category, Name, Score]
#books = [
#['Computer', 'Data Structures and Algorithms', 4.5],
#['Computer', 'Data Structures and Algorithms in Python', 3.8],
#['Computer', 'Data Structures and Algorithms with Java', 4.0],
#['Math', 'Math II', 3.0],
#['Computer', 'A Byte of Python', 3.5],
#]

def create_categories():
    global categories

    for category in categories:
        Categories(name=category).save()


def create_books():
    global books

    f = open('data/all_book.txt', 'r')

    for line in f:
        all_book = [b for b in line.split('\t') if b not in '']
        all_book[2] = float(all_book[-1][:-1])    #delete \n

        Categories.objects.get(name=all_book[0]).book_set.create(name=all_book[1], score=all_book[2])

    f.close()


def create_all():
    create_categories()
    create_books()


def delete_all():
    Categories.objects.all().delete()
    Book.objects.all().delete()



