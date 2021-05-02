from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Nft
from PIL import Image
import tempfile
from django.test import override_settings
from django.contrib.auth.models import User

# Helper function for to create a temp image for image test
def get_temporary_image(temp_file):
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    image.save(temp_file, 'png')
    return temp_file

# Home Page tests
class HomePageTest(TestCase):

    # Check the status code at home view
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    # Cannot upload without login
    def test_anonymous_cannot_see_page(self):
        response = self.client.get(reverse("upload"))
        self.assertRedirects(response, "/accounts/login/?next=/upload/")

    # Test redirecting to home.html and response that contain list of objects stored in nft
    def test_nft_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'just a test')
        self.assertTemplateUsed(response, 'home.html')

#Upload View Test
class HomePageTest(TestCase):
    
    # Setup object
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        
        self.nft = Nft.objects.create(
            title='Reminder: Start that business', 
            price='420.69', 
            tags="shopify", 
            uploaded_by=self.user,
        )

    # Check the content of title
    def test_title_content(self):
        nft = Nft.objects.get()
        expected_object_name = f'{nft.title}'
        self.assertEquals(expected_object_name, 'Reminder: Start that business')

    # Test price content
    def test_price_content(self):
        nft=Nft.objects.get()
        expected_object_name = f'{nft.price}'
        self.assertEqual(expected_object_name, '420.69')

    # Check the content of tags
    def test_title_content(self):
        nft = Nft.objects.get()
        expected_object_name = f'{nft.tags}'
        self.assertEquals(expected_object_name, 'shopify')

    #Check user login
    def test_title_content(self):
        nft = Nft.objects.get()
        expected_object_name = f'{nft.tags}'
        self.assertEquals(expected_object_name, 'shopify')

# Image upload test
class ImageUploadTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='dhrumil',
            email='test@email.com',
            password='iloveshopify'
        )
        
        self.assertTrue(self.client.login(username='dhrumil', password='iloveshopify'))

    # Changing media_root to a temp dir to prevent filiing our media dir with garbage
    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_image_upload(self):
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        image = Nft.objects.create(image=test_image.name, uploaded_by=self.user)
        self.assertEqual(len(Nft.objects.all()), 1)
    
    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_image_delete(self):
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        image = Nft.objects.create(image=test_image.name, uploaded_by=self.user, id=1)
        image.delete()
        self.assertEqual(len(Nft.objects.all()), 0)