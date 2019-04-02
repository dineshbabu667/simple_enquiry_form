from django.conf.urls import include, url

app_name = 'enquiries'

from . import views

from .views import EnquiryAddForm,ListEnquiry

urlpatterns = [
            
            url(r'^(?i)enquiryform', EnquiryAddForm.as_view(), name='enquiryform'),
            url(r'^(?i)listenquiry', ListEnquiry.as_view(), name='listenquiry'),
            
]