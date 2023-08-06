from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from datetime import datetime
from profiles.models import UserProfile
from profiles.forms import UserProfileForm


def bookings(request):

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        booking_form = BookingForm(initial={
            'name': profile.default_name,
            'email': profile.default_email,
            'phone': profile.default_phone,
        })
        if request.method == 'POST':
            booking_form = BookingForm(request.POST)
            if booking_form.is_valid():
                booking = booking_form.save(commit=False)
                booking.save()

            # Render a success page or redirect to another URL
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('booking_success', args=[booking.booking_number]))
    else:
        booking_form = BookingForm()
        messages.error(request, 'There was an error with your form. \
            Please double check your information.')

    return render(
        request, 'bookings/booking.html', {'booking_form': booking_form})


def booking_success(request, booking_number):
    save_info = request.session.get('save_info')
    booking = get_object_or_404(Booking, booking_number=booking_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        booking.user_profile = profile
        booking.save()

    messages.success(request, f'Appointment successfully processed! \
        Your appointment number is {booking_number[:8]}.')

    template = 'bookings/booking_success.html'
    context = {
        'booking': booking,
        'booking_number': booking_number,
    }

    return render(request, template, context)


def booking_management(request):
    """ Display the user's profile. """
    today = datetime.today()

    # Get all bookings scheduled for today or later
    bookings = Booking.objects.filter(date__gte=today)

    # Order the bookings by date
    bookings = bookings.order_by('date')

    context = {
        'bookings': bookings,
    }

    return render(request, 'bookings/booking_management.html', context)
