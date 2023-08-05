from django.shortcuts import render, redirect, reverse, get_object_or_404
from decimal import Decimal
from .models import Service
from .forms import ServiceForm


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


def add_service(request):
    """ Add a service to the website """
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            messages.success(request, 'Successfully added service!')
            return redirect(reverse('services', args=[service.slug]))
        else:
            messages.error(request, 'Failed to add service. \
                 Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'services/add_service.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
