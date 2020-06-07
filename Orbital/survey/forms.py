from django.forms import ModelForm
from django import forms
from .models import UploadSurvey
import datetime

class UploadSurveyForm(forms.ModelForm):
    class Meta():
        model = UploadSurvey
        fields = ('surveytitle','surveylink','surveydescription','surveycategory')
        widgets={
            'surveytitle': forms.TextInput(attrs={'type':'text', 'id':'login-input-user', 'class':'login__input'}),
            'surveylink': forms.TextInput(attrs={'type':'text', 'id':'login-input-user', 'class':'login__input'}),
            'surveydescription':forms.Textarea(attrs={'type':'text', 'id':'login-input-user', 'class':'login__input'}),
            'surveycategory':forms.Select(attrs={'id':'login-input-user', 'class':'login__input','style': 'width:430px'}),
        }


