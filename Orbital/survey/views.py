from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UploadSurveyForm
from .models import UploadSurvey
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from django import forms


@login_required
def dashboard_view(request):
    return render(request, 'survey/dashboard.html')

@login_required
def rewards_view(request):
    return render(request, 'survey/rewards.html')

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
