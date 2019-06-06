from django.shortcuts import render, get_object_or_404, redirect
from .models import Menu, Food
from .forms import  FoodForm
from django.db.models import Q
from django import template

def index(request):
    food = Food.objects.all()
    menu = Menu.objects.all()
    return render(request, 'index.html', {
        'food':food,
        'menu':menu
    })
    
def menu(request,id):
    menu = Menu.objects.get(id=Menu.id)
    menu_list = Food.objects.all()
    return render(request, 'menu.html', {
        'menu': menu,
        'menu_list': menu_list,
        })

def food_detail(request,id):
    food_detail = Food.objects.get(id=id)
    return render(request, 'detail.html',{
        'food_detail': food_detail,
    })

def search(request):
    food = Food.objects.filter(name__icontains=request.GET['q'])
    return render(request, "index.html", {"food": food})
    