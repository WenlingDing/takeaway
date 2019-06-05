from django.shortcuts import render, get_object_or_404
from .models import Menu, Food
from .forms import  FoodForm

def index(request):
    return render(request, 'index.html')

def menu(request, menu_name):
    menu = Menu.objects.get(name=menu_name)
    food_list = list(Food.objects.filter(menu__name=menu_name))[:9]
    return render(request, 'menu.html', {
        'menu': menu,
        'food_list': food_list,
        })

def food_detail(request, PK):
    menu = secondMenu.objects.get(name=menu_name)
    food_list = list(Food.objects.filter(menu__name=menu_name))
    return render(request, 'detail.html', {
        'menu': menu,
        'food_list': food_list
        })
        
def food(request, food_name):
    food = Food.objects.get(name=food_name)
    form = CommentForm()
    comment_list = food.comment_set.all()
    comments = list(comment_list)
    # for comment in comment_list:
    #     username = str(User.objects.get(username=comment.user))
    #     comments.append(username)
    return render(request, 'takeout/food.html', {
        'food': food,
        'form': form,
        'comments': comments
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

