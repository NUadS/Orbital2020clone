from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UploadSurveyForm
from .models import UploadSurvey,CompletedSurveys, UserPoints
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from django import forms
from .filters import SurveyFilter
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, Sum

@login_required
def dashboard_view(request):
    profile=request.user.userprofileinfo
    target_filter= UploadSurvey.objects.filter(
            gender_filter__gender_filter=profile.gender, 
            year_filter__year_filter=profile.year_in_school, 
            faculty_filter__faculty_filter=profile.faculty, 
            singaporean_filter__singaporean_filter=profile.singaporean,
            residential_filter__residential_filter=profile.currentresidentialtype
        )
    survey_filter= SurveyFilter(request.GET, queryset=target_filter)
    context={
        'dashboardfilter': survey_filter
    }
    return render(request, 'survey/dashboard.html',context)

@login_required
def survey_view(request):
    return render(request, 'survey/survey.html')



### VIEWS FOR UPLOADSURVEY
class SurveyCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model=UploadSurvey
    form_class = UploadSurveyForm
    success_message = "Your survey was created successfully"
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class SurveyDeleteView(LoginRequiredMixin,UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model=UploadSurvey
    success_message = "Your survey was successfully deleted!"
    success_url='/tracksurvey/'

    def test_func(self):
        survey=self.get_object()
        if self.request.user == survey.user:
            return True
        return False

class SurveyUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model=UploadSurvey
    form_class=UploadSurveyForm
    success_message = "Your survey was successfully updated!"

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

    def test_func(self):
        survey=self.get_object()
        if self.request.user == survey.user:
            return True
        return False


### VIEWS FOR TRACKSURVEY
@login_required
def tracksurvey_view(request):
    context = {
        'displayedsurveys': UploadSurvey.objects.filter(user=request.user)
    }
    return render(request, 'survey/tracksurvey.html', context)

class SurveyListView(LoginRequiredMixin,ListView):
    model=UploadSurvey
    template_name = 'survey/tracksurvey.html'
    context_object_name= 'allsurveys'
    ordering=['-uploadDate']

class SurveyDetailView(DetailView):
    model=UploadSurvey


### VIEWS FOR COMPLETEDSURVEYS
def completedsurveys_view(request):
    context = {
        'allcompletedsurveys': CompletedSurveys.objects.get(user=request.user)
    }
    return render(request, 'survey/completedsurveys.html', context)


### VIEWS FOR NEWLY COMPLETED SURVEY
def completedsurveys_update(request, pk):
    try:
        user_completedsurveys = CompletedSurveys.objects.get(user=request.user)
    except ObjectDoesNotExist:
        user_completedsurveys = CompletedSurveys.objects.create(user=request.user)
        user_completedsurveys.save()

    newsurvey = UploadSurvey.objects.get(pk=pk)
    user_completedsurveys.completedsurveys.add(newsurvey)
    

    earned_points = UserPoints.objects.create(user=request.user)

    messages.success(request, 'Survey {} completed successfully'.format(pk))
    return redirect('survey:dashboard')


### VIEWS FOR REWARDS
@login_required
def rewards_view(request):
    context={
        'displayedpoints':UserPoints.objects.filter(user=request.user).aggregate(Sum('points_amount'))
    }
    return render(request, 'survey/rewards.html', context)

