from django.shortcuts import render
from .models import Product, Category


# Create your views here.
def all_products(request):
    """returns a view of all available products"""
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/all_products.html', context)


def category(request, category):
    """returns a page with information and products relating to the selected category"""
    context = {
        'category': category,
    }
    return render(request, 'products/category.html', context)
