from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Business

class BusinessTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='aik@yahoo.fr',
            password='secret'
        )
        self.business = Business.objects.create(
            owner=self.user,
            business_name='tester',
            logo='test_logo.png',
            business_description='Busineess description test',
            location='test location',
            email='aik@yahoo.com',
            contact=12345
        )
    def test_business_creation(self):
        self.business.save()
        self.assertEqual(self.business.owner, self.user)
        self.assertEqual(self.business.business_name, 'tester')
        self.assertEqual(self.business.logo, 'test_logo.png')

