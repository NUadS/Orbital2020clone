from django.forms import ModelForm
from django import forms
from .models import UploadSurvey
import datetime

class UploadSurveyForm(forms.ModelForm):
    class Meta():
        model = UploadSurvey
        fields = ('surveytitle','surveylink','surveydescription','surveycategory')
        widgets={
            'surveytitle': forms.TextInput(attrs={'style': 'width:500px'}),
            'surveylink': forms.TextInput(attrs={'style':'width:500px'}),
            'surveydescription':forms.Textarea(attrs={'style':'width:500px'}),
            'surveycategory':forms.Select(attrs={'style':'width:500px'}),
        }
