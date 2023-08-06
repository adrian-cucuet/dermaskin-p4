from django.contrib import admin
from .models import Booking


class BookingAdmin(admin.ModelAdmin):
    """ Display the Queries in the Admin Panel """

    list_display = ('name', 'date', 'time',
                    'service', 'package', 'status',)

    search_fields = ['name', 'service', ]

    list_filter = ('name', 'date', 'status',)

    ordering = ('date',)


admin.site.register(Booking, BookingAdmin)
