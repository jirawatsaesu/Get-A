from django.test import TestCase
from book.views import find_book

class BookPageTest(TestCase):

    def test_book_page_returns_correct_html(self):
        response = self.client.get('/book/')
        self.assertTemplateUsed(response, 'book.html')
