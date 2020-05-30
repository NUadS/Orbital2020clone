from django.forms import ModelForm
from django import forms
from .models import UploadSurvey

class UploadSurveyForm(forms.ModelForm):

    class Meta():
        model = UploadSurvey
        fields = ('surveytitle','surveylink','surveydescription','surveytype')
        widgets={
            'surveytitle': forms.TextInput(attrs={'style': 'width:500px'}),
            'surveylink': forms.TextInput(attrs={'style':'width:500px'}),
            'surveydescription':forms.Textarea(attrs={'style':'width:500px'}),
            'surveytype':forms.Select(attrs={'style':'width:500px'}),
        }
