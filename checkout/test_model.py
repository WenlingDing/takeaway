from django.test import TestCase

# Create your tests here.

from .models import Order, OrderLineItem

# Create your tests here.
class OrderTest(TestCase):
    
    def testCanCreateOrderByName(self):
        full_name = Order(full_name="Alex Wang")
        full_name.save()
        
        full_name_from_db = Order.objects.all().get(pk=full_name.id)
        self.assertEqual(full_name_from_db.full_name, "Alex Wang")
        self.assertEqual(full_name_from_db.id, full_name.id)
     
    def testCanCreateOrderByPhone(self):
        test_phone = Order(phone_number="99990000")
        test_phone.save()
        
        test_phone_from_db = Order.objects.all().get(pk=test_phone.id)
        self.assertEqual(test_phone_from_db.phone_number, "99990000")
        self.assertEqual(test_phone_from_db.id, test_phone.id)
        
    def testCanCreateOrderByCountry(self):
        test_country = Order(country="Singapore")
        test_country.save()
        
        test_country_from_db = Order.objects.all().get(pk=test_country.id)
        self.assertEqual(test_country_from_db.country, "Singapore")
        self.assertEqual(test_country_from_db.id, test_country.id)

    def testCanCreateOrderByPostcode(self):
        test_postcode = Order(postcode="000000")
        test_postcode.save()
        
        test_postcode_from_db = Order.objects.all().get(pk=test_postcode.id)
        self.assertEqual(test_postcode_from_db.postcode, "000000")
        self.assertEqual(test_postcode_from_db.id, test_postcode.id)

