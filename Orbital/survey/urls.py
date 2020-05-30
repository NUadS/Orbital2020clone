from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from survey import views as survey_views
from accounts import views as accounts_views

app_name = 'survey'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('login/',views.login_view,name='login'),
#     path('signup/',views.signup_view, name='signup')
# ]

urlpatterns=[
    path('dashboard/', survey_views.dashboard_view, name='dashboard'),
    path('survey/', survey_views.survey_view, name='survey'),
    path('rewards/', survey_views.rewards_view, name='rewards')
    
]
