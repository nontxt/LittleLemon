import json
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from restaurant.models import Menu


class MenuViewTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = Menu.objects.create(title="Pasta", price=90, inventory=50)

    def test_get_all(self):
        response = self.client.get(reverse('menu'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = [
            {'id': self.item1.id, 'title': 'IceCream', 'price': '80.00', 'inventory': 100},
            {'id': self.item2.id, 'title': 'Pasta', 'price': '90.00', 'inventory': 50},
        ]

        self.assertEqual(json.loads(response.content), expected_data)

    def test_retrieve(self):
        response = self.client.get(reverse('menu', args=[self.item1.id]), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        expected_data = {
            'id': self.item1.id,
            'title': 'IceCream',
            'price': '80.00',
            'inventory': 100,
        }

        self.assertEqual(json.loads(response.content), expected_data)
