from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from products.models import Product
from .models import City, Maker
from .forms import MakerForm


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


@login_required
@user_passes_test(lambda u: u.is_superuser)
def add_maker(request):
    """ displays a form for superusers to add a new category """
    if request.method == 'POST':
        form = MakerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'A new maker has been added!')
            return redirect(reverse('add_maker'))
        else:
            messages.error(request, 'Unable to add maker. Please check'
                                    ' that you have completed the form '
                                    'correctly.')
    else:
        form = MakerForm()

    return render(request, 'map/add_maker.html', {
        'form': form,
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_maker(request, maker_id):
    """ displays a form to update an artisan's details """
    maker = get_object_or_404(Maker, pk=maker_id)
    if request.method == 'POST':
        form = MakerForm(request.POST, request.FILES, instance=maker)
        if form.is_valid():
            form.save()
            messages.success(request, 'The maker info has been updated.')
            return redirect(reverse('city_detail', args=[maker.city.name]))
        else:
            messages.error(request, 'Unable to update maker. Please '
                                    'check the details entered on the form.')
    else:
        form = MakerForm(instance=maker)

    return render(request, 'map/edit_maker.html', {
        'form': form,
        'maker': maker,
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_maker(request, maker_id):
    """ Delete a maker """
    maker = get_object_or_404(Maker, pk=maker_id)
    maker.delete()
    messages.success(request, 'Maker deleted!')
    return redirect(reverse('map'))
