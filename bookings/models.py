import uuid
from django.db import models
from datetime import datetime
from profiles.models import UserProfile

TIME = (
    ('10.00 - 11.00', '10.00 - 11.00'),
    ('11.00 - 12.00', '11.00 - 12.00'),
    ('12.00 - 13.00', '12.00 - 13.00'),
    ('13.00 - 14.00', '13.00 - 14.00'),
    ('14.00 - 15.00', '14.00 - 15.00'),
    ('15.00 - 16.00', '15.00 - 16.00'),
    ('16.00 - 17.00', '16.00 - 17.00'),
    ('17.00 - 18.00', '17.00 - 18.00'),
    )
SERVICE = (
    ('Microneedling', 'Microneedling'),
    ('Facial', 'Facial'),
    ('Chemical Peel', 'Chemical Peel'),
    ('Microdermabrasion', 'Microdermabrasion'),
    ('Botox', 'Botox'),
    ('Derma Fillers', 'Derma Fillers'),
    ('Laser treatments', 'Laser treatments'),
    ('IPL (Intense Pulsed Light)', 'IPL (Intense Pulsed Light)'),
    )
PACKAGE = (
    ('Package Bronze', 'Package Bronze'),
    ('Package Silver', 'Package Silver'),
    ('Package Gold', 'Package Gold'),
)
STATUS = (
    (0, 'Pending'),
    (1, 'Approved'),
    (2, 'Canceled'),
)


class Booking(models.Model):

    booking_number = models.CharField(max_length=50, null=False,
                                      editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='bookings')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=False, blank=False)
    service = models.CharField(max_length=50, choices=SERVICE)
    package = models.CharField(max_length=50, choices=PACKAGE)
    date = models.DateField()
    time = models.CharField(max_length=15, choices=TIME)
    status = models.CharField(max_length=100, choices=STATUS,
                              default=STATUS[0])

    def _generate_booking_number(self):
        """
        Generate a random, unique order number using UUID
        """

        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.booking_number:
            self.booking_number = self._generate_booking_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.booking_number
