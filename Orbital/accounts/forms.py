from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User
from .models import UserProfileInfo 

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
         fields = ('matriculationNumber','age','dob','gender','nationality', 'singaporean',
         'faculty','degree','year_in_school','currentresidentialtype',
         'portfolio_site','profile_pic','email')
         
         widgets={
            'nationality': forms.Select(attrs={'style': 'width:200px'}),
            'singaporean':forms.Select(attrs={'style':'width:200px'}),
            'faculty': forms.Select(attrs={'style':'width:220px'}),
            'currentresidentialtype':forms.Select(attrs={'style':'width:130px'}),
            'gender':forms.Select(attrs={'style':'width:140px'}),
            'year_in_school':forms.Select(attrs={'style':'width:140px'})
        }
        

class UserUpdateForm(forms.ModelForm):
    class Meta():
         model = User
         fields=['username',]
         widgets={
            'username':forms.TextInput(attrs={'type':'text', 'id':'login-input-user', 'class':'login__input'}),
        }

         
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=UserProfileInfo
        fields=('matriculationNumber','age','dob','gender','nationality','singaporean',
         'faculty','degree','year_in_school','currentresidentialtype',
         'portfolio_site','profile_pic','email')

        widgets={

            'email': forms.TextInput(attrs={'type':'text', 'id':'login-input-user', 'class':'login__input'}),
            'nationality': forms.Select(attrs={'id':'login-input-user', 'class':'login__input','style': 'width:330px'}),
            'singaporean': forms.Select(attrs={'id':'login-input-user','class':'login__input','style':'width:150px'}),
            'faculty': forms.Select(attrs={'id':'login-input-user', 'class':'login__input','style':'width:250px'}),
            'currentresidentialtype':forms.Select(attrs={'id':'login-input-user', 'class':'login__input','style':'width:130px'}),
            'gender':forms.Select(attrs={'id':'login-input-user', 'class':'login__input','style':'width:150px'}),
            'year_in_school':forms.Select(attrs={'id':'login-input-user', 'class':'login__input','style':'width:250px'}),
            'matriculationNumber':forms.TextInput(attrs={'type':'text', 'id':'login-input-user', 'class':'login__input'}),
            'age':forms.NumberInput(attrs={'id':'login-input-user', 'class':'login__input'}),
            'dob':forms.TextInput(attrs={'type':'text', 'id':'login-input-user', 'class':'login__input'}),
            'degree':forms.TextInput(attrs={'type':'text', 'id':'login-input-user', 'class':'login__input'}),
            'currentresidentialtype':forms.Select(attrs={'id':'login-input-user', 'class':'login__input','style':'width:280 px'})
             
        }
