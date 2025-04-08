from django import forms

from .models import *
from django.contrib.auth.forms import UserCreationForm


class SignInForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Username"}))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))


class UserRegForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','username','password1','password2']
        # fields="__all__"
        widgets = {
            "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Firstname"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password1":forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}),
            "password2":forms.PasswordInput(attrs={"class":"form-control"}),
        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','username','user_type']
        widgets = {
            "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Firstname"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "user_type":forms.Select(attrs={"class":"form-control"}),
        }


class AdminRegForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','username','password1','password2']
        widgets = {
            "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Firstname"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password1":forms.PasswordInput(attrs={"class":"form-control","placeholder":"password"}),
            "password2":forms.PasswordInput(attrs={"class":"form-control"}),
        }


class AdminEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','email','username','user_type']
        widgets = {
            "first_name":forms.TextInput(attrs={"class":"form-control","placeholder":"Firstname"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "user_type":forms.Select(attrs={"class":"form-control"}),
        }


def validate_due_date(value):
    if value < timezone.now().date():
        raise forms.ValidationError("Date must be today or a future date.")
    
class TaskCreateForm(forms.ModelForm):
    due_date=forms.DateField(validators=[validate_due_date],widget=forms.DateInput(attrs={'class': 'form-control','placeholder': 'MM/DD/YYYY',}))
    
    class Meta:
        model = Task
        fields = ['title', 'assigned_to', 'due_date', 'status']

    def __init__(self, *args, **kwargs):
        super(TaskCreateForm, self).__init__(*args, **kwargs)
        self.fields['assigned_to'].queryset = CustomUser.objects.filter(user_type='User')


class TaskViewForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'assigned_to', 'due_date', 'completion_report','worked_hours']

    
