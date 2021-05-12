from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Nft
from PIL import Image
import tempfile
from django.test import override_settings
from django.contrib.auth.models import User

def get_temporary_image(temp_file):
    """ Returns a temporary image.png with size 200x200 """
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    image.save(temp_file, 'png')
    return temp_file

class HomePageTest(TestCase):
    """ Test Cases for Home Page 
    
    Methods
    -------
    test_home_page_status_code(self)
        Returns True if Status code is 200 OK
   
    test_anonymous_cannot_see_page(self)
        Returns True if accessing /upload endpoint without login redirects to login

    test_home_page_redirect(self)
        Returns True if redirected to homepage correctly
    """

    def test_home_page_status_code(self):
        """ Returns True if Status code is 200 OK """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_anonymous_cannot_see_page(self):
        """ Returns True if accessing /upload endpoint without login redirects to login """
        response = self.client.get(reverse("upload"))
        self.assertRedirects(response, "/accounts/login/?next=/upload/")

    def test_home_page_redirect(self):
        """ Returns True if redirected to homepage correctly """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

class ModelTest(TestCase):
    """ Test Cases for Model 
    
    Methods
    -------
    setUp(self)
        Sets up test user and add test data to the model 
   
    test_title_content(self)
        Returns True if successfully retrieves title

    test_price_content(self)
        Returns True if successfully retrieves price

    test_tags_content(self)
        Returns True if successfully retrieves tags
    
    test_user_login(self)
        Returns True if if user can log-in
    """
   
    def setUp(self):
        """ Sets up test user and add test data to the model """

        self.user = User.objects.create_user(
            username='dhrumil',
            email='test@email.com',
            password='iloveshopify'
        )
        
        self.nft = Nft.objects.create(
            title='Reminder: Start that business', 
            price='420.69', 
            tags="shopify", 
            uploaded_by=self.user,
        )

    def test_title_content(self):
        """ Returns True if successfully retrieves title """
        nft = Nft.objects.get()
        expected_object_name = f'{nft.title}'
        self.assertEquals(expected_object_name, 'Reminder: Start that business')

    def test_price_content(self):
        """ Returns True if successfully retrieves price """
        nft=Nft.objects.get()
        expected_object_name = f'{nft.price}'
        self.assertEqual(expected_object_name, '420.69')

    def test_tags_content(self):
        """ Returns True if successfully retrieves tags """
        nft = Nft.objects.get()
        expected_object_name = f'{nft.tags}'
        self.assertEquals(expected_object_name, 'shopify')

    def test_user_login(self):
        """ Returns True if if user can log-in """
        self.assertTrue(self.client.login(username='dhrumil', password='iloveshopify'))

class ImageTest(TestCase):
    """ Test Cases for Image 
    
    Methods
    -------
    setUp(self)
        Sets up test user and log-in (required for image upload and delete)

    test_image_upload(self)
        Returns True if Image can be successfully uploaded
    
    test_image_delete(self)
        Returns True if Image can be successfully deleted

    """

    def setUp(self):
        """ Sets up test user and log-in (required for image upload and delete) """
        self.user = User.objects.create_user(
            username='dhrumil',
            email='test@email.com',
            password='iloveshopify'
        )
        
        self.assertTrue(self.client.login(username='dhrumil', password='iloveshopify'))

    # Changing media_root to a temp dir to prevent filiing our media dir with garbage
    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_image_upload(self):
        """ Returns True if Image can be successfully uploaded """
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        image = Nft.objects.create(image=test_image.name, uploaded_by=self.user)
        self.assertEqual(len(Nft.objects.all()), 1)
    
    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_image_delete(self):
        """ Returns True if Image can be successfully deleted """
        temp_file = tempfile.NamedTemporaryFile()
        test_image = get_temporary_image(temp_file)
        image = Nft.objects.create(image=test_image.name, uploaded_by=self.user, id=1)
        image.delete()
        self.assertEqual(len(Nft.objects.all()), 0)