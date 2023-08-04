from django.shortcuts import render
from .models import Service


def services(request):
    service = Service.objects.all()

    context = {
        'service': service,
    }

    return render(request, 'services/services.html', context)
