from django.test import TestCase
from book.views import find_book
from book.models import Book

class BookPageTest(TestCase):

    def test_uses_book_page_template(self):
        response = self.client.get('/book/')
        self.assertTemplateUsed(response, 'book.html')

    def test_can_receive_a_GET_request(self):
        response = self.client.get('/book/book_name=A book&sport=Sport')
        self.assertIn('A book', response.content.decode())
        self.assertIn('Sport', response.content.decode())

    def test_can_search_books(self):
        first_book = Book()
        first_book.name = 'Data Structures and Algorithms in Python'
        first_book.score = 4.5
        first_book.save()

        second_book = Book()
        second_book.name = 'Data Structures and Algorithms with Java'
        second_book.score = 4.0
        second_book.save()

        third_book = Book()
        third_book.name = 'Data Structures and Algorithms'
        third_book.score = 3.8
        third_book.save()

        fourth_book = Book()
        fourth_book.name = 'Math II'
        fourth_book.score = 3.0
        fourth_book.save()

        saved_book = Book.objects.all()
        self.assertEqual(saved_book.count(), 4)

        search_book = Book.objects.filter(name__contains="Data")
        self.assertEqual(search_book.count(), 3)
