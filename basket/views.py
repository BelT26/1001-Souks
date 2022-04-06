from django.shortcuts import render, redirect


# Create your views here.
def view_basket(request):
    """returns a view of the contents of the basket"""
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """allows user to add items to their shopping basket"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)