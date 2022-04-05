from django.shortcuts import render


# Create your views here.
def basket(request):
    """returns a view of the contents of the basket"""
    return render(request, 'basket/basket.html')