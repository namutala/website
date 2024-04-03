from django.test import TestCase
from .models import service, booking
from django.contrib.auth import get_user_model

class ServiceTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='aik@yahoo.fr',
            password='secret'
        )
        self.service = service.objects.create(
            service_name="test",
            service_description="test description",
            service_prices="100",
            location="test location",
            Contact=256,
            image1="test_image1.png",
        )
        self.booking = booking.objects.create(
            customer=self.user,
            service_booked=self.service,
        )
    def test_service_creation(self):
        self.service.save()
        latest_service = service.objects.latest('id')
        self.assertEqual(latest_service.service_name, "test")
        self.assertEqual(latest_service.service_description, "test description")
    def test_booking_creation(self):
        self.service.save()
        self.booking.save()
        latest_service = service.objects.latest('id')
        latest_booking = booking.objects.latest('id')
        self.assertEqual(latest_booking.service_booked, self.service)

