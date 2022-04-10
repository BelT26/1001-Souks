from django.shortcuts import render, redirect


# Create your views here.
def view_basket(request):
    """returns a view of the contents of the basket"""
    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """allows user to add items to their shopping basket"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    colour = None
    if 'product_colour' in request.POST:
        colour = request.POST['product_colour']
    basket = request.session.get('basket', {})

    if colour:
        if item_id in list(basket.keys()):
            if colour in basket[item_id]['items_by_colour'].keys():
                basket[item_id]['items_by_colour'][colour] += quantity
            else:
                basket[item_id]['items_by_colour'][basket] = quantity
        else:
            basket[item_id] = {'items_by_colour': {colour: quantity}}
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
        else:
            basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)



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
