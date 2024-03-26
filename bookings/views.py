from django.shortcuts import render
from .models import service, booking


def service_request(request):
    context = {
        'services': service.objects.all()
    }
    return render(request, 'bookings/services.html', context)

def booking_request(request):
    context = {
        'book': booking.objects.all()
    }
    return render(request, 'bookings/booking.html', context)




