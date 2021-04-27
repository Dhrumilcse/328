from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Nft

# Create your tests here.
class HomePageTest(TestCase):

    def setUp(self):
        Nft.objects.create(title='just a test', price="45.9", image="media/csgo.png")

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_title_content(self):
        nft = Nft.objects.get(id=1)
        expected_object_name = f'{nft.title}'
        self.assertEquals(expected_object_name, 'just a test')

    def test_nft_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'just a test')
        self.assertTemplateUsed(response, 'home.html')