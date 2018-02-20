from django.test import TestCase
from place.views import home_page, find_place 

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


    def test_place_page_returns_correct_html(self):
        response = self.client.get('/place/')
        self.assertTemplateUsed(response, 'place.html')
