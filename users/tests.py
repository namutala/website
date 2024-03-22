from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Profile

class ProfileTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='aik@yahoo.fr',
            password='secret'
        )
        self.profile = Profile.objects.create(
            user= self.user,
            image='test.png',
            Bio='This is a test bio.'
        )

    def test_profile_creation(self):
        self.profile.save()
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.image, 'test.png')
        self.assertEqual(self.profile.Bio, 'This is a test bio.')

    def test_save_profile(self):
        self.profile.save()
        query_from_db = Profile.objects.get(user=self.user)
        self.assertEqual(query_from_db.user, self.profile)
        self.assertEqual(query_from_db.image, 'test.png')
        self.assertEqual(query_from_db.Bio, 'This is a test bio.')

