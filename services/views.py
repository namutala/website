from django.shortcuts import render, redirect
from .models import service, booking
from .forms import bookingform

def service_request(request, service_id):
    context = {
        'services_provided': service.objects.all()
    }
    return render(request, 'services/service.html', context)


def book_service(request, service_id):
    Service = service.objects.get(pk =service_id)
    if request.method == "POST":
        form = bookingform(request.POST)
        if form.is_valid():
            book = form.save(commit = False)
            book.customer = request.user
            book.save()
            return redirect('services')
    else:
        form = bookingform()
    return render(request, 'services/booking.html', {'form': form, 'service': service})
