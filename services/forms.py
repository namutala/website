from django import forms
from .models import booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = ['service_booked', 'date_booked', 'status']
        
 