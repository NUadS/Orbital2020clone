from .models import UploadSurvey
from django import forms
import django_filters

class SurveyFilter(django_filters.FilterSet):
    # surveytitle = django_filters.CharFilter(lookup_expr='icontains')
    # surveydescription = django_filters.CharFilter(lookup_expr='icontains')
    # surveycategory = django_filters.MultipleChoiceFilter(choices=UploadSurvey.objects.filter().only('surveycategory'),
    #     widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = UploadSurvey
        fields = ['surveytitle','surveycategory']
