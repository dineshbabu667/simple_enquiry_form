from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.views import password_reset,PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.
def login(request):
    context = {}
    context.update(csrf(request))
    #return render_to_response('kmine_auth/login.html',c)
    return render(request, 'login/login.html', context)


def login_auth(request):
    
    username= request.POST.get('username')
    password = request.POST.get('password')
    
    try:
        findUser = username
    except User.DoesNotExist:
        findUser = None
        
    if findUser is not None:
        caseSensitiveUsername = findUser
        user = auth.authenticate(username=caseSensitiveUsername,password=password)
    else:
        user = None
        
    if user is not None:
        auth.login(request,user) 
        print('authenticated')
        return HttpResponseRedirect('/enquiryform/',)
        
    else:
        Error_Text = "Login Details are invalid"
        return render(request, 'login/login.html',{'Error_Text': Error_Text})
    
    
def log_out(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/login/',)

'''
class ChangePasswordView(PasswordChangeView):
    template_name = 'login/change_password.html'
    form_class = PasswordChangeForm
    def get_success_url(self, **kwargs):    
        messages.add_message(self.request, messages.SUCCESS, 'Staff Password Updated Successfully')     
        return reverse("kmine_auth:change_password")
'''


class EmailAuthBackend():
    def authenticate(self, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(raw_password=password):
                return user
            return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None