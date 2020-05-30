from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UploadSurveyForm
from django.contrib import messages


@login_required
def dashboard_view(request):
    return render(request, 'survey/dashboard.html')

@login_required
def rewards_view(request):
    return render(request, 'survey/rewards.html')

@login_required
def survey_view(request):
    return render(request, 'survey/survey.html')


def uploadsurvey_view(request):
    if request.method == 'POST':
        uploadsurvey_form = UploadSurveyForm(request.POST)
        if uploadsurvey_form.is_valid():
            uploadsurvey_form.save()
            messages.add_message(request, messages.SUCCESS, 'Your survey was updated successfully!')
            return render(request,'survey/survey.html')
    else:
        uploadsurvey_form = UploadSurveyForm()
    return render(request,'survey/uploadsurvey.html',
                          {'uploadsurvey_form':uploadsurvey_form})



def tracksurvey_view(request):
    return render(request, 'survey/tracksurvey.html')
