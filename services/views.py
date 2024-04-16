from django.shortcuts import render, redirect
from .models import service, booking
from .forms import bookingform

def service_request(request):
    context = {
        'services_provided': service.objects.all()
    }
    return render(request, 'services/service.html', context)



