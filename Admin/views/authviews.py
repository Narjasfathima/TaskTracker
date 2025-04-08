from django.shortcuts import render,redirect
from django.views.generic import View, FormView, TemplateView
from django.contrib.auth import login,authenticate,logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from Admin.forms import SignInForm




# SIGN-IN
@method_decorator([never_cache],name="dispatch")
class SignInView(FormView):
    template_name = "login.html"
    form_class = SignInForm

    def post(self,request,*args,**kwargs):
        form_data = SignInForm(data=request.POST)
        if form_data.is_valid():
            uname = form_data.cleaned_data.get("username")
            pwd = form_data.cleaned_data.get("password")
            user = authenticate(request,username=uname,password=pwd)

            if user is not None:
                if user.is_superuser or user.user_type == 'Admin':
                    login(request,user)
                    return redirect('super_admin_home')
                        
            else:
                print("error")
                return redirect('signin')
        return render(request,"login.html",{"form":form_data})
    

class SuperAdminHomeView(TemplateView):
    template_name = 'admin_nav.html'
