from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type':"password"}))
    class Meta():
        model = User
        fields = ('username','password')
        widgets={
            'username':forms.TextInput(attrs={'type':'text'}),

        }

class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('matriculationNumber','age','dob','gender','nationality',
         'faculty','degree','year_in_school','currentresidentialtype',
         'portfolio_site','profile_pic','email')
         
         widgets={
            'nationality': forms.Select(attrs={'style': 'width:200px'}),
            'faculty': forms.Select(attrs={'style':'width:220px'}),
            'currentresidentialtype':forms.Select(attrs={'style':'width:130px'}),
            'gender':forms.Select(attrs={'style':'width:140px'}),
            'year_in_school':forms.Select(attrs={'style':'width:140px'})
        }

         

         
