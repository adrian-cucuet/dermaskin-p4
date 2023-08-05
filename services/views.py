from django.shortcuts import render, get_object_or_404
from .models import Service
from decimal import Decimal


def services(request):
    services = Service.objects.all()

    context = {
        'services': services,
    }

    return render(request, 'services/services.html', context)


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    price_two = service.price * 3
    package_two = price_two - (price_two * Decimal(0.15))
    price_three = service.price * 6
    package_three = price_three - (price_three * Decimal(0.25))

    context = {
        'service': service,
        'package_two': package_two,
        'package_three': package_three,
    }

    return render(request, 'services/service_detail.html', context)
