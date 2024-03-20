from django import forms
from .models import Business

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields =['owner', 'business_name','logo','business_description','location', 'email', 'contact']