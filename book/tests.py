from django.test import TestCase
from book.views import find_book

class BookPageTest(TestCase):

    def test_uses_book_page_template(self):
        response = self.client.get('/book/')
        self.assertTemplateUsed(response, 'book.html')
