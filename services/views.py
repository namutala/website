from django.shortcuts import render, redirect
from .models import service, booking
from .forms import BookingForm
from django.contrib import messages
def service_request(request):
    context = {
        'services_provided': service.objects.all()
    }
    return render(request, 'services/service.html', context)

def book_service(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid:
            form.save()
            service_booked = form.cleaned_data.get('service')
            customer = form.cleaned_data.get('customer')
            messages.success = (request, f"{service_booked} has been booked for {customer}")
            return redirect('services')
    else:
        form = BookingForm()
    return render(request, 'services/booking.html', {'form': form })




