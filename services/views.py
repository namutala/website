from django.shortcuts import render
from .models import service, booking

def service_request(request):
    context = {
        'services_provided': service.objects.all()
    }
    return render(request, 'services/service.html', context)


def booking_request(request):
    context = {
        'booking_requests' :booking.objects.all()
    }
    return render(request, 'services/booking.html', context)

