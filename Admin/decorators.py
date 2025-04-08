from django.shortcuts import render,redirect


def is_super_admin(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return fn(request,*args,**kwargs)
        else:
            return redirect('super_admin_home')
    return inner


def is_admin(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated and request.user.user_type == 'Admin':
            return fn(request,*args,**kwargs)
        else:
            return redirect('signin')
    return inner


def is_admin_or_superadmin(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser or request.user.user_type == 'Admin':
                return fn(request,*args,**kwargs)
        else:
            return redirect('signin')
    return inner