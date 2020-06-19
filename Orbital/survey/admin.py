from django.contrib import admin
from .models import GenderFilter,SingaporeanFilter, FacultyFilter, YearFilter, ResidentialFilter,UploadSurvey
# Register your models here.
admin.site.register(GenderFilter)
admin.site.register(SingaporeanFilter)
admin.site.register(FacultyFilter)
admin.site.register(YearFilter)
admin.site.register(ResidentialFilter)
admin.site.register(UploadSurvey)

