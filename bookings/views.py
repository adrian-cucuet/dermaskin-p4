from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Booking
from .forms import BookingForm
from django.contrib import messages
from datetime import datetime


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


def booking_management(request):
    """ Display the user's profile. """
    today = datetime.today()
    bookings = Booking.objects.filter(date__gte=today)

    context = {
        'bookings': bookings,
    }

    return render(request, 'bookings/booking_management.html', context)


# def edit_booking(request, booking_id):
#     """ Edit a product in the store """
#     booking = get_object_or_404(Booking, pk=booking_id)
#     if request.method == 'POST':
#         form = BookingForm(request.POST, request.FILES, instance=booking)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Successfully updated \
#                  booking {booking.name}!')
#             return redirect(reverse('booking_management'))
#         else:
#             messages.error(request, 'Failed to update booking. \
#                  Please ensure the form is valid.')
#     else:
#         form = BookingForm(instance=booking)
#         messages.info(request, f'You are editing {booking.name}')

#     context = {
#         'form': form,
#         'booking': booking,
#     }

#     return render(request, 'bookings/edit_booking.html', context)
