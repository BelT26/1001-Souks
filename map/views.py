from django.shortcuts import render


# Create your views here.
def loction_map(request):
    """returns the map page"""
    return render(request, 'map/map.html')
