from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'survey'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('login/',views.login_view,name='login'),
#     path('signup/',views.signup_view, name='signup')
# ]

urlpatterns=[
    url(r'^$',views.index,name='index')
]
