from django.shortcuts import render, redirect
from takeaway_app.views import index
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")

@login_required
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

    request.session['cart'] = cart
    return redirect('index')

    
@login_required
def adjust_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect('view_cart')


