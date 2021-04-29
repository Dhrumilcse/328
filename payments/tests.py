from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.
class BuyViewTest(TestCase):

    #Only loggedin users can see buy page
    def test_authenticated_user_can_see_page(self):
        user = User.objects.create_user("dhrumil" "dhrumilcse14@gmail.com", "origami")
        self.client.force_login(user=user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)