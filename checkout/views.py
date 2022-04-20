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
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, 'Your basket is currently empty')
        return redirect(reverse('home'))

    current_basket = basket_contents(request)
    total = current_basket['total']
    stripe_total = round(total * 100)

    form = OrderForm()
    
    return render(request, 'checkout/checkout.html', {
        'form': form,
        'stripe_public_key': 'pk_test_51KVCjXLzPYZbKFCeKtJpmj7yQ4hByR7OUxl0NVO8EKsr4qBviIwtAE53x3k9ikM2TWIJJK0wLG0atu1LJi5sPj1i00isbVub7I',
        'client_secret': 'test',
    })
