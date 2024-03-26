from django.test import TestCase
from .models import *
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils import timezone

class TestStorefront(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='tester',
            email='aik@yahoo.fr',
            password='secret'
        )
        self.customer = Customer.objects.create(
            name='test customer',
            phone_number='+9112345678',
            email='aik@yahoo.com',
            address='test address',
            city='test city',
        )
        self.item = Item.objects.create(
            title='test item',
            picture='test_picture.png',
            price=100.10,
            category='music',
            label='limited'
        )
        self.item_detail = Item_details.objects.create(
            item=self.item.title,
            description='test description',
            key_features='test key_features'
        )
        self.order_item = OrderItem.objects.create(item=self.item_detail.item)
        self.order = Order.objects.create(
            user=self.user,
            items=self.item_detail.item,
            start_date=timezone.now(),
            ordered_date=timezone.now(),
            ordered=False
        )
        #test if we make an inappropriate category, the count stays the same


