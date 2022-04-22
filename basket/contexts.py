from django.shortcuts import get_object_or_404
from products.models import Product
from django.conf import settings
# the below code is based on the Boutique Ado walkthrough project


def basket_contents(request):
    """"makes basket accessible across all apps"""
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            subtotal = item_data * product.price
            product_count += item_data
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'subtotal': subtotal
            }) 

        else:
            product = get_object_or_404(Product, pk=item_id)
            for colour, quantity in item_data['items_by_colour'].items():
                total += quantity * product.price
                subtotal = quantity * product.price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'colour': colour,
                    'subtotal': subtotal,
                })

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
    }

    return context
