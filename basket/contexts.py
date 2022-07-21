from decimal import Decimal
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
    multibuy_discount = 0    
  
    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            multibuy_count = item_data
            total_quantity = item_data
            product_count += item_data
         
            if product.multibuy_offer and multibuy_count >= product.multibuy_num_items:
                num_offers = multibuy_count // product.multibuy_num_items
                multibuy_amount = num_offers * product.multibuy_total
                extras = multibuy_count % product.multibuy_num_items
                multibuy_discount += ((total_quantity - extras) * product.price) - multibuy_amount

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
            multibuy_count = sum(item_data['items_by_colour'].values())
            total_quantity = 0
            for colour, quantity in item_data['items_by_colour'].items():
                # display the products as usual
                total_quantity += quantity
                product_count += quantity
                total += quantity * product.price
                subtotal = quantity * product.price
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'colour': colour,
                    'subtotal': subtotal,
            })
            if product.multibuy_offer and multibuy_count >= product.multibuy_num_items:
                # if this is a multibuy eligible product and there are enough
                # to meet the threshold,calculate how many offers we have
                num_offers = multibuy_count // product.multibuy_num_items
                # calculate the cost amount of the multibuy products
                multibuy_amount = num_offers * product.multibuy_total
                # calculate how many leftover products there are
                extras = multibuy_count % product.multibuy_num_items
                # calculate the multibuy discount
                multibuy_discount += ((total_quantity - extras) * product.price) - multibuy_amount
    # subtract the discount from the final amount
    total_after_discount = total - multibuy_discount          
    
    if total_after_discount < settings.FREE_DELIVERY_THRESHOLD:
        delivery = Decimal(settings.STANDARD_DELIVERY_CHARGE)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total_after_discount + delivery

    context = {
        'basket_items': basket_items,
        'total': total,
        'total_after_discount': total_after_discount,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'discount': multibuy_discount,
        'grand_total': grand_total,
        'product_count': product_count,
    }

    return context
