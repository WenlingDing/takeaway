from django.shortcuts import render, get_object_or_404, redirect
from .models import Menu, Food
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
# to show the menu button list
    menu = Menu.objects.all()
# to get foods for each menu 
    food_menu = Menu.objects.get(id=id)
    menu_list=food_menu.food_menu.all()
    return render(request, 'menu.html', {
        'menu_list': menu_list,
        'menu':menu
        })

def food_detail(request,id):
    food_detail = Food.objects.get(id=id)
    menu = Menu.objects.all()
    return render(request, 'detail.html',{
        'food_detail': food_detail,
        'menu':menu
    })

def search(request):
    food = Food.objects.filter(name__icontains=request.GET['q'])
    menu = Menu.objects.all()
    return render(request, "search.html", {
        "food": food,
        'menu':menu
    })
    