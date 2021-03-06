from django.db import models
from takeaway_app.models import Food
from datetime import datetime


# Create your models here.
class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=True)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Order - " + str(self.id)

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    food = models.ForeignKey(Food, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.food.name, self.food.price)
