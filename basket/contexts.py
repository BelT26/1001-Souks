def basket_contents(request):
    """"makes basket accessible across all apps"""
    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'basket': basket
    }

    return context
