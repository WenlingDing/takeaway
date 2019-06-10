from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.

class Menu(models.Model):
	name = models.CharField(blank=False,max_length=255)
	def __str__(self):
		return self.name

class Food(models.Model):
	name = models.CharField(blank=False,max_length=255)
	price = models.IntegerField(default=0)
	photo = ImageField(blank=True)
	description = models.TextField(blank=True)
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='food_menu', null=True)

	def __str__(self):
		return self.name
	
		