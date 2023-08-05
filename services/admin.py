from django.contrib import admin
from .models import Service
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Service)
class ServiceAdmin(SummernoteModelAdmin):

    list_display = ('name', 'price')
    search_fields = ['name']
    list_filter = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('description', 'benefits', 'faq1_answer',
                         'faq2_answer', 'faq3_answer')
