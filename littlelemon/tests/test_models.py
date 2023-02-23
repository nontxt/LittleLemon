from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def setUp(self):
        self.menu_item = Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_get_item(self):
        self.assertEqual(str(self.menu_item), "IceCream : 80")
