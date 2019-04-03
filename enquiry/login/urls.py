from django.conf.urls import include, url

app_name = 'login'

from . import views



urlpatterns = [
            
       
         url(r'^login/',views.login,name='login'),
         url(r'^login_auth/',views.login_auth,name='login_auth'),
         url(r'logout/',views.log_out,name='logout')  
          
            
]