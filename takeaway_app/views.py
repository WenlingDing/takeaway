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
