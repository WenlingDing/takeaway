from django.test import TestCase

# Create your tests here.
from .forms import OrderForm

class TestOrderForm(TestCase):

    def test_can_create_an_item_with_just_a_full_name(self):
        form = OrderForm({'full_name': 'Create Tests'})
        self.assertFalse(form.is_valid())
    
    def test_correct_message_for_missing_full_name(self):
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'], [u'This field is required.'])
        
    def test_can_create_an_item_with_just_a_phone_number(self):
        form = OrderForm({'phone_number': '000111'})
        self.assertFalse(form.is_valid())
    
    def test_correct_message_for_missing_a_phone_number(self):
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['phone_number'], [u'This field is required.'])
        
    def test_can_create_an_item_with_just_postcode(self):
        form = OrderForm({'postcode': '000111'})
        self.assertFalse(form.is_valid())
    
    def test_correct_message_for_missing_postcode(self):
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        
    def test_can_create_an_item_with_just_street_address1(self):
        form = OrderForm({'street_address1': 'bedok north st1'})
        self.assertFalse(form.is_valid())
    
    def test_correct_message_for_missing_street_address1(self):
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['street_address1'], [u'This field is required.'])
        
    def test_can_create_an_item_with_just_street_address2(self):
        form = OrderForm({'street_address2': 'bedok north st1'})
        self.assertFalse(form.is_valid())
    
    def test_correct_message_for_missing_street_address2(self):
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['street_address2'], [u'This field is required.'])
        
