from django.shortcuts import render, get_object_or_404,  redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from takeaway_app.models import Food
import stripe
from takeaway_app.views import index

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                food = get_object_or_404(Food, pk=id)
                total += quantity * food.price
                order_line_item = OrderLineItem(
                    order=order,
                    food=food,
                    quantity=quantity
                )
                order_line_item.save()
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="sgd",
                    description=request.user.email,
                    source = request.POST.get('stripe_id')
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(index)
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = PaymentForm()
        order_form = OrderForm()
    
    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, 'stripe_publishable_key':settings.STRIPE_PUBLISHABLE_KEY})

