from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='dhrumil',
            email='dhrumil@test.com',
            password='iloveshopify'
        )

    def test_login(self):
        self.assertEqual(self.user.username, 'dhrumil')
        self.assertTrue(self.user.is_authenticated)
        self.assertTrue(self.client.login(username='dhrumil', password='iloveshopify'))
        self.assertFalse(self.client.login(username='dhrumil', password='startthatbusiness'))

    def test_logout(self):
        self.client.logout()
        self.assertTrue(self.user.is_authenticated)