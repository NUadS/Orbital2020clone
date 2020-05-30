from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request):
    return render(request, 'survey/dashboard.html')

@login_required
def rewards_view(request):
    return render(request, 'survey/rewards.html')

@login_required
def survey_view(request):
    return render(request, 'survey/survey.html')






