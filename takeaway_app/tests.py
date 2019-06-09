from django.test import TestCase
from .models import Menu, Food

# Create your tests here.
# test models
class MenuTest(TestCase):
    
    def testCanCreateMenu(self):
        menuName = Menu(name="vagen")
        menuName.save()
        
        menu_name_from_db = Menu.objects.all().get(pk=menuName.id)
        self.assertEqual(menu_name_from_db.name, "vagen")
        self.assertEqual(menu_name_from_db.id, menuName.id)
     
class FoodTest(TestCase):
    
    def testCanCreateFood(self):
        foodName = Food(name="tomato")
        foodName.save()
        
        food_name_from_db = Food.objects.all().get(pk=foodName.id)
        self.assertEqual(food_name_from_db.name, "tomato")
        self.assertEqual(food_name_from_db.id, foodName.id)
        
    def test_can_create_an_item_with_a_name_and_price(self):
        item = Food(name="Create a Test", price="10")
        item.save()
        self.assertEqual(item.name, "Create a Test")
        self.assertTrue(item.price)   
        
    def test_can_create_an_item_with_a_name_and_price_and_description(self):
        item = Food(name="juice", price="10", description="very nice")
        item.save()
        self.assertEqual(item.name, "juice")
        self.assertTrue(item.price)  
        self.assertEqual(item.price, "10")
        self.assertTrue(item.description,"very nice")  


