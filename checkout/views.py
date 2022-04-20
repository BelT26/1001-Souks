# adapted from Boutique Ado project
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents

import stripe

def checkout(request):
    """
    returns an order form so that the user
    can complete checkout. redirects user to
    home page if their basket is empty
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'Your basket is currently empty')
        return redirect(reverse('home'))

    current_basket = basket_contents(request)
    total = current_basket['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    print(intent)

    form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')
 
    return render(request, 'checkout/checkout.html', {
        'form': form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    })
