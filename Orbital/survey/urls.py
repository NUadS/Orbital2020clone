from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from survey import views as survey_views
from accounts import views as accounts_views
from .views import SurveyListView, SurveyDetailView, SurveyCreateView, SurveyUpdateView, SurveyDeleteView


app_name = 'survey'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('login/',views.login_view,name='login'),
#     path('signup/',views.signup_view, name='signup')
# ]

urlpatterns=[
    path('dashboard/', survey_views.dashboard_view, name='dashboard'),
    path('survey/', survey_views.survey_view, name='survey'),
    path('uploadsurvey/', SurveyCreateView.as_view(), name='uploadsurvey'),
    path('tracksurvey/', SurveyListView.as_view() , name='tracksurvey'),
    path('tracksurvey/survey/<int:pk>/', SurveyDetailView.as_view() , name='tracksurvey-detail'),
    path('rewards/', survey_views.rewards_view, name='rewards'),
    path('tracksurvey/survey/<int:pk>/update/', SurveyUpdateView.as_view(), name='updatesurvey'),
    path('tracksurvey/survey/<int:pk>/delete/', SurveyDeleteView.as_view(), name='deletesurvey')

]
