from django.test import TestCase
from book.views import find_book

class BookPageTest(TestCase):

    def test_uses_book_page_template(self):
        response = self.client.get('/book/')
        self.assertTemplateUsed(response, 'book.html')

    def test_can_save_a_GET_request(self):
        response = self.client.get('/book/book_name=A book&sport=Sport')
        self.assertIn('A book', response.content.decode())
        self.assertIn('Sport', response.content.decode())
