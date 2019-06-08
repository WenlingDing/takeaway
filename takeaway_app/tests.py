from django.test import TestCase
from .models import Menu, Food

# Create your tests here.
class TestDjango(TestCase):
    def test_is_this_thing_on(self):
        self.assertEqual(1,1)
         
class 