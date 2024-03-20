from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Business
from .forms import BusinessForm

@login_required(login_url='/login')
def register_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            owner= form.cleaned_data.get('owner')
            business =form.save()
            business.owner = request.user
            business.save()
            return redirect('profile')
    else:
        form = BusinessForm()
        return render(request, 'business/business.html', {'form':form})

def business_profile(request):
    return HttpResponse('Not yet implemented')