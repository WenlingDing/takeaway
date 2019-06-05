from django import forms
from .models import Menu,Food

class MenuForm(forms.ModelForm):
    
    class Meta:
        model = Menu
        fields = ('name')

class FoodForm(forms.ModelForm):
    
    class Meta:
        model = Food
        fields = ('name', 'price', 'image', 'description', 'menu')
    
