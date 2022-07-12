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
            product_count += item_data
            if product.multibuy_offer:
                if product_count >= product.multibuy_num_items:
                    num_offers = item_data // product.multibuy_num_items
                    extras = item_data % product.multibuy_num_items
                    multibuy_amount = num_offers * product.multibuy_total
                    extras_amount = extras * product.price
                    subtotal = multibuy_amount + extras_amount
                    total += multibuy_amount + extras_amount
                else:
                    total += item_data * product.price
                    subtotal = item_data * product.price
            else:
                total += item_data * product.price
                subtotal = item_data * product.price
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'subtotal': subtotal
            })

        else:
            product = get_object_or_404(Product, pk=item_id)
            for colour, quantity in item_data['items_by_colour'].items():
                product_count += quantity
                
                if product.multibuy_offer:
                    if product_count >= product.multibuy_num_items:
                        num_offers = quantity // product.multibuy_num_items
                        extras = quantity % product.multibuy_num_items
                        multibuy_amount = num_offers * product.multibuy_total
                        extras_amount = extras * product.price
                        subtotal = multibuy_amount + extras_amount
                        total += multibuy_amount + extras_amount
                    else:
                        total += quantity * product.price
                        subtotal = quantity * product.price
                else:
                    total += quantity * product.price
                    subtotal = quantity * product.price
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'colour': colour,
                    'subtotal': subtotal,
                })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = settings.STANDARD_DELIVERY_CHARGE
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'product_count': product_count,
    }

    return context
