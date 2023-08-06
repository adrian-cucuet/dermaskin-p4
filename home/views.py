from django.shortcuts import render
from services.models import Service
import random


def home(request):
    """ A view for home page to render random services """
    data = list(Service.objects.all())

    # to get 4 random services
    services = random.sample(data, 4)

    context = {
        'services': services,
    }

    return render(request, 'home/index.html', context)
