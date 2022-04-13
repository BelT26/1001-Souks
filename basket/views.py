from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from products.models import Product


# Create your views here.
def view_basket(request):
    """returns a view of the contents of the basket"""
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """allows user to add items to their shopping basket"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    colour = None
    if 'product_colour' in request.POST:
        colour = request.POST['product_colour']
    basket = request.session.get('basket', {})

    if colour:
        if item_id in list(basket.keys()):
            if colour in list(basket[item_id]['items_by_colour'].keys()):
                basket[item_id]['items_by_colour'][colour] += quantity
                num_items = basket[item_id]['items_by_colour'][colour]
                messages.success(request, f'Updated quantity of {product.name}'
                                          f' in {colour} to {num_items}.')
            else:
                basket[item_id]['items_by_colour'][colour] = quantity
                messages.success(request, f'Added {product.name} in '
                                          f'{colour} to your basket')
        else:
            basket[item_id] = {'items_by_colour': {colour: quantity}}
            messages.success(request, f'Added {product.name} in '
                                      f'{colour} to your basket')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request, f'Updated quantity of {product.name}'
                                      f' to {basket[item_id]} items')
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['basket'] = basket
    return redirect(redirect_url)


def remove_from_basket(request, item_id):
    """Remove the item from the shopping bag"""
    product = get_object_or_404(Product, pk=item_id)
    try:
        colour = None
        if 'product_colour' in request.POST:
            colour = request.POST['product_colour']
        basket = request.session.get('basket', {})

        if colour:
            del basket[item_id]['items_by_colour'][colour]
            if not basket[item_id]['items_by_colour']:
                basket.pop(item_id)
            messages.success(request, f'Removed {product.name} in '
                                      f'{colour} from your basket')
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item{e}')
        return HttpResponse(status=500)


def adjust_basket(request, item_id):
    """allows user to change the number of items in their shopping basket"""
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    colour = None
    if 'product_colour' in request.POST:
        colour = request.POST['product_colour']
    basket = request.session.get('basket', {})

    if colour:
        if quantity > 0:
            basket[item_id]['items_by_colour'][colour] = quantity
            num_items = basket[item_id]['items_by_colour'][colour]
            messages.success(request, f'Updated quantity of {product.name}'
                                      f' in {colour} to {num_items}.')
        else:
            del basket[item_id]['items_by_colour'][colour]
            if not basket[item_id]['items_by_colour']:
                basket.pop(item_id)
            messages.success(request, f'Removed {product.name} in '
                                      f'{colour} from your basket')
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request, f'Updated quantity of {product.name}'
                                      f' to {basket[item_id]} items')
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')
    request.session['basket'] = basket
    return redirect(reverse('basket'))


# def add_to_basket(request, item_id):
#     """allows user to add items to their shopping basket"""
#     quantity = int(request.POST.get('quantity'))
#     redirect_url = request.POST.get('redirect_url')
#     colour = None
#     if 'product_colour' in request.POST:
#         colour = request.POST['product_colour']
#     size = None
#     if 'product_size' in request.POST:
#         size = request.POST['product-size']
#     basket = request.session.get('basket', {})

#     if colour:
#         if item_id in list(basket.keys()):
#             if colour in basket[item_id]['items_by_colour'].keys():
#                 if size:
#                     if item_id in list(basket.keys()):
#                         if size in basket[item_id]['items_by_size'].keys():
#                             basket[item_id]['size_colour'][size] += quantity
#                         else:
#                             basket[item_id]['size_colour'][basket] = quantity
#                 else:
#                     basket[item_id]['items_by_colour'][colour] += quantity
#             else:
#                 basket[item_id]['items_by_colour'][basket] = quantity
#         else:
#             basket[item_id] = {'items_by_colour': {colour: quantity}}
#     elif size:
#         if item_id in list(basket.keys()):
#             if size in basket[item_id]['items_by_size'].keys():
#                 basket[item_id]['items_by_size'][size] += quantity
#             else:
#                 basket[item_id]['items_by_size'][basket] = quantity
#         else:
#             basket[item_id] = {'items_by_size': {size: quantity}}
#     else:
#         if item_id in list(basket.keys()):
#             basket[item_id] += quantity
#         else:
#             basket[item_id] = quantity

#     request.session['basket'] = basket
#     return redirect(redirect_url)
