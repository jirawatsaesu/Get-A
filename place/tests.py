from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from place.views import home_page, find_place 

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_url_resolves_to_place_page_view(self):
        found = resolve('/place/')
        #self.assertEqual(found.func, find_place)
