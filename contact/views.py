from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from .forms import QueryForm
from .models import Query


# Create your views here.
def contact(request):
    """
    returns a form for the user to contact the
    site owner
    """
    if request.method == "POST":
        form = QueryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been submitted')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Please check that you have completed '
                                    'the form correctly.')
    else:
        form = QueryForm()
    
    return render(request, 'contact/contact.html', {
        'form': form,
        'on_profile_page': True})


@login_required
@user_passes_test(lambda u: u.is_superuser)
def view_queries(request):
    """
    allows a superuser to view all submitted queries
    """
    queries = Query.objects.all()

    return render(request, 'contact/queries.html', {
        'queries' : queries
    })
