from django.shortcuts import render,redirect
from django.views.generic import View, FormView, TemplateView, CreateView, ListView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache

from Admin.forms import TaskCreateForm, TaskViewForm
from Admin.decorators import is_admin_or_superadmin
from Admin.models import CustomUser, Task

decs = [never_cache, is_admin_or_superadmin]


@method_decorator(decs,name="dispatch")
class TaskCreateView(CreateView):

    def get(self,request):
        form_ob=TaskCreateForm()
        return render(request,"add_task.html",{"form":form_ob})
    
    def post(self,request,*args,**kwargs):
        form_ob=TaskCreateForm(data=request.POST)
        if form_ob.is_valid():
            form_ob.save()
            return redirect('super_admin_home')
        return render(request,"add_task.html",{"form":form_ob})
    

@method_decorator(decs,name="dispatch")   
class TaskListView(ListView):
    template_name="manage_task.html"
    queryset=Task.objects.all()
    context_object_name="task"


@method_decorator(decs,name="dispatch")  
class EditTaskView(View):
    def get(self,request,*args,**kwargs):
        tid=kwargs.get('id')
        res=Task.objects.get(id=tid)
        form_ob=TaskCreateForm(instance=res)
        return render(request,"edit_task.html",{"form":form_ob})
    
    def post(self,request,*args,**kwargs):
        tid=kwargs.get('id')
        res=Task.objects.get(id=tid)
        form_data=TaskCreateForm(data=request.POST,instance=res)
        if form_data.is_valid():
            form_data.save()
            return redirect("task_list")
        return render(request,"edit_task.html",{"form":form_data})
    

decs
def delete_taskView(request,*args,**kwargs):
    uid=kwargs.get('id')
    res=Task.objects.get(id=uid)
    res.delete()
    return redirect('task_list')

 
@method_decorator(decs,name="dispatch")   
class CompletedTaskListView(ListView):
    template_name="completed_task.html"
    queryset=Task.objects.all()
    context_object_name="task"

    def get_queryset(self):
        return Task.objects.filter(status='Completed')
    

@method_decorator(decs,name="dispatch")  
class TaskView(View):
    def get(self,request,*args,**kwargs):
        tid=kwargs.get('id')
        res=Task.objects.get(id=tid)
        # form_ob=TaskViewForm(instance=res)
        return render(request,"task_report.html",{"i":res})