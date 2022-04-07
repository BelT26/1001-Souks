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

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
    }

    return context
