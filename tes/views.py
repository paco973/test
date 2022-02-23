from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Band
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext


def band_listing(request):
    """A view of all bands."""
    bands = Band.objects.all()
    return render(request, 'bands/band_listing.html', {'bands': bands})


@login_required
def my_protected_view(request):
    """A view that can only be accessed by logged-in users"""
    return render(request, 'protected.html', {'current_user': request.user})


def homepage(request):
    """
    Shows the homepage with a welcome message that is translated in the
    user's language.
    """
    message = gettext('Welcome to our site!')
    return render(request, 'homepage.html', {'message': message})
