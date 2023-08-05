from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Booking
from .forms import BookingForm
from django.contrib import messages


def bookings(request):
    booking_form = BookingForm()
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
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        booking_form = BookingForm()
    return render(
        request, 'bookings/booking.html', {'booking_form': booking_form})


def booking_success(request, booking_number):
    save_info = request.session.get('save_info')
    booking = get_object_or_404(Booking, booking_number=booking_number)

    # if request.user.is_authenticated:
    #     profile = UserProfile.objects.get(user=request.user)
    #     # Attach the user's profile to the order
    #     booking.user_profile = profile
    #     booking.save()

    messages.success(request, f'Appointment successfully processed! \
        Your appointment number is {booking_number}.')

    template = 'bookings/booking_success.html'
    context = {
        'booking': booking,
        'booking_number': booking_number,
    }

    return render(request, template, context)
