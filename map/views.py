from django.shortcuts import render, get_object_or_404
from .models import City, Maker
from .forms import MakerForm
from products.models import Product



# Create your views here.
def loction_map(request):
    """returns the map page"""
    return render(request, 'map/map.html')


def city_detail(request, city_name):
    """returns a page with more detailed information about the
    selected city"""
    selected_city = get_object_or_404(City, name=city_name)
    makers = Maker.objects.filter(city=selected_city)
    products = Product.objects.all()
    context = {
        'city': selected_city,
        'makers': makers,
        'products': products,

    }
    return render(request, 'map/city.html', context)


def add_maker(request):
    """ displays a form for superusers to add a new category """
    form = MakerForm()

    return render(request, 'products/add_maker.html', {
        'form': form,
    })
