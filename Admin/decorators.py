from django.shortcuts import render,redirect
from django.contrib import messages


def is_super_admin(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"Only Super Admin Can Access!!")
            return redirect('super_admin_home')
    return inner


def is_admin(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated and request.user.user_type == 'Admin':
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"Only Admin Can Access!!")
            return redirect('signin')
    return inner


def is_admin_or_superadmin(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.user_type == 'Admin':
                return fn(request,*args,**kwargs)
        else:
            messages.error(request,"Either Super Admin or Admin Can Access!!")
            return redirect('signin')
    return inner