from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class BuyViewTest(TestCase):
    """ Test Cases for Buy View 
    
    Methods
    -------
    test_authenticated_user_can_see_page(self)
        Returns True if authenticated user can see page
    """

    def test_authenticated_user_can_see_page(self):
        """ Returns True if authenticated user can see page"""
        
        user = User.objects.create_user("dhrumil" "dhrumilcse14@gmail.com", "origami")
        self.client.force_login(user=user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)