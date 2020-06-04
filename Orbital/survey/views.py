from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UploadSurveyForm
from .models import UploadSurvey
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime

@login_required
def dashboard_view(request):
    return render(request, 'survey/dashboard.html')

@login_required
def rewards_view(request):
    return render(request, 'survey/rewards.html')

@login_required
def survey_view(request):
    return render(request, 'survey/survey.html')

@login_required
def uploadsurvey_view(request):
    if request.method == 'POST':
        uploadsurvey_form = UploadSurveyForm(request.POST)
        if uploadsurvey_form.is_valid():
            USform = uploadsurvey_form.save(commit=False)
            USform.user = request.user
            USform.save()
            messages.success(request, 'Your survey is successfully uploaded!')
            return render(request,'survey/survey.html')
    else:
        uploadsurvey_form = UploadSurveyForm()
    return render(request,'survey/uploadsurvey.html',
                          {'uploadsurvey_form':uploadsurvey_form})



def tracksurvey_view(request):
    return render(request, 'survey/tracksurvey.html')
