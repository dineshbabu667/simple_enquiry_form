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
from enquiries.tables import Enquiry_Table,Enquiry_TableFilter,Enquiry_Search_Form

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
        enquiries_qs = EnquiryForm.objects.all()
        EnquiryTable = Enquiry_Table(enquiries_qs)
        context['table'] = EnquiryTable
      
        return context
    
class ListEnquiryCrispyform(ListView):
    #import ipdb;ipdb.set_trace()
    model = EnquiryForm
    template_name = 'enquiries/enquiry_list_with_filter.html'
    def get_queryset(self, **kwargs):
        return EnquiryForm.objects.all()
    
    def get_context_data(self,**kwargs):
        context=super(ListEnquiryCrispyform, self).get_context_data(**kwargs)
        context['Title'] = 'List Enquiry'
        filter = Enquiry_TableFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = Enquiry_Search_Form()
        filter.form.helper.add_input(Submit('submit', 'Search',css_class="btn btn-default"))
        filter.form.helper.add_input(Reset('Clear', 'Clear',css_class="btn btn-default",css_id='reset-billid-clear'))
        filter.form.helper.add_input(Reset('Reset Search','Reset Search',css_class="btn btn-default",css_id='reset-search'))
        Table = Enquiry_Table(filter.qs)
        RequestConfig(self.request, paginate={'per_page': 20}).configure(Table)
        context['table'] = Table
        context['filter'] = filter
      
        return context  
    



# ajax
'''
#@ajax
def get_producttype_list(request):
    type = request.POST['category_id']
    
    try:
        #import ipdb;ipdb.set_trace()
        product_type_qs = ProductType.objects.filter(category = type)
        product_type_list = []
        for item in product_type_qs:
                head_acc_tmp = {}
                head_acc_tmp['id'] =item.id
                head_acc_tmp['name'] =item.name
               
               
                product_type_list.append(head_acc_tmp)
                
    except:
        head_acc_list = ''
        
    json_data = {
        'product_type_list':product_type_list,
        }
         
    
    return json_data 

#@ajax
def get_productitem_list(request):
    type = request.POST['producttype_id']
    
    try:
        #import ipdb;ipdb.set_trace()
        product_item_qs = Purchase.objects.filter(Q(producttype = type) & Q(status=0))
        product_item_list = []
        for item in product_item_qs:
                head_acc_tmp = {}
                head_acc_tmp['id'] =item.id
                head_acc_tmp['name'] =item.name
                product_item_list.append(head_acc_tmp)
    except:
        head_acc_list = ''
        
    json_data = {
        'product_item_list':product_item_list,
        }
         
    
    return json_data 


#@ajax
def get_productitemdetail_ajax(request):
    producttype_id = request.POST['producttype_id']
    try:
        #import ipdb;ipdb.set_trace()
        product_qs = Purchase.objects.get(id = producttype_id)
        product_name = product_qs.name
        supplier = product_qs.supplier
        purchase_type=product_qs.purchase_type
        gold_weight = product_qs.gold_weight
               
    except:
        student_name = ''
        student_Surname =''
        student_Gender =''
        student_Date_of_Birth =''
        student_age =''
        student_Home_address =''
     
        
        
    json_data = {
        'student_name':student_name,
        'student_Surname':student_Surname,
        'student_Gender': student_Gender,
        'student_Date_of_Birth':student_Date_of_Birth,
        'student_age':student_age,
        'student_Home_address' :student_Home_address,
      
        }
         
    
    return json_data 
'''
