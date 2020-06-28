from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UploadSurveyForm
from .models import UploadSurvey, CompletedSurveys, TotalPoints, Reward, RedeemedRewards
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from django import forms
from .filters import SurveyFilter
from django.core.exceptions import ObjectDoesNotExist
# from django.db.models import Avg, Sum
from django.db.models import F



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
    success_url='/createdsurveys/'

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


### VIEWS FOR createdsurveys
@login_required
def createdsurveys_view(request):
    context = {
        'createdsurveys': UploadSurvey.objects.filter(user=request.user)
    }
    return render(request, 'survey/createdsurveys.html', context)

class SurveyListView(LoginRequiredMixin,ListView):
    model=UploadSurvey
    template_name = 'survey/createdsurveys.html'
    context_object_name= 'allsurveys'
    ordering=['-uploadDate']

class SurveyDetailView(DetailView):
    model=UploadSurvey


### VIEWS FOR DASHBOARDFILTER
@login_required
def dashboard_view(request):
    survey_filter= SurveyFilter(request.GET, queryset=UploadSurvey.objects.all())
    profile=request.user.userprofileinfo
    context={
        'displayedsurveys':UploadSurvey.objects.filter(
            gender_filter__gender_filter=profile.gender,
            year_filter__year_filter=profile.year_in_school,
            faculty_filter__faculty_filter=profile.faculty,
            singaporean_filter__singaporean_filter=profile.singaporean,
            residential_filter__residential_filter=profile.currentresidentialtype,
            # completedsurveys__isnull=True
            ),
        'dashboardfilter': survey_filter,
    }
    return render(request, 'survey/dashboard.html',context)

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

    try:
        user_totalpoints = TotalPoints.objects.get(user=request.user)
    except ObjectDoesNotExist:
        user_totalpoints = TotalPoints.objects.create(user=request.user)
        user_totalpoints = TotalPoints.objects.get(user=request.user)

    user_totalpoints.points = F('points') + 1
    user_totalpoints.save()

    messages.success(request, 'Survey {} completed successfully'.format(pk))
    return redirect('survey:dashboard')


### VIEWS FOR REWARDS
@login_required
def rewards_view(request):
    return render(request, 'survey/rewards.html')


@login_required
def shoprewards_view(request):
    context={
        'displayedpoints': TotalPoints.objects.get_or_create(user=request.user),
        'displayedrewards':Reward.objects.all()
    }
    return render(request, 'survey/shoprewards.html', context)


def redeem_update(request,pk):
    try:
        user_redeemedrewards = RedeemedRewards.objects.get(user=request.user)
    except ObjectDoesNotExist:
        user_redeemedrewards = RedeemedRewards.objects.create(user=request.user)
        user_redeemedrewards.save()

    newredeemedreward = Reward.objects.get(pk=pk)
    user_redeemedrewards.redeemedrewards.add(newredeemedreward)

    user_totalpoints = TotalPoints.objects.get(user=request.user)
    requiredpoints = newredeemedreward.requiredpoints

    if user_totalpoints.points < requiredpoints:
        messages.error(request, 'Insufficient points to redeem reward')
    else:
        user_totalpoints.points = F('points') - requiredpoints
        user_totalpoints.save()
        messages.success(request, 'Reward {} redeemed successfully'.format(pk))
    return redirect('survey:shoprewards')


### VIEWS FOR REDEEMEDREWARDS
def redeemedrewards_view(request):
    context = {
        'allredeemedrewards': RedeemedRewards.objects.get(user=request.user)
    }
    return render(request, 'survey/redeemedrewards.html', context)
