from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    """ Display the Queries in the Admin Panel """

    list_display = ('name', 'date',
                    'time', 'service', 'package',)

    search_fields = ['name', 'service',]

    list_filter = ('name', 'date',)

    ordering = ('date',)


admin.site.register(Booking, BookingAdmin)
