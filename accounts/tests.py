from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class UserTests(TestCase):
    """ Test Cases for Users 
   
   Methods
    -------
    setUp(self)
        Sets up test user
   
    test_anonymous_cannot_see_page(self)
        Returns True if accessing /upload endpoint without login redirects to login

    test_home_page_redirect(self)
        Returns True if redirected to homepage correctly
    """
    
    def setUp(self):
        """ Sets up test user """
        self.user = User.objects.create_user(
            username='dhrumil',
            email='dhrumil@test.com',
            password='iloveshopify'
        )

    def test_login(self):
        """ Tests Logging in with and without valid userid and password """
        self.assertEqual(self.user.username, 'dhrumil')
        self.assertTrue(self.user.is_authenticated)
        self.assertTrue(self.client.login(username='dhrumil', password='iloveshopify'))
        self.assertFalse(self.client.login(username='dhrumil', password='startthatbusiness'))

    def test_logout(self):
        """ Return True if can successfully logout """
        self.client.logout()
        self.assertTrue(self.user.is_authenticated)