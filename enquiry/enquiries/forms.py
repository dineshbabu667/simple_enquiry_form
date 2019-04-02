from django.forms import ModelForm
from django import forms
from django.contrib.admin import widgets 

from django.forms import ModelChoiceField


from enquiries.models import EnquiryForm


class EnquiryFormDetails(forms.ModelForm):
    
    message = forms.Textarea(attrs={'rows': 2, 'cols': 30})
    class Meta:
        model= EnquiryForm
        fields='__all__'
        exclude=['created_on','modified_on','status']