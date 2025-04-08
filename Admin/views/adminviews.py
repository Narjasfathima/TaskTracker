from django.shortcuts import render,redirect
from django.views.generic import View, FormView, TemplateView, CreateView, ListView
from django.contrib.auth import login,authenticate,logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from Admin.forms import AdminRegForm, AdminEditForm
from Admin.decorators import is_super_admin
from Admin.models import CustomUser

decs = [never_cache, is_super_admin]


@method_decorator(decs,name="dispatch")
class AdminRegView(CreateView):

    def get(self,request):
        form_ob=AdminRegForm()
        return render(request,"admin_reg.html",{"form":form_ob})
    
    def post(self,request,*args,**kwargs):
        form_ob=AdminRegForm(data=request.POST)
        if form_ob.is_valid():
            user = form_ob.save(commit=False)
            user.user_type = 'User'
            user.save()
            return redirect('super_admin_home')
        return render(request,"admin_reg.html",{"form":form_ob})
    

@method_decorator(decs,name="dispatch")  
class AdminListView(ListView):
    template_name="admin_list.html"
    queryset=CustomUser.objects.all()
    context_object_name="admin"

    def get_queryset(self):
        return CustomUser.objects.filter(user_type='Admin')


@method_decorator(decs,name="dispatch")
class EditAdminView(View):
    def get(self,request,*args,**kwargs):
        uid=kwargs.get('id')
        res=CustomUser.objects.get(id=uid)
        form_ob=AdminEditForm(instance=res)
        return render(request,"edit_admin.html",{"form":form_ob})
    
    def post(self,request,*args,**kwargs):
        uid=kwargs.get('id')
        res=CustomUser.objects.get(id=uid)
        form_data=AdminEditForm(data=request.POST,instance=res)
        if form_data.is_valid():
            form_data.save()
            return redirect("admin_list")
        return render(request,"edit_admin.html",{"form":form_data})
    

decs
def delete_adminView(request,*args,**kwargs):
    uid=kwargs.get('id')
    res=CustomUser.objects.get(id=uid)
    res.delete()
    return redirect('admin_list')