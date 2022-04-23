from django.shortcuts import render


def profile(request):
    """ Displays the user's profile. """    
    context = {}

    return render(request, 'profiles/profile.html', context)
