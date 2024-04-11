from django import forms
from .models import booking

class bookingform(forms.ModelForm):
    class Meta:
        Model = booking
        fields = ['customer','service_booked', 'start_date', 'status', 'Durations']