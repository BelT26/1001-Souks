from django.shortcuts import render


# Create your views here.
def index(request):
    """returns the home page template"""
    return render(request, 'home/index.html')
