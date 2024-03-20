from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Business, Catalogue
from .forms import BusinessForm, CatalogueForm

@login_required(login_url='/login')
def register_business(request):
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            owner= form.cleaned_data.get('owner')
            business =form.save()
            business.owner = request.user
            business.save()
            return redirect('catalogue')
    else:
        form = BusinessForm()
    return render(request, 'business/business.html', {'form':form})

def add_catalogue(request):
    if request.method == 'POST':
        CartForm= CatalogueForm(request.POST)
        if CartForm.is_valid():
            cart = CartForm.save()
            return redirect('login')
    else:
        CartForm =CatalogueForm()
    return render(request, 'business/catalogue.html', {'CartForm':CartForm})
