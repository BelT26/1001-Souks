from django.shortcuts import render


# Create your views here.
def all_products(request):
    """returns a view of all available products"""
    return render(request, 'products/all_products.html')
