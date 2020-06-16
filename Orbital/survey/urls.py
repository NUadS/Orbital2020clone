from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from survey import views as survey_views
from accounts import views as accounts_views
from .views import SurveyListView, SurveyDetailView, SurveyCreateView, SurveyUpdateView, SurveyDeleteView


app_name = 'survey'

urlpatterns=[
    path('dashboard/', survey_views.dashboard_view, name='dashboard'),
    path('survey/', survey_views.survey_view, name='survey'),
    path('uploadsurvey/', SurveyCreateView.as_view(), name='uploadsurvey'),
    path('createdsurveys/', survey_views.createdsurveys_view , name='createdsurveys'),
    path('createdsurveys/survey/<int:pk>/', SurveyDetailView.as_view() , name='createdsurveys-detail'),
    path('createdsurveys/survey/<int:pk>/update/', SurveyUpdateView.as_view(), name='updatesurvey'),
    path('createdsurveys/survey/<int:pk>/delete/', SurveyDeleteView.as_view(), name='deletesurvey'),
    path('completedsurveys/', survey_views.completedsurveys_view , name='completedsurveys'),
    path('dashboard/<int:pk>/', survey_views.completedsurveys_update , name='completedsurveys_update'),

    path('rewards/', survey_views.rewards_view, name='rewards'),
]
