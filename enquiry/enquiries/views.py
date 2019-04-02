from django.shortcuts import render

from django.shortcuts import render,get_list_or_404, get_object_or_404

# generic views 
from django.views.generic.edit import CreateView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView,View

# redirect 

from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers  import reverse

# time 
from datetime import date
import datetime

from django.contrib import messages
# sum 
from django.db.models import Q
from django.db.models import Count, Min, Sum, Avg

# ajax
from django_ajax.decorators import ajax

# tables
from django_tables2 import RequestConfig
from decimal import getcontext, Decimal
from crispy_forms.layout import Submit,ButtonHolder,Reset


from enquiries.models import EnquiryForm
from enquiries.forms import EnquiryFormDetails
from enquiries.tables import Enquiry_Table

# Create your views here.

class EnquiryAddForm(CreateView):
    form_class = EnquiryFormDetails
    template_name = 'enquiries/enquiry_form.html'
    
    def get_context_data(self, **kwargs):
       context = super(EnquiryAddForm, self).get_context_data(**kwargs)
       context['Title'] = 'Enquiry Form'
       return context
    def get_success_url(self, **kwargs):
        messages.add_message(self.request, messages.SUCCESS, 'Enquiry Submitted Successfully')
        return reverse("enquiries:enquiryform")
    
    
class ListEnquiry(ListView):
    #import ipdb;ipdb.set_trace()
    model = EnquiryForm
    template_name = 'enquiries/enquiry_list.html'
    def get_queryset(self, **kwargs):
        return EnquiryForm.objects.all()
    
    def get_context_data(self,**kwargs):
        context=super(ListEnquiry, self).get_context_data(**kwargs)
        context['Title'] = 'List Enquiry'
        #enquiries_qs = EnquiryForm.objects.all()
        #EnquiryTable = Enquiry_Table(enquiries_qs)
        #context['table'] = EnquiryTable
      
        return context
    
    
    
