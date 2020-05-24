from django.urls import path
from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'NUadvertS'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('login/',views.login_view,name='login'),
#     path('signup/',views.signup_view, name='signup')
# ]

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]
