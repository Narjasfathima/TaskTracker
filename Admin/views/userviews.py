from django.shortcuts import render,redirect
from django.views.generic import View, FormView, TemplateView, CreateView, ListView
from django.contrib.auth import login,authenticate,logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from Admin.forms import UserRegForm, UserEditForm
from Admin.models import CustomUser


class UserRegView(CreateView):

    def get(self,request):
        form_ob=UserRegForm()
        return render(request,"user_reg.html",{"form":form_ob})
    
    def post(self,request,*args,**kwargs):
        form_ob=UserRegForm(data=request.POST)
        if form_ob.is_valid():
            user = form_ob.save(commit=False)
            user.user_type = 'User'
            user.save()
            return redirect('super_admin_home')
        return render(request,"user_reg.html",{"form":form_ob})
    

# @method_decorator(decs2,name="dispatch")   
class UsersListView(ListView):
    template_name="user_list.html"
    queryset=CustomUser.objects.all()
    context_object_name="user"

    def get_queryset(self):
        return CustomUser.objects.filter(user_type='User')


class EditUserView(View):
    def get(self,request,*args,**kwargs):
        uid=kwargs.get('id')
        res=CustomUser.objects.get(id=uid)
        form_ob=UserEditForm(instance=res)
        return render(request,"edit_user.html",{"form":form_ob})
    
    def post(self,request,*args,**kwargs):
        uid=kwargs.get('id')
        res=CustomUser.objects.get(id=uid)
        form_data=UserEditForm(data=request.POST,instance=res)
        if form_data.is_valid():
            form_data.save()
            return redirect("user_list")
        return render(request,"edit_user.html",{"form":form_data})
    

def delete_userView(request,*args,**kwargs):
    uid=kwargs.get('id')
    res=CustomUser.objects.get(id=uid)
    res.delete()
    return redirect('user_list')