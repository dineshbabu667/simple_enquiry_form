from django.conf.urls import include, url

app_name = 'enquiries'

from . import views

from .views import EnquiryAddForm,ListEnquiry,ListEnquiryCrispyform

urlpatterns = [
            
            url(r'^(?i)enquiryform', EnquiryAddForm.as_view(), name='enquiryform'),
            url(r'^(?i)listenquiry', ListEnquiry.as_view(), name='listenquiry'),
            url(r'^(?i)enquiryfilterlist', ListEnquiryCrispyform.as_view(), name='enquiryfilterlist'),
            
]