from django.forms import ModelForm
from django import forms
from .models import UploadSurvey

class UploadSurveyForm(forms.ModelForm):

    class Meta():
        model = UploadSurvey
        fields = ('surveytitle','surveylink','surveydescription','surveytype')
        widgets={
            'surveytitle': forms.TextInput(attrs={'style': 'width:500px','id':'login-input-user', 'class':'login__input'}),
            'surveylink': forms.TextInput(attrs={'style':'width:500px','id':'login-input-user', 'class':'login__input'}),
            'surveydescription':forms.Textarea(attrs={'style':'width:500px','id':'login-input-user', 'class':'login__input'}),
            'surveytype':forms.Select(attrs={'style':'width:500px','id':'login-input-user', 'class':'login__input'}),
        }
