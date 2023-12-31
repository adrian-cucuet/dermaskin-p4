from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from bookings.models import Booking


def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated successfully')
        else:
            messages.error(request, 'Update failed. \
                 Please ensure the form is valid.')

    form = UserProfileForm(instance=profile)
    bookings = profile.bookings.all().order_by('date')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'bookings': bookings,
    }

    return render(request, template, context)
