from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q

from .models import Product, Category
from .forms import ProductForm


# Create your views here.
def all_products(request):
    """returns a view of all available products
    or those matching a query if a search term is
    provided. code adapted from boutique ado project"""
    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            context = {
                'categories': categories,
                'products': products,
            }
            return render(request, 'products/category.html', context)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search query")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'query': query,

    }
    return render(request, 'products/all_products.html', context)


def product_info(request, product_id):
    """returns a page with more detailed information about the
    selected product"""
    selected_product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': selected_product,
    }
    return render(request, 'products/product.html', context)


def add_product(request):
    """ displays a form for superusers to add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your product has been added!')
            return redirect(reverse('add_product'))
        else:
            messages.error(request, 'Unable to add product. Please check'
                                    ' that you have completed the form '
                                    'correctly.')
    else:
        form = ProductForm()

    return render(request, 'products/add_product.html', {
        'form': form,
    })
