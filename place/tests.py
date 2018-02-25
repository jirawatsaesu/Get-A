from django.test import TestCase
from place.views import home_page, find_place 

class HomePageAndPlacePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')


    def test_uses_place_page_template(self):
        response = self.client.get('/place/')
        self.assertTemplateUsed(response, 'place.html')
