from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Nft

# Home Page tests
class HomePageTest(TestCase):

    # Setup object
    def setUp(self):
        Nft.objects.create(title='just a test', price='45.9', image="media/csgo.png")

    # Check the status code at home view
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Check the content of title
    def test_title_content(self):
        nft = Nft.objects.get(id=1)
        expected_object_name = f'{nft.title}'
        self.assertEquals(expected_object_name, 'just a test')

    # Test price content
    def test_price_content(self):
        nft=Nft.objects.get(id=1)
        expected_object_name = f'{nft.price}'
        self.assertEqual(expected_object_name, '45.90')

    # Test redirecting to home.html and response that contain list of objects stored in nft
    def test_nft_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'just a test')
        self.assertTemplateUsed(response, 'home.html')

    