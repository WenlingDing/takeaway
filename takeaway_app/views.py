from django.shortcuts import render, get_object_or_404
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
    
def menu(request, menu_name):
    menu = Menu.objects.get(name=menu_name)
    menu_list = list(Food.objects.filter(menu__name=menu_name))
    return render(request, 'menu.html', {
        'menu': menu,
        'menu_list': menu_list,
        })

def food_detail(request, PK):
    menu = Menu.objects.get(name=menu_name)
    food_list = list(Food.objects.filter(menu__name=menu_name))
    return render(request, 'detail.html', {
        'menu': menu,
        'food_list': food_list
        })
        
def food(request, food_name):
    food = Food.objects.get(name=food_name)
    return render(request, 'food.html', {
        'food': food,
        })

def search(request):
    q = request.GET.get('q')
    error_msg = ''
    if not q:
        error_msg = ''
        return render(request, 'search.html', {'error_msg': error_msg})
    food_list = Food.objects.filter(Q(name__icontains=q))
    error_msg = 'Sorry we have not this food' if not food_list else 'you want all here '
    return render(request, 'search.html', {
        'food_list': food_list,
        'error_msg': error_msg
        })

