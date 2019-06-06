from django.shortcuts import get_object_or_404
from takeaway_app.models import Food


def cart_contents(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    food_count = 0
    
    for id, quantity in cart.items():
        food = get_object_or_404(Food, pk=id)
        total += quantity * food.price
        food_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'food': food})
    
    return {'cart_items': cart_items, 'total': total, 'food_count': food_count}