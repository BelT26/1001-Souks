from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


def profile(request):
    """ Displays the user's profile. """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    return render(request, 'profiles/profile.html', {
        'orders': orders,
        'form': form,
        'on_profile_page': True
    })


def order_history(request, order_number):
    """
    displays details of past orders
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'The original confirmation was sent on the order date.'
    ))

    return render(request, 'checkout/checkout_success.html', {
        'order': order,
        'from_profile': True,
    })