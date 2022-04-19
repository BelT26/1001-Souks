# adapted from Boutique Ado project
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


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

    form = OrderForm()
    
    return render(request, 'checkout/checkout.html', {
        'form': form,
    })
