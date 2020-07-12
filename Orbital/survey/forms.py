from django.forms import ModelForm
from django import forms
from .models import UploadSurvey, Report
import datetime

class UploadSurveyForm(forms.ModelForm):

    class Meta():
        model = UploadSurvey
        fields = ('surveytitle','surveylink','surveydescription','surveycategory','gender_filter','singaporean_filter','faculty_filter','year_filter','residential_filter')
        widgets={
            'surveytitle': forms.TextInput(attrs={'type':'text', 'id':'login-input-user', 'class':'login__input'}),
            'surveylink': forms.TextInput(attrs={'type':'text', 'id':'login-input-user', 'class':'login__input'}),
            'surveydescription':forms.Textarea(attrs={'type':'text', 'id':'login-input-user', 'class':'login__input'}),
            'surveycategory':forms.Select(attrs={'id':'login-input-user', 'class':'login__input','style': 'width:430px'}),
            'gender_filter': forms.CheckboxSelectMultiple(),
            'singaporean_filter': forms.CheckboxSelectMultiple(),
            'faculty_filter': forms.CheckboxSelectMultiple(),
            'year_filter': forms.CheckboxSelectMultiple(),
            'residential_filter': forms.CheckboxSelectMultiple()


        }

class ReportForm(forms.ModelForm):
    class Meta():
        model = Report
        fields = ('user','subject','details')
        widgets={
            'subject':forms.TextInput(attrs={'type':'text', 'id':'login-input-user', 'class':'login__input'}),
            'details':forms.Textarea(attrs={'type':'text', 'id':'login-input-user', 'class':'login__input'})
        }
