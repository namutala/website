from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Business


@login_required(login_url='/login')
def register_business(request):
    if request.method == 'POST':
        return HttpResponse('Business Registered Successfully')
    else:
        return render(request, 'business/business.html')
