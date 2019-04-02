import django_tables2 as tables
from django_tables2.utils import A

from datetime import date
from django.db.models import Q

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

import django_filters 
from django_filters import DateRangeFilter,DateFilter

from django.template.defaultfilters import date


from django_select2.forms import ModelSelect2Widget,Select2Widget

from django.contrib.auth.models import User

from enquiries.models import EnquiryForm

class Enquiry_Table(tables.Table):
   
   # BUTTON_TEMPLATE = """ <a  href="{% url 'jewellery:edit_category' record.id %}" title="Edit" ><i class="fa fa-edit "> </i></a>
   # """
    #Actions = tables.TemplateColumn(BUTTON_TEMPLATE,orderable=False )
    
   
    class Meta:
         model =  EnquiryForm
         orderable = True
         attrs = {'class': 'table table-striped table-bordered table-hover','id':'Table_list'}
         fields=['name','status']
         
         
class Enquiry_TableFilter(django_filters.FilterSet):
    
    created_min = django_filters.DateFilter(name='created_on', lookup_expr='gte',label='From Date')
    created_max = django_filters.DateFilter(name='created_on', lookup_expr='lte',label='To Date')
    name = django_filters.CharFilter(lookup_expr='icontains',label='Name')
    
   
    class Meta:
        model =EnquiryForm
        fields=['name','status']
       
class Enquiry_Search_Form(FormHelper):
    
        model = EnquiryForm
        form_id = 'Bill_Search_Form'
        form_method = 'get'
        form_class = 'form-horizontal'
        form_role = 'form'
        label_class = 'col-md-3'
        field_class = 'col-md-5'
        

        