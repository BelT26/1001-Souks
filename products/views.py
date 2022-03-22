from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


# Create your views here.
def all_products(request):
    """returns a view of all available products
    or those matching a query if a search term is
    provided. code copied from boutique ado project"""
    products = Product.objects.all()
    query = None

    if request.GET:
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


def chosen_category(request, category_name):
    """returns a page with information and products relating to the selected category"""
    selected_category = get_object_or_404(Category, name=category_name)
    selected_products = Product.objects.filter(category=selected_category)
    context = {
        'category': selected_category,
        'products': selected_products,
    }
    return render(request, 'products/category.html', context)


def product_info(request, product_id):
    """returns a page with more detailed information about the selected product"""
    selected_product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': selected_product,
    }
    return render(request, 'products/product.html', context)


