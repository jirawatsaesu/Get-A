from django.test import TestCase
from book.views import find_book
from book.models import Book, Categories

class BookPageTest(TestCase):

    def test_uses_book_page_template(self):
        response = self.client.get('/book/')
        self.assertTemplateUsed(response, 'book.html')

    def test_can_receive_a_GET_request(self):
        response = self.client.get('/book/book_name=A book&sport=Sport')
        self.assertIn('A book', response.content.decode())
        self.assertIn('Sport', response.content.decode())

    def test_can_search_books_by_categories(self):
        com = Categories()
        com.name = 'Computer'
        com.save()
        math = Categories()
        math.name = 'Math'
        math.save()

        first_book = Book()
        first_book.name = 'Data Structures and Algorithms in Python'
        first_book.score = 3.8
        first_book.save()
        first_book.categories.add(com)

        second_book = Book()
        second_book.name = 'Data Structures and Algorithms with Java'
        second_book.score = 4.0
        second_book.save()
        second_book.categories.add(com)

        third_book = Book()
        third_book.name = 'Discrete Math'
        third_book.score = 4.5
        third_book.save()
        third_book.categories.add(com, math)

        fourth_book = Book()
        fourth_book.name = 'Math II'
        fourth_book.score = 3.0
        fourth_book.save()
        fourth_book.categories.add(math)

        fifth_book = Book()
        fifth_book.name = 'A byte of Python'
        fifth_book.score = 3.5
        fifth_book.save()
        fifth_book.categories.add(com)

        saved_cat = Categories.objects.all()
        self.assertEqual(saved_cat[0], com)
        self.assertEqual(saved_cat[1], math)

        saved_book = Book.objects.all()
        self.assertEqual(saved_book.count(), 5)

        search_book = Book.objects.filter(name__contains="Data")
        self.assertEqual(search_book.count(), 2)

        search_cate = Categories.objects.filter(name__contains="Com")[0]
        self.assertEqual(search_cate.book_set.all().count(), 4)

        book_in_cate = search_cate.book_set.filter(name__contains="Data")
        self.assertEqual(search_book.count(), 2)

        book_in_two_cate = Book.objects.filter(name__contains="Discrete")[0]
        self.assertEqual(book_in_two_cate.categories.all().count(), 2)
