from django.contrib import admin
from .models import Service
from django_summernote.admin import SummernoteModelAdmin


class ServiceAdmin(SummernoteModelAdmin):
    summernote_fields = ('benefits', 'description',
                         'faq1_answer', 'faq2_answer', 'faq3_answer',)

    list_display = ('name', 'price', 'duration',)

    list_filter = ('name', 'price',)

    ordering = ('name',)


admin.site.register(Service, ServiceAdmin)
