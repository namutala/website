from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class RegistrationTest(TestCase):
    def test_register_link_exists(self):
        response = self.client.get(reverse("site-home"))
        self.assertEqual(response.status_code, 200)
